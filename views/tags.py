import streamlit as st
from main import Update_tags


def tag():
    with st.form("my_form"):
        # exception input
        st.write("**Enter Tags to store in lookup database**",
                 value='', key='text')
        error = st.text_input("", value='', key='error')
        tag = st.selectbox("Select Tag type", options=[
                           'Business Exception', 'System Exception'], key="tag")
        submitted1 = st.form_submit_button("Submit")

        if submitted1:
            # call Classify here
            print(tag)
            print()
            b = Update_tags(error=error, tag=tag)
            b.update()
