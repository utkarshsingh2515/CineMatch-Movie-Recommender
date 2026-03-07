import pickle
import pandas as pd

# load data
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie = movie.lower()

    if movie not in movies['title'].str.lower().values:
        return ["Movie not found"]

    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommendations = []
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations