import streamlit as st

# Set up the page
st.set_page_config(page_title="Basic app")

# Display title and button
st.title("Basic app")
if st.button("Click me"):
    st.write("Clicked")

# Display markdown text
st.markdown("Hello world")
