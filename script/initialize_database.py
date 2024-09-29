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
    async with session.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    session = SessionManager(config.db_config)
    async with session.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def insert():
    translation = TranslationTable(
            source_language="android",
            source_component="androidx.cardview.widget.CardView",
            source_component_code="<androidx.cardview.widget.CardView\n        android:layout_width=\"match_parent\"\n        android:layout_height=\"wrap_content\"\n        android:layout_marginBottom=\"16dp\"\n        android:backgroundTint=\"@color/cardview_light_background\"\n        app:cardCornerRadius=\"12dp\"\n        app:cardElevation=\"8dp\"\n        app:cardUseCompatPadding=\"true\"\n        app:strokeWidth=\"1dp\"\n        app:strokeColor=\"@color/cardview_shadow_start_color\">\n\n    <LinearLayout\n            android:layout_width=\"match_parent\"\n            android:layout_height=\"wrap_content\"\n            android:orientation=\"vertical\"\n            android:padding=\"20dp\">\n\n        <TextView\n                android:layout_width=\"wrap_content\"\n                android:layout_height=\"wrap_content\"\n                android:text=\"Elegant Card Title 1\"\n                android:textSize=\"20sp\"\n                android:textStyle=\"bold\"\n                android:textColor=\"@color/design_default_color_on_primary\"\n                 />\n\n        <TextView\n                android:layout_width=\"wrap_content\"\n                android:layout_height=\"wrap_content\"\n                android:text=\"This is an enhanced description for Card 1. It has more padding and better styling.\"\n                android:textSize=\"16sp\"\n                android:lineSpacingExtra=\"4dp\"\n                android:textColor=\"@color/design_default_color_on_primary\"\n                android:layout_marginTop=\"8dp\"\n                />\n    </LinearLayout>\n</androidx.cardview.widget.CardView>",
            source_component_description="一个带有自定义样式的 CardView，卡片具有 12dp 的圆角、8dp 的阴影高度，并设置了 1dp 宽的边框，边框颜色和背景颜色可通过资源文件进行自定义。卡片内部使用了一个垂直布局，其中包含 20sp 的加粗标题 和 16sp 描述文字。描述文字通过 4dp 的额外行间距 提高了可读性，并在标题和描述之间设置了 8dp 的上边距。",
            source_component_version="1",
            target_language="harmony",
            target_component=["Column", "Text"],
            target_component_code="      Column() {\n        Column() {\n          Text('Elegant Card Title 1')\n            .fontSize(20)\n            .fontWeight(FontWeight.Bold)\n            .fontColor($r('app.color.title_text_color'))\n\n          Text('This is an enhanced description for Card 1. It has more padding and better styling.')\n            .fontSize(16)\n            .lineSpacing(LengthMetrics.vp(4))\n            .fontColor($r('app.color.description_text_color'))\n            .margin({ top: 8 })\n        }\n        .width('100%')\n        .padding(20)\n      }\n      .width('100%')\n      .margin({ bottom: 16 })\n      .backgroundColor($r('app.color.card_background_color'))\n      .borderRadius(12)\n      .shadow(8)\n      .borderWidth(1)\n      .borderColor($r('app.color.card_border_color'))",
            target_component_description="通过 Column 布局实现了一个自定义的卡片视图，使用 12vp 的圆角、8vp 的阴影高度 以及 1vp 的边框 来定义卡片的外观，边框和背景颜色可以通过资源文件设置。卡片内部包含两个文本元素，标题采用 20vp 的加粗字体，描述文字为 16vp，并通过 4vp 的行间距 增强可读性，同时设置了 8vp 的上边距。整个布局使用了 20vp 的内边距 和 16vp 的底部外边距，确保卡片在视觉上具有良好的层次感和适当的间距，适合用于展示简洁的标题和描述内容。",
            target_component_version="12"
        )

    async with SessionManager(config.db_config) as session:
        session.add(translation)
        await session.commit()
        result = await session.execute(select(TranslationTable))
        translations = result.scalars().all()
    print(translations)

async def main():
    await drop_db()
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
        session.add_all(translation_list)
        await session.commit()
        result = await session.execute(select(TranslationTable))
        translations = result.scalars().all()
    print(translations)


asyncio.run(main())
