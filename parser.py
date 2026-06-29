import pdfplumber

def parse_resume(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted

    common_skills = [
        "python",
        "machine learning",
        "deep learning",
        "nlp",
        "sql",
        "java",
        "tensorflow",
        "pytorch",
        "aws",
        "docker",
        "kubernetes",
        "data science"
    ]

    skills = []

    lower_text = text.lower()

    for skill in common_skills:

        if skill in lower_text:

            skills.append(skill)

    return {
        "skills": skills,
        "text": text
    }
