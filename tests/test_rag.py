import os
from uuid import uuid4

from core.config.config_loader import ConfigLoader
from core.prompt.prompt_loader import PromptLoader

from core.pilot.harmony.component import get_harmony_component

os.chdir("../")

ConfigLoader.from_file("./config.yaml")


def test_jina_code_embedding_model():
    from sentence_transformers import SentenceTransformer
    from sentence_transformers.util import cos_sim
    config = ConfigLoader.get_config()
    model = SentenceTransformer(
        config.rag_config.embedding.text.model,
        trust_remote_code=True
    )
    embeddings = model.encode([
        "使用Checkbox创建多选框",
        "// xxx.ets\n@Entry\n@Component\nstruct Index {\n\n  build() {\n    Row() {\n      Column() {\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个Checkbox组件，设置其宽度和高度\n          // 功能与效果描述：Checkbox组件用于用户选择或取消选择某个选项。设置宽度和高度以确保其显示效果。\n          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })\n            .width(30)\n            .height(30)\n          // 创建一个文本标签，设置其字体大小\n          // 功能与效果描述：文本标签用于标识Checkbox组件，设置字体大小以确保文本清晰可读。\n          Text('Checkbox1').fontSize(20)\n        }\n\n        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {\n          // 创建一个Checkbox组件，设置其宽度和高度\n          // 功能与效果描述：Checkbox组件用于用户选择或取消选择某个选项。设置宽度和高度以确保其显示效果。\n          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })\n            .width(30)\n            .height(30)\n          // 创建一个文本标签，设置其字体大小\n          // 功能与效果描述：文本标签用于标识Checkbox组件，设置字体大小以确保文本清晰可读。\n          Text('Checkbox2').fontSize(20)\n        }\n      }\n      .width('100%') // 设置Column的宽度为100%\n    }\n    .height('100%') // 设置Row的高度为100%\n  }\n}",
    ])
    print(embeddings.shape)
    print(cos_sim(embeddings[0], embeddings[1]))


def test_langchain_qdrant():
    from transformers import AutoTokenizer
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_qdrant import QdrantVectorStore
    from langchain_core.documents import Document
    from qdrant_client import QdrantClient
    from qdrant_client.http.models import Distance, VectorParams

    config = ConfigLoader.get_config()
    embedding_model_tokenizer = AutoTokenizer.from_pretrained(
        config.rag_config.embedding.text.model,
        use_fast=True
    )
    embedding_model = HuggingFaceEmbeddings(
        model_name=config.rag_config.embedding.text.model,
        model_kwargs={
            "trust_remote_code": True,
        }
    )
    embedding_model.client.max_seq_length = 4096

    vector_client = QdrantClient(":memory:")
    vector_client.create_collection(
        collection_name="test",
        vectors_config=VectorParams(size=768, distance=Distance.COSINE)
    )
    vector_store = QdrantVectorStore(
        client=vector_client,
        collection_name="test",
        embedding=embedding_model
    )
    documents = []
    components = get_harmony_component()
    max_length = 0
    for component_name, component_schema in components.items():
        component_examples = component_schema.examples
        if component_examples and len(component_examples) > 0:
            for example in component_examples:
                documents.append(Document(
                    page_content=example,
                    meta={"source": "component", "component_name": component_name}
                ))
                input_ids = embedding_model_tokenizer.encode(example)
                if len(input_ids) > max_length:
                    max_length = len(input_ids)
    uuids = [str(uuid4()) for _ in range(len(documents))]
    print(max_length)
    for i in range(0, len(documents), 10):
        end_index = i + 10 if i + 10 < len(documents) else len(documents)
        print(f"Adding documents from {i} to {end_index}")
        vector_store.add_documents(documents[i:end_index], ids=uuids[i:end_index])
    # 检索
    results = vector_store.similarity_search(
        query="如何使用Checkbox创建多选框"
    )
    print(results)


def test_component_example_document():
    components = get_harmony_component()
    examples = []
    for component_name, component_schema in components.items():
        component_examples = component_schema.examples
        if component_examples and len(component_examples) > 0:
            examples.extend(component_examples)
    print(examples)


def test_component_document():
    total_harmony_components = PromptLoader.get_prompt(
        "harmony/components.prompt",
        harmony_components=get_harmony_component(),
        is_component_content=True
    )
    print(total_harmony_components)