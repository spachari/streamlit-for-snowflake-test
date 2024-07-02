import streamlit as st
import datetime

@st.cache_data
def now():
    return datetime.datetime.now()


if st.button("Show Current time"):
    st.write(now())
    st.write(datetime.datetime.now())