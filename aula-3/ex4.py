import json

documents = []
with open("books.json") as files:
    for file in files:
        documents.append(json.loads(file)["categories"])
print(documents[1])  # imprime o primeiro pokemon da documents