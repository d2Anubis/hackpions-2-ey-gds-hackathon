import streamlit as st
from views.query import query
from views.tags import tag

st.set_page_config(layout="wide")

st.sidebar.markdown(
    "Welcome to **NLP + Fuzzy Logic powered Exception Tagger**")

add_selectbox = st.sidebar.selectbox(
    "Select an action",
    ("Query", "Update Tags")
)

if add_selectbox == "Query":
    query()
elif add_selectbox == "Update Tags":
    tag()
else:
    pass
