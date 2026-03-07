import ast

def convert(text):
    return [i['name'] for i in ast.literal_eval(text)]

def convert_cast(text):
    L = []
    for i in ast.literal_eval(text)[:3]:  # cleaner way
        L.append(i['name'])
    return L

def fetch_director(text):
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            return [i['name']]
    return []

def transform_data(movies):
    movies = movies.copy()  

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert_cast)
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    # remove spaces
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ","") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ","") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ","") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ","") for i in x])

    # create tags
    movies['tags'] = movies['genres'] + movies['keywords'] + movies['overview'] + movies['cast'] + movies['crew']

    # create new dataframe safely
    new_df = movies[['id', 'title', 'tags']].copy()  # ✅ FIX

    new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
    new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

    return new_df