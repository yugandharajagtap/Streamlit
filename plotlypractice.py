'''
Modern chart library
fully interactive:
    zoom , Hover  , Tooltips
used in dashbord 
important for projects

types :
Line , Bar , pie and scatter

'''
import streamlit as st
import plotly.express as px

st.title("Plotly Chart")

data ={
    "day":[1,2,3,4],
    "Sales":[10,20,15,25]
}

fig = px.line(data , x= "day", y="Sales",title="Sales Trend")

st.plotly_chart(fig)

# chai Data 

import pandas as pd 

df = pd.read_csv("chai_sale.csv")

st.title("Chai Dashbord")

fig = px.bar(df , x="City",y="Chai_Type",title="Chai sales by city")

st.plotly_chart(fig)





