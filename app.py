import streamlit
from PIL import Image
import streamlit as st

# Nav bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #E50900">
  <a class="navbar-brand" target="_blank">Multi app</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
     <li class="nav-item active">
        <a class="nav-link" href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/" target="_blank">Home</a>
      <li class="nav-item active">
        <a class="nav-link" href="https://agbanagbawilliams-mywebpage-app-vqxbm4.streamlit.app/" target="_blank">Project</a>
      <li class="nav-item">
        <a class="nav-link" href="https://blank-app-quobxypwoytpuhz3cchas6.streamlit.app/" target="_blank">Chatbot</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

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
        st.write(" If you want to see my Scratch profile https://scratch.mit.edu/users/Williamsagb/")
        st.write(" If you see my duolingo profile https://www.duolingo.com/profile/Williamsagba")
        st.write(" If you want to see my github account https://github.com/Agbanagbawilliams/")
        st.write("If you love my webpage please buy this to support me https://buy.stripe.com/test_cN215l5qb13B2aY8wz")

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
st.header("Follow me📬")
st.write("""Follow me on

Scratch😺https://scratch.mit.edu/

Duolingo🐦https://www.duolingo.com/

Github🐈‍⬛https://github.com/dashboard/
""")
