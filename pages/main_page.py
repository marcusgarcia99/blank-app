import streamlit as st

st.markdown("# Intrusive Thoughts 🎈")


with st.sidebar:
    st.sidebar.markdown("# Well Thought Out Thoughts 🎈")
    st.write("Chick-Fil-A should be open on Sundays cuz thats when I crave it. Do you agree?")
    st.radio("Pick one", ["Agreed", "You need therapy."])