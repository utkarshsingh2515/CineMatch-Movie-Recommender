import pandas as pd
from feature_engineering import transform_data

def load_and_merge_data():
    # Load datasets
    movies = pd.read_csv('data/tmdb_5000_movies.csv')
    credits = pd.read_csv('data/tmdb_5000_credits.csv')

    # Merge on title
    movies = movies.merge(credits, on='title')

    # Select useful columns
    movies = movies[['genres','id','keywords','overview','title','cast','crew']]

    # Remove missing values
    movies.dropna(inplace=True)

    return movies


if __name__ == "__main__":
    print("Loading and merging data...")
    movies = load_and_merge_data()

    print("Transforming data (creating tags)...")
    new_df = transform_data(movies)

    # Save processed file
    new_df.to_csv('data/movies_tags.csv', index=False)

    print("movies_tags.csv created successfully in /data folder!")