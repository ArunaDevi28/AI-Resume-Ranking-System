from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def semantic_score(jd, resume):

    emb1 = model.encode([jd])

    emb2 = model.encode([resume])

    score = cosine_similarity(
        emb1,
        emb2
    )

    return float(score[0][0])
