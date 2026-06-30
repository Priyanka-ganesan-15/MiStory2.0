from app.services.medical_bert import extract_with_bert

def extract_symptoms(text: str):
    """
    Unified extraction layer.
    Later we can switch models without touching API layer.
    """

    return extract_with_bert(text)