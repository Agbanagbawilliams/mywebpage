from PIL import Image
import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("images/yt contact_form.png")
img_lottie_animation = Image.open("images/yt lotte_animation.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("HI I am Williams:wave:")
    st.title("MY WEBPAGE")

# ---- What I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do🤔")
        st.write("##")
        st.write("What i do is reading, programing, math, english, sports, and Traveling.")
        st.write("If you want to see my Scratch profile https://scratch.mit.edu/users/Williamsagb/")
        st.write("If you want to see my duolingo profile https://www.duolingo.com/profile/Williamsagba")
        st.write("If you want to see my github account https://github.com/Agbanagbawilliams/")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Integrating With Lottie files")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write('''
            Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun for programing, and Lottie Files are the easiest way to do!
                In this tutorial, It will show you exactly how to do it.
                ''')
        st.markdown("Watch Video https://www.youtube.com/watch?v=TXSOitGoINE")

# ---- CONNECT WITH ME ----
st.header("Connect with me📬")
st.write("""Connect with me on

Scratch😺https://scratch.mit.edu/

Duolingo🐦https://www.duolingo.com/

Github🐈‍⬛https://github.com/dashboard/
""")