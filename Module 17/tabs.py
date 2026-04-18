import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.header("Content for Tab 1")
    st.write("This si the content for the first tab.")

with tab2:
    st.header("Content for Tab 2")
    st.write("This si the content for the second tab.")

with tab3:
    st.header("Content for Tab 3")
    st.write("This si the content for the third tab.")