import streamlit as st
from streamlit import server

server.enableWebsocketCompression=False
server.enableXsrfProtection=False

_,_,col3,_,_ = st.columns(5)
with col3:
    st.image('tiss.jpg')

st.markdown("<h1 style='text-align: center;'> Welcome to Casablanca! 🍻 </h1>", unsafe_allow_html=True)
st.markdown("")
st.markdown("<h3> casablanca is a web application provided by the TISS data team to present ideas to stakeholders. \
            enjoy it. </h3>", unsafe_allow_html=True)
st.markdown("")

video_file = open('casablanca.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

