import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(jd_text):

    doc = nlp(jd_text)

    skills = []

    for token in doc:

        if token.pos_ in ["NOUN", "PROPN"]:

            skills.append(
                token.text.lower()
            )

    return list(set(skills))
