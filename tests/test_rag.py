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


def test_chromadb():
    import chromadb
    from chromadb.utils.embedding_functions.sentence_transformer_embedding_function import \
        SentenceTransformerEmbeddingFunction
    from transformers import AutoTokenizer
    from sentence_transformers import SentenceTransformer

    config = ConfigLoader.get_config()
    embedding_model_tokenizer = AutoTokenizer.from_pretrained(
        config.rag_config.embedding.text.model,
        use_fast=True
    )
    embedding_model = SentenceTransformerEmbeddingFunction(
        model_name_or_path=config.rag_config.embedding.text.model,
        trust_remote_code=True
    )
    embedding_model.max_seq_length = 4096
    db_client = chromadb.PersistentClient("tmp/chromadb")
    db_collection = db_client.create_collection(
        name="test",
        embedding_function=embedding_model,
        get_or_create=True
    )


def test_qdrant():
    from transformers import AutoTokenizer
    from sentence_transformers import SentenceTransformer
    from qdrant_client import QdrantClient
    from qdrant_client.http.models import Distance, VectorParams

    config = ConfigLoader.get_config()
    embedding_model_tokenizer = AutoTokenizer.from_pretrained(
        config.rag_config.embedding.text.model,
        use_fast=True
    )
    embedding_model = SentenceTransformer(
        model_name_or_path=config.rag_config.embedding.text.model,
        trust_remote_code=True
    )
    print(embedding_model)
    return
    embedding_model.max_seq_length = 4096
    vector_client = QdrantClient(path="tmp/langchain_qdrant")
    # TODO：创建或获取集合
    vector_client.get_collection(
        collection_name="test",
        # vectors_config=VectorParams(size=768, distance=Distance.COSINE)
    )
    results = vector_client.query(
        collection_name="test",
        query_text="如何使用Button类型的Toggle",
    )
    print(results)


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

    vector_client = QdrantClient(path="tmp/langchain_qdrant")
    # TODO：创建或获取集合
    vector_client.get_collection(
        collection_name="test",
        # vectors_config=VectorParams(size=768, distance=Distance.COSINE)
    )
    vector_store = QdrantVectorStore(
        client=vector_client,
        collection_name="test",
        embedding=embedding_model
    )
    # documents = []
    # components = get_harmony_component()
    # for component_name, component_schema in components.items():
    #     component_examples = component_schema.examples
    #     if component_examples and len(component_examples) > 0:
    #         for example in component_examples:
    #             documents.append(Document(
    #                 page_content=example,
    #                 metadata={"source": "component", "component_name": component_name}
    #             ))
    # uuids = [str(uuid4()) for _ in range(len(documents))]
    # for i in range(0, len(documents), 10):
    #     end_index = i + 10 if i + 10 < len(documents) else len(documents)
    #     print(f"Adding documents from {i} to {end_index}")
    #     vector_store.add_documents(documents[i:end_index], ids=uuids[i:end_index])
    # 检索
    results = vector_store.similarity_search_with_score(
        query="如何使用Button类型的Toggle", k=5, score_threshold=0.5
    )
    for result, score in results:
        print(f"--- {score} ---")
        print(result)
        print(f"--- {score} ---")


def test_rerank():
    from sentence_transformers import CrossEncoder

    config = ConfigLoader.get_config()
    model = CrossEncoder(
        config.rag_config.embedding.rerank.model,
        device="cpu",
        automodel_args={"torch_dtype": "auto"},
        trust_remote_code=True,
    )

    # Example query and documents
    query = "Organic skincare products for sensitive skin"
    documents = [
        "Organic skincare for sensitive skin with aloe vera and chamomile.",
        "New makeup trends focus on bold colors and innovative techniques",
        "Bio-Hautpflege für empfindliche Haut mit Aloe Vera und Kamille",
        "Neue Make-up-Trends setzen auf kräftige Farben und innovative Techniken",
        "Cuidado de la piel orgánico para piel sensible con aloe vera y manzanilla",
        "Las nuevas tendencias de maquillaje se centran en colores vivos y técnicas innovadoras",
        "针对敏感肌专门设计的天然有机护肤产品",
        "新的化妆趋势注重鲜艳的颜色和创新的技巧",
        "敏感肌のために特別に設計された天然有機スキンケア製品",
        "新しいメイクのトレンドは鮮やかな色と革新的な技術に焦点を当てています",
    ]

    # construct sentence pairs
    sentence_pairs = [[query, doc] for doc in documents]

    scores = model.predict(sentence_pairs, convert_to_tensor=True).tolist()
    """
    [0.828125, 0.0927734375, 0.6328125, 0.08251953125, 0.76171875, 0.099609375, 0.92578125, 0.058349609375, 0.84375, 0.111328125]
    """

    rankings = model.rank(query, documents, return_documents=True, convert_to_tensor=True)
    print(f"Query: {query}")
    for ranking in rankings:
        print(f"ID: {ranking['corpus_id']}, Score: {ranking['score']:.4f}, Text: {ranking['text']}")
    """
    Query: Organic skincare products for sensitive skin
    ID: 6, Score: 0.9258, Text: 针对敏感肌专门设计的天然有机护肤产品
    ID: 8, Score: 0.8438, Text: 敏感肌のために特別に設計された天然有機スキンケア製品
    ID: 0, Score: 0.8281, Text: Organic skincare for sensitive skin with aloe vera and chamomile.
    ID: 4, Score: 0.7617, Text: Cuidado de la piel orgánico para piel sensible con aloe vera y manzanilla
    ID: 2, Score: 0.6328, Text: Bio-Hautpflege für empfindliche Haut mit Aloe Vera und Kamille
    ID: 9, Score: 0.1113, Text: 新しいメイクのトレンドは鮮やかな色と革新的な技術に焦点を当てています
    ID: 5, Score: 0.0996, Text: Las nuevas tendencias de maquillaje se centran en colores vivos y técnicas innovadoras
    ID: 1, Score: 0.0928, Text: New makeup trends focus on bold colors and innovative techniques
    ID: 3, Score: 0.0825, Text: Neue Make-up-Trends setzen auf kräftige Farben und innovative Techniken
    ID: 7, Score: 0.0583, Text: 新的化妆趋势注重鲜艳的颜色和创新的技巧
    """


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
