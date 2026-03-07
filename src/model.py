from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle

def create_model(new_df):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()

    similarity = cosine_similarity(vectors)

    # save files
    pickle.dump(new_df.to_dict(), open('movies_dict.pkl','wb'))
    pickle.dump(similarity, open('similarity.pkl','wb'))

    return similarity


# =========================
# RUN MODEL (IMPORTANT)
# =========================
if __name__ == "__main__":
    new_df = pd.read_csv('data/movies_tags.csv')
    create_model(new_df)
    print("Model created and files saved")