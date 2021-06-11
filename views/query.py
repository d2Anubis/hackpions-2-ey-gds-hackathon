from numpy.lib.npyio import save
import streamlit as st
from main import Classify
import pandas as pd

df = pd.read_excel("./data/exceptions.xlsx")
_l = None


def find(error, save):
    global _l
    a = Classify(error)
    finder = a.match_from_database()

    if save:
        print("Saving to database")
        a.update_to_database()

    if type(finder) == dict:
        _l = None
        return ('only tag', finder['tag'])
    elif finder[0] == "Error exists at index" and type(finder[1]) == int:
        _l = 1
        return ('direct', finder[1])
    elif type(finder[1]) == list:
        finder = [first for first, second in sorted(
            finder[1], key=lambda x: x[1], reverse=True)[:5]]
        _l = len(finder)
        return ("Fuzzy or Bert match", finder)
    else:
        pass


def query():
    global _l
    with st.form("my_form"):
        # exception input
        st.write("**Enter Exception to classify....**",
                 value='', key='exception')
        err = st.text_input("", value='', key='exception')

        col1, col2 = st.beta_columns(2)

        with col1:
            # submit button
            submitted1 = st.form_submit_button("Search")

        with col2:
            # save to database ?
            save_to_database = st.checkbox("Save to Database ?")

    st.markdown("<hr/>", unsafe_allow_html=True)

    if submitted1:
        f = find(err, save_to_database)

        if _l != None:

            # direct match exception details
            if _l == 1 and (f[0] == "direct" or f[0] == "fuzzy match"):
                with st.form("temp"):
                    st.markdown("**ID : " + str(df.loc[f[1], 'ID'])+" **")
                    st.markdown(df.loc[f[1], 'Exception'])
                    searcher = st.form_submit_button(
                        df.loc[f[1], 'Category'])

            # match using fuzzy details
            else:
                for i in f[1]:
                    # submit button
                    with st.form(str(i)):
                        st.markdown("**ID : " + str(df.loc[i, 'ID'])+" **")
                        st.markdown(df.loc[i, 'Exception'])
                        searcher = st.form_submit_button(
                            df.loc[i, 'Category'])

        elif f[0] == "only tag":
            st.info("Direct match from look up table : **"+str(f[1])+"**")
