from fastapi import FastAPI, Form
from elasticsearch import Elasticsearch

app = FastAPI()

es = Elasticsearch(hosts=["http://elasticsearch:9200"])

index_name = "india"

if not es.indices.exists(index=index_name):
    es.indices.create(
        index=index_name,
        body={
            "mappings": {
                "properties": {"id": {"type": "keyword"}, "text": {"type": "text"}}
            }
        },
    )

    docs = [
        {
            "id": "1",
            "text": "India is a country in South Asia. It is the seventh-largest country by land area, the most populous country, and the most populous democracy in the world.",
        },
        {
            "id": "2",
            "text": "Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east.",
        },
        {
            "id": "3",
            "text": "In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.",
        },
        {
            "id": "4",
            "text": "Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago. Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.",
        },
    ]

    for doc in docs:
        es.index(index=index_name, id=doc["id"], document=doc)


@app.post("/get")
async def get_best_document(query: str = Form(...)):
    response = es.search(index=index_name, body={"query": {"match": {"text": query}}})
    if response["hits"]["hits"]:
        best_doc = response["hits"]["hits"][0]["_source"]["text"]
        return {"result": best_doc}
    else:
        return {"result": "No matching document found."}


@app.post("/insert")
async def insert_document(document: str = Form(...)):
    es.index(index=index_name, document={"text": document})
    return {"message": "Document Inserted"}
