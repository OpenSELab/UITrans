import os
import json
import asyncio
from sqlalchemy import select, inspect, delete

from core.db.model.base import Base
from core.db.model.translation import TranslationTable
from core.config.config_loader import ConfigLoader
from core.db.session import SessionManager

os.chdir("../")
config = ConfigLoader.from_file("config.yaml")


async def init_db():
    session = SessionManager(config.db_config)
    async with session.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_db()
    with open("script/initialize_database/component_table.json", "r", encoding="utf-8") as f:
        translations = json.loads(f.read())
    translation_list = []
    for translation in translations:
        translation_list.append(TranslationTable(
            source_language=translation["source_language"],
            source_component=translation["source_component"],
            source_component_code=translation["source_component_code"],
            source_component_description=translation["source_component_description"],
            source_component_version=translation["source_component_version"],
            target_language=translation["target_language"],
            target_component=translation["target_component"],
            target_component_code=translation["target_component_code"],
            target_component_description=translation["target_component_description"],
            target_component_version=translation["target_component_version"]
        ))
    async with SessionManager(config.db_config) as session:
        # await session.execute(TranslationTable.__table__.delete())
        # session.add_all(translation_list)
        # await session.commit()
        result = await session.execute(select(TranslationTable))
        translations = result.scalars().all()
    print(translations)


asyncio.run(main())
