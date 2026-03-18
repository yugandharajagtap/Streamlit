import streamlit as st

st.title("Chai Maker App")
st.subheader("Let's Make Your Man Pasand Chai")

name = st.text_input("Enter your name")
dob = st.date_input("Select your date of birth")
address = st.text_input("You are From")

tea_type = st.radio("Pick your chai base :",["Milk","water","Almond" , "Lemon"])

flavour = st.selectbox("choose flavour:",["Adrak","Kesar","Tulsi"])
sugar = st.slider("Sugar level(spoon)", 0 , 5 ,2) #2 is default value

cups = st.number_input("How many cups you want to enjoy",min_value = 1 , max_value =10 , step = 1)
st.write(f" {cups} Cups , Right!")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added to your chai")

if st.button("Make Chai"):
    st.success("Accepted")
    st.write(f"Heyyyy {name} You are from {address}")
    st.write(f" Your Selected Base is  {tea_type}")
    st.write(f"Selected flavour is {flavour}")
    st.write(f"Selected sugar level  is {sugar}")

    st.write(f"{name}! Your Manpasand Chai is comming soon , are you ready ?")


# '''
#     TYPES of INPUT :
#         text_input()
#         text_area()
#         number_input()

#         button() , checkbox() , radio() , selectbox() , multiselect ()

#         slider()
#         select_slider()

#         file_uploader()

#         date_input()
#         time_input()

#         color_picker()
# '''

