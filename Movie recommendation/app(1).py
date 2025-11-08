import streamlit as st
import pickle as pkl
import pandas as pd

movies = pkl.load(open('movies.pkl', 'rb'))
movies_listed = movies['names'].values
similarity = pkl.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[ movies['names'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].names)
    return recommended_movies

st.title("Movie recommendation system")

selected_movie = st.selectbox(
    'Choose your movie',
    movies_listed
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)

