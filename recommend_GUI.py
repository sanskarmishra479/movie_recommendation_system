import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2b947e99fe2972606102c316b1236ba1'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w185" + data['poster_path']

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distences = similarity[movie_index]
  movies_list = sorted(list(enumerate(distences)),reverse=True,key= lambda x:x[1])[1:6]

  recommended_movies = []
  recommended_movies_posters = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    #extract poster
    recommended_movies_posters.append(fetch_posters(movie_id))
  return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
    'Enter The Movie Name',movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2 ,col3,col4,col5 = st.columns(5,gap="large")
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])