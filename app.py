import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "0876ae843ecf4d8799a6c4fec32ec77c"
CLIENT_SECRET = "6cba082776304d7ca1fa55f880ced976"

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get song album cover
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_music_names = []
    recommend_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist # fetch the movie poster
        print(artist)
        print(music.iloc[i[0]].song)
        recommend_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommend_music_names.append(music.iloc[i[0]].song)

    return recommend_music_names, recommend_music_posters


st.header('Music Recommender System')
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommend_music_names, recommend_music_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_music_names[0])
        st.image(recommend_music_posters[0])
    with col2:
        st.text(recommend_music_names[1])
        st.image(recommend_music_posters[1])

    with col3:
        st.text(recommend_music_names[2])
        st.image(recommend_music_posters[2])
    with col4:
        st.text(recommend_music_names[3])
        st.image(recommend_music_posters[3])
    with col5:
        st.text(recommend_music_names[4])
        st.image(recommend_music_posters[4])