import os
from pytube import YouTube
from datetime import datetime
import streamlit as st

now = datetime.now()


def rename_file(out_file, file_ext):
    current_time = now.strftime("%Y%d%m_%H%M%S")
    base, ext = os.path.splitext(out_file)
    new_file = base + current_time + '.' + file_ext
    os.rename(out_file, new_file)

def download_360p_mp4_videos(url: str, file_format: str,outpath: str = "./"):
    yt = YouTube(url)
    if file_format == "music":
        print('music-------------------------------')
        out_file = yt.streams.filter(only_audio=True).first().download(outpath)
        rename_file(out_file, "mp3")
    else:
        print('video-------------------------------')
        out_file = yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
        rename_file(out_file, "mp4")
    return yt.title


st.title('My yt downloader')
st.subheader('this is my music and video downloader')
st.write('this app is awesome')



st.selectbox('Which file format?',('music', 'video'), key="file_format")
st.text_input('', key="url")

if st.button('Download'):
    url = st.session_state['url']
    file_format = st.session_state['file_format'].strip()

    st.write(file_format == 'music')

    if file_format == 'music':
        st.write('music')
        title = download_360p_mp4_videos(url,"mp3")
    else:
        st.write('video')
        title = download_360p_mp4_videos(url,"mp4")
    
    
    

