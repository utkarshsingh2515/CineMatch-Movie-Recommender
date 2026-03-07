import streamlit as st
import requests
from src.recommend import recommend

API_KEY = "4857c335"

st.set_page_config(page_title="CineMatch", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.stImage img{
    border-radius:12px;
    transition: transform .3s ease;
}

.stImage img:hover{
    transform: scale(1.08);
}

.movie-title{
    text-align:center;
    font-weight:bold;
    font-size:16px;
    margin-top:6px;
}

.rating{
    text-align:center;
    color:gold;
    font-size:14px;
}

.details{
    background:#1c1c1c;
    padding:12px;
    border-radius:10px;
    color:white;
}

</style>
""", unsafe_allow_html=True)


# ---------- Fetch Movie ----------
def fetch_movie(title):

    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    data = requests.get(url).json()

    if data["Response"] == "True":

        poster = data["Poster"]
        rating = data["imdbRating"]
        year = data["Year"]
        plot = data["Plot"]

        if poster == "N/A":
            poster = "https://via.placeholder.com/300x450?text=No+Poster"

        return poster, rating, year, plot

    return "https://via.placeholder.com/300x450", "N/A", "", "No description available"


# ---------- Display Movies ----------
def display_movies(movie_list):

    cols = st.columns(5)

    for i, movie in enumerate(movie_list):

        poster, rating, year, plot = fetch_movie(movie)

        with cols[i % 5]:

            st.image(poster)

            st.markdown(
                f"<div class='movie-title'>{movie}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='rating'>⭐ {rating} | {year}</div>",
                unsafe_allow_html=True
            )

            if st.button("Details", key=f"{movie}_{i}"):

                st.markdown(
                    f"""
                    <div class="details">
                    <b>{movie}</b><br><br>
                    ⭐ Rating: {rating}<br>
                    📅 Year: {year}<br><br>
                    {plot}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ---------- Title ----------
st.title("🎬 CineMatch – Movie Recommender")


# ---------- Search ----------
movie_name = st.text_input("Search Movie")

recommend_clicked = st.button("Recommend")


# ---------- Homepage Movie Sections ----------
trending_movies = [
"Avatar","Avengers","Inception","Interstellar","Joker",
"The Dark Knight","Titanic","Gladiator"
]

top_rated = [
"The Shawshank Redemption",
"The Godfather",
"The Dark Knight",
"Forrest Gump",
"Fight Club",
"Pulp Fiction"
]

popular_classics = [
"Jurassic Park",
"The Matrix",
"Back to the Future",
"Terminator 2",
"Indiana Jones",
"Star Wars"
]


# ---------- Show Recommendations ----------
if recommend_clicked and movie_name != "":

    st.subheader("🎯 Recommended Movies")

    results = recommend(movie_name)

    display_movies(results)


# ---------- Homepage ----------
else:

    st.subheader("🔥 Trending Movies")
    display_movies(trending_movies)

    st.markdown("---")

    st.subheader("⭐ Top Rated Movies")
    display_movies(top_rated)

    st.markdown("---")

    st.subheader("🎬 Popular Classics")
    display_movies(popular_classics)