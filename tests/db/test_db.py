import os

import pytest
import pytest_asyncio

from sqlalchemy.future import select
from core.config.schema import DBConfig
from core.db.model.base import Base
from core.db.model.translation import TranslationTable
from core.db.session import SessionManager


@pytest_asyncio.fixture
async def test_session_manager() -> SessionManager:
    """
    Set up a temporary in-memory database for testing.

    This fixture is an async context manager.
    """
    db_cfg = DBConfig(url="sqlite+aiosqlite:///:memory:")
    manager = SessionManager(db_cfg)
    async with manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield manager


@pytest.mark.asyncio
async def test_db(test_session_manager):
    """
    Set up a temporary in-memory database for testing.

    This fixture is an async context manager that yields
    a database session.
    """
    async with test_session_manager as session:
        # 插入数据
        translation = TranslationTable(
            source_language="android",
            source_component="android_test_component",
            source_component_code="android_test_component_code",
            source_component_description="android_test_component_description",
            source_component_version="0.1",
            target_language="harmony",
            target_component="harmony_test_component",
            target_component_code="harmony_test_component_code",
            target_component_description="harmony_test_component_description",
            target_component_version="0.1"
        )
        session.add(translation)
        await session.commit()

        result = await session.execute(select(TranslationTable))
        translations = result.scalars().all()
        print(translations)


@pytest.mark.asyncio
async def test_insert_component_table(test_session_manager):
    import json
    print(os.path.exists("./db/component_table.json"))
    with open("./db/component_table.json", "r", encoding="utf-8") as f:
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
    print(translation_list)
    async with test_session_manager as session:
        ...
