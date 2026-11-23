
from src.knowledge_base import load_knowledge_base
from src.retriever import KnowledgeRetriever


knowledge = load_knowledge_base()
retriever = KnowledgeRetriever(knowledge)

questions = [
    "Does Cynbit provide AI automation?",
    "Tell me about Cynbit's software development services.",
    "What products does Cynbit offer?",
    "How can I submit a project inquiry?"
]

for question in questions:
    print("\nQuestion:", question)

    results = retriever.search(question, top_k=2)

    for result in results:
        print("Title:", result["title"])
        print("Similarity:", result["score"])
        print("Information:", result["content"])
