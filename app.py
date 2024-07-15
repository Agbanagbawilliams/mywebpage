from PIL import Image
import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("images/yt contact_form.png")
img_lottie_animation = Image.open("images/yt lotte_animation.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("HI I am Williams👋")
    st.title("MY WEBPAGE")

# ---- What I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do🤔")
        st.write("##")
        st.write("What i do is reading, programing, math, english, sports, and Traveling.")
        st.write("You see my Scratch profile over here: https://scratch.mit.edu/users/Williamsagb/")
        st.write("You see my duolingo profile over here: https://www.duolingo.com/profile/Williamsagba")
        st.write("You see my github account over here: https://github.com/Agbanagbawilliams/")
        st.write("You can buy a cup over over here: https://buy.stripe.com/test_fZe15lcSD4fN7vi3cc please buy🥺.")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Learning scratch")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Learning how to code on scratch.")
        st.write("""
            Learn how to code in scratch!
                Coding in scratch is fun!
                You use tools to programme which is easy then programming language because you type 
                and in scratch you use tools/blocks👍.
                """)

        st.subheader("Using scratch tutorials")
        st.write("Scratch tutorials helps you to use and understand Scratch😉.")
        st.markdown("Tutorials https://scratch.mit.edu/projects/1046994874/editor")

# ---- CONNECT WITH ME ----
st.header("Connect with me📬")
st.write("""Connect with me on

Scratch😺https://scratch.mit.edu/

Duolingo🐦https://www.duolingo.com/

Github🐈‍⬛https://github.com/dashboard/
""")
