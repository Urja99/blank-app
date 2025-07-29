import streamlit as st

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar. You can add filters or navigation here.")

# Main Title
st.title("Streamlit Layout Demo")
st.write("This app demonstrates Streamlit layouts, containers, and sidebar usage.")

# Columns
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content in the first column.")
    st.button("Button 1")
with col2:
    st.header("Column 2")
    st.write("Content in the second column.")
    st.button("Button 2")

# Expander
with st.expander("See more details"):
    st.write("This is inside an expander. You can hide or show this section.")

# Container
container = st.container()
with container:
    st.subheader("Container Section")
    st.write("This content is grouped inside a container.")
    st.slider("Example slider", 0, 100, 50)

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("This is Tab 1.")
with tab2:
    st.write("This is Tab 2.")

st.set_page_config(
    page_title="Streamlit Deployment App",
    page_icon="rocket",
)
