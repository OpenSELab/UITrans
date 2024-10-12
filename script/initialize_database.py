import os
import json
import asyncio

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from sqlalchemy import select, delete

from core.db.model.base import Base
from core.db.model.harmony import HarmonyComponentExample
from core.db.model.translation import TranslationTable
from core.config.config_loader import ConfigLoader
from core.db.session import SessionManager
from core.llms import LLMFactory
from core.pilot.harmony.component import get_harmony_component

os.chdir("../")

config = ConfigLoader.from_file("./config.yaml")
llm_client = LLMFactory.create_llm_from_config(llm_client_type="openai",
                                               llm_config=config.llm_config["openai"].dict())
db_client = Chroma(
    collection_name="harmony-component-doc",
    persist_directory=config.rag_config.persist_directory,
    embedding_function=HuggingFaceEmbeddings(
        model_name=config.rag_config.embedding.text.model,
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True},
    ),
    collection_metadata={
        "hnsw:M": 64,  # 增大图结构中节点的最大连接数，避免图结构过于稀疏，无法生成高质量的邻居搜索结果。默认值为：16
        "hnsw:construction_ef": 200,  # 控制图结构的质量，值越大，图结构质量越高，但搜索速度越慢。默认值为：100
        "hnsw:space": "cosine",  # 距离度量方式使用余弦相似度，可选值为：cosine、l2、ip。默认值为：l2
    }
)


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


async def init_translation_table():
    # 清空表
    async with SessionManager(config.db_config) as session:
        await session.execute(delete(TranslationTable))
        await session.commit()
    with open("script/initialize_database/component_table.json", "r", encoding="utf-8") as f:
        translations = json.loads(f.read())
    translation_list = []
    for translation in translations:
        translation_list.append(TranslationTable(
            source_language=translation["source_language"],
            source_component=translation["source_component"],
            source_component_code=translation["source_component_code"].strip(),
            source_component_description=translation["source_component_description"].strip(),
            source_component_version=translation["source_component_version"],
            target_language=translation["target_language"],
            target_component=translation["target_component"],
            target_component_code=translation["target_component_code"],
            target_component_description=translation["target_component_description"],
            target_component_version=translation["target_component_version"],
            disabled=False
        ))
    async with SessionManager(config.db_config) as session:
        session.add_all(translation_list)
        await session.commit()


def init_component_rag_database():
    """初始化RAG组件文档库

    从Harmony组件库中获取组件信息，生成文档并存入知识库

    **IMPORTANT**: 目前未存储类型文档
    """
    harmony_components = get_harmony_component()

    documents = []
    for component_name, component_schema in harmony_components.items():
        documents.append(Document(
            page_content=f"""组件名：{component_name}
组件描述：{component_schema.description}
""",
            metadata={"source": "harmony-component-doc"
                                "t-doc", "component_name": component_name, "type": "component"},
        ))
        for attribute_name, attribute_schema in component_schema.attributes.items():
            documents.append(Document(
                page_content=f"""{attribute_schema.description}
属性名称：{attribute_name}
属性参数：{attribute_schema.params}
""",
                metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "attribute",
                          "name": attribute_name},
            ))
        for event_name, event_schema in component_schema.events.items():
            documents.append(Document(
                page_content=f"""{event_schema.description}
事件名称：{event_name}
事件参数：{event_schema.params}
事件返回值：{event_schema.returns}
""",
                metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "event",
                          "name": event_name},
            ))
    #     related_types = get_component_related_types(component_name)
    #     for type_name, type_schema in related_types.items():
    #         if type_schema.type == "object":
    #             document = Document(
    #                 page_content=f"""类型名：{type_name}
    # 类型描述：{type_schema.description}
    # 参数：{type_schema.properties}
    #                         """,
    #                 metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "type",
    #                           "name": type_name},
    #             )
    #         elif type_schema.type == "enum":
    #             # 枚举值介绍
    #             all_enum_description = ""
    #             for enum_value, enum_description in type_schema.enumDescriptions.items():
    #                 all_enum_description += f"* {enum_value}: {enum_description}\n"
    #             document = Document(
    #                 page_content=f"""枚举类型名：{type_name}
    # 枚举类型描述：{type_schema.description}
    # 枚举值：{type_schema.enum}
    # 枚举值描述：
    # {all_enum_description}
    #                         """,
    #                 metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "enum",
    #                           "name": type_name},
    #             )
    #         else:
    #             # 普通类型
    #             document = Document(
    #                 page_content=f"""类型名：{type_name}
    # 类型描述：{type_schema.description}
    # 类型：{type_schema.type}
    #                         """,
    #                 metadata={"source": "harmony-component-doc", "component_name": component_name, "type": "type",
    #                           "name": type_name},
    #             )
    #         documents.append(document)
    #         if type_schema.examples:
    #             for example in type_schema.examples:
    #                 documents.append(Document(
    #                     page_content=f"""类型{type_name}示例：
    # {example}
    # """,
    #                     metadata={"source": "harmony-component-doc", "component_name": component_name,
    #                               "type": "example", "name": type_name},
    #                 ))

    db_client.add_documents(documents)


async def init_component_examples():
    """初始化组件示例库

    从Harmony组件库中获取组件使用示例，存入数据库以及知识库
    """

    # 清空表
    # async with SessionManager(config.db_config) as session:
    #     await session.execute(delete(HarmonyComponentExample))
    #     await session.commit()

    async def add_example(component_example_code, component_example_description) -> Document:
        component_example_entity = HarmonyComponentExample(
            api_version="12",
            component_name=component_name,
            description=component_example_description,
            code=component_example_code
        )
        async with SessionManager(config.db_config) as session:
            session.add(component_example_entity)
            await session.commit()
        return Document(
            page_content=component_example_description,
            metadata={"source": "harmony-component-example-doc", "component_name": component_name,
                      "table_id": component_example_entity.id},
        )

    documents = []
    with open("script/initialize_database/components.json", "r", encoding="utf-8") as f:
        harmony_components = json.loads(f.read())

    # for component_name, component_schema in harmony_components.items():
    #     if "examples" in component_schema and component_schema["examples"]:
    #         for example in component_schema["examples"]:
    #             if not isinstance(example, dict):
    #                 print(f"组件{component_name}示例格式错误")
    #                 continue
    #             component_example_description = example["description"]
    #             component_example_code = example["code"]
    #             documents.append(await add_example(component_example_code, component_example_description))
    #     else:
    #         print(f"组件{component_name}没有不存在示例")
    from component_examples import examples
    for component_name, component_examples in examples.items():
        for example in component_examples:
            documents.append(await add_example(example["code"], example["description"]))
    db_client.add_documents(documents)


async def main():
    # await drop_db()
    await init_db()
    # 初始化转译表
    await init_translation_table()
    # 初始化组件示例库
    init_component_rag_database()
    # 初始化示例库
    await init_component_examples()


asyncio.run(init_component_examples())
