from transformers import pipeline

# lightweight instruction model (demo-safe)
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)


def generate_answer(prompt: str):
    result = generator(prompt)
    return result[0]["generated_text"]