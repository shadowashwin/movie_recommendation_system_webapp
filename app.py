import streamlit as st
import pickle
import pandas as pd
import requests

# page_bg = """
# <style>
# [data-testid="stMarkdownContainer"]{
# background-image: url("https://wallpaperaccess.com/full/499.jpg");
# background-size: cover;
# }
# </style>
# """
#
# st.markdown(page_bg, unsafe_allow_html=True)


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=f0ce014c50b11771debefe558168b1f7&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']  # complete image path


def similar_movies(movie):
    index = movies[movies['title'] == movie].index[0]
    m_d = similarity[index]
    m_l = sorted(list(enumerate(m_d)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []
    for i in m_l:
        movie_id = movies.iloc[i[0]].movie_id  # fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


similarity = pickle.load(open('similarity.pkl', 'rb'))

m_ll = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(m_ll)

# web page
st.title('Movie Recommendation System')

option = st.selectbox(
    'Select the movie to be recommended',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = similar_movies(option)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

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

    with col6:
        st.text(names[5])
        st.image(posters[5])

    with col7:
        st.text(names[6])
        st.image(posters[6])

    with col8:
        st.text(names[7])
        st.image(posters[7])

    with col9:
        st.text(names[8])
        st.image(posters[8])

    with col10:
        st.text(names[9])
        st.image(posters[9])

    # for i in range(10) :
    #     col = st.columns(1)
    #     with col:
    #         st.header(names[i])
    #         st.image(posters[i])

# what all i have used
# https://www.themoviedb.org/settings/api   # api key
# https://developers.themoviedb.org/3/movies/get-movie-details    # getting movie details
# https://api.themoviedb.org/3/movie/65?api_key=f0ce014c50b11771debefe558168b1f7&language=en-US    # pasting the above details with api key and movie_id
# => jason
# {"adult":false,"backdrop_path":"/bfccQmQWNFQYRv4PHgCnjDu7PXn.jpg","belongs_to_collection":null,"budget":41000000,"genres":[{"id":10402,"name":"Music"},{"id":18,"name":"Drama"}],"homepage":"https://www.uphe.com/movies/8-mile","id":65,"imdb_id":"tt0298203","original_language":"en","original_title":"8 Mile","overview":"For Jimmy Smith, Jr., life is a daily fight just to keep hope alive. Feeding his dreams in Detroit's vibrant music scene, Jimmy wages an extraordinary personal struggle to find his own voice - and earn a place in a world where rhymes rule, legends are born and every moment… is another chance.","popularity":49.625,"poster_path":"/7BmQj8qE1FLuLTf7Xjf9sdIHzoa.jpg","production_companies":[{"id":23,"logo_path":"/mkxNjThahj5pvntvYKVpMbWXm3D.png","name":"Imagine Entertainment","origin_country":"US"},{"id":24,"logo_path":null,"name":"Mikona Productions GmbH & Co. KG","origin_country":"DE"}],"production_countries":[{"iso_3166_1":"DE","name":"Germany"},{"iso_3166_1":"US","name":"United States of America"}],"release_date":"2002-11-08","revenue":242875078,"runtime":111,"spoken_languages":[{"english_name":"English","iso_639_1":"en","name":"English"}],"status":"Released","tagline":"Every Moment Is Another Chance","title":"8 Mile","video":false,"vote_average":7.115,"vote_count":6212}
# jason viewer
# => http://jsonviewer.stack.hu/#http://
