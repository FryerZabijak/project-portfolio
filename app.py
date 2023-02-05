import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Pepa Mráz | Portfolio Projektů", page_icon=":blue_book:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- ASSETS ---
lottie_developer = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")


# --- HEADER SECTION ---

with st.container():
        st.subheader("Ahoj, jmenuji se Pepa :wave:")
        st.title("Website Developer z Ostravy")
        st.write("Rád tvořím kreativní webové aplikace s různými technologiemi")
        st.write("[Více o mně >](https://pepamraz.cz)")

# --- V ČEM TVOŘÍM ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("V čem tvořím")
        st.write("##")
        st.write("""
                 Mezi technologie, které rád používám patří:
                 - React.js, Svelte pro frontend
                 - Python, Express.js a PHP pro backend
                 - MYSQL a MongoDB pro práci s databázemi
                 - CSS si buď píši sám, nebo v poslední době jsem si oblíbil Tailwind CSS a Bootstrap
                 """)
        st.write("[Můj Github >](https://github.com/fryerzabijak)")
    with right_column:
        st_lottie(lottie_developer)
        
def Project(title, emoji, image, description, link_url):
    project_img = Image.open(image)
    
    with st.container():
        st.subheader(f"{title} {emoji}")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image(project_img)
        with right_column:
            st.write(description)
            st.write(f"[Projekt >]({link_url})")
        st.write("#")
        

# --- PROJEKTY ---
with st.container():
    st.write("---")
    st.header("Mé Projekty")
    
    Project("Flask Blog s administrací",":notebook:","img/flask-blog.jpg","""
            Technologie použity:
            - Python
            - Flask
            - SQLAlchemy
            - Jinja
            - Tailwind CSS
            """, "https://github.com/FryerZabijak/flask-blog")
    Project("Mafia Game",":dollar:","img/mafia-game.jpg","""
            Technologie použity:
            - JavaScript
            - CSS
            - PHP
            - HTML
            - MySQL
            """, "https://mafiagame.space")
    Project("C# Chválící aplikace s administrací",":iphone:","img/chvalici-aplikace.jpg","""
            Technologie použity:
            - C#
            - .NET Framework
            - WPF
            """, "https://github.com/FryerZabijak/chvalici-appka")
    Project("Oběšenec v Bashi",":skull:","img/obesenec-v-bashi.jpg","""
            Technologie použity:
            - Linux Shell
            """, "https://github.com/FryerZabijak/obesenec-v-shellu")
    contact_form = """
             <form action="https://formsubmit.co/8c3c9237d0e4a1bcb981b9d01ae7aa65" method="POST">
                <input type="text" name="name" placeholder="Jméno" required>
                <input type="email" name="email" placeholder="E-mail" required>
                <button type="submit">Odeslat</button>
            </form> 
                """
    col1, col2, col3 = st.columns((1,3,1))
    with col1:
        st.write(" ")
    with col2:
        st.header("Kontaktujte mě")
        st.markdown(contact_form, unsafe_allow_html=True)
    with col3:
        st.write(" ")
    
# Použít Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")