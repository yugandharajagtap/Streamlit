import streamlit as st

st.title("Chai Taste Poll")

col1 , col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/905485/pexels-photo-905485.jpeg",width=200 )
    vote1 = st.button("Vote Masala chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/1034044/pexels-photo-1034044.jpeg", width =200)
    vote2 = st.button("Vote Adrak chai")

if vote1:
    st.success("Thanks for voting Masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")

name = st.sidebar.text_input("Enter Your Name")
tea = st.sidebar.selectbox("Choose your chai",["Masala","Adrak","kesar"])

st.write(f"Welcome {name} ! your {tea} Chai is getting ready")

with st.expander("Show chai making instructions"):
    st.write("""
    1. Boil Water with tea leaves
    2. Add milk and spices
    3. Serve hot    
""")

st.markdown('###Welcome to chai app')
st.markdown('>Blockquote')



