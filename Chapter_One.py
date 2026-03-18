'''
Streamlit is a simple Python framework 
that lets you turn your Python scripts 
into interactive web apps—without needing
HTML, CSS, or JavaScript.

'''

import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with stremlit")
st.text("welcome to your first interactive app")
st.write("choose your fav. variety of chai")

chai = st.selectbox("Your fav chai:",["Masala chai","Lemon Tea",
                                      "Adrak Chai","kesar chai"])
st.write(f"Your choose {chai} . Excellent Choice")

st.success("Your Chai has been Brewed")

