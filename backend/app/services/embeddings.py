from sentence_transformers import SentenceTransformer

# lightweight + fast + free
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    return model.encode(text).tolist()