from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CANDIDATE_SYMPTOMS = [
    "headache",
    "nausea",
    "fatigue",
    "dizziness",
    "chest pain",
    "fever",
    "cough",
    "abdominal pain",
    "ear bleeding"
]

CANDIDATE_SYSTEMS = [
    "Neurological",
    "Gastrointestinal",
    "Respiratory",
    "Cardiovascular",
    "ENT",
    "General"
]


def extract_with_bert(text: str):

    symptom_result = classifier(
        text.lower(),
        CANDIDATE_SYMPTOMS,
        multi_label=True
    )

    symptoms = []
    flat_symptoms = []

    for label, score in zip(symptom_result["labels"], symptom_result["scores"]):
        if score > 0.25:
            symptoms.append({
                "name": label,
                "confidence": float(score)
            })
            flat_symptoms.append(label)

    # system classification
    system_result = classifier(
        text,
        CANDIDATE_SYSTEMS,
        multi_label=True
    )

    top_system = system_result["labels"][0]

    # severity
    severity = "low"
    t = text.lower()

    if any(x in t for x in ["bleeding", "severe", "unbearable"]):
        severity = "high"
    elif any(x in t for x in ["pain", "bad", "worse"]):
        severity = "medium"

    return {
        "symptoms": symptoms,              # structured (for physician)
        "symptom_list": flat_symptoms,     # safe (for UI)
        "body_system": top_system,
        "severity": severity
    }