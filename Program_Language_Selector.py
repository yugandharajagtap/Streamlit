import streamlit as st

st.title("Programming Language")
st.subheader("Your program languages is here")
st.text("Welcome Here")

lang = st.selectbox("Your Fav Language.",["JAVA" , "Python","HTML","CSS"])
st.write(f"You choose {lang}. Good Choice")
st.success("Your choose your fav Language ")