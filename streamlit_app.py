import streamlit as st

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar. You can add filters or navigation here.")


st.title("🎈 My Streamlit Deployment app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.set_page_config(
    page_title="Streamlit Deployment app",
    page_icon="rocket",
)

