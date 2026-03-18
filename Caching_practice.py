'''

Streamlit apps return from top to bottom on every iteration.
for example , click button , change filter , upload file

problem : Heavy operations repeat:
Reading file , API calls again , Model loading again

solution :

Caching stores the output of a function and reuses it if nothing changed



'''
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("chai_sale.csv")

'''
Streamlit Does:
1.Execute function 
2.Serializes output
3.Creates a hash key using:
    function code
    input parameters
4. stores result in cache

on next run :
    recalculate hash
    compare with stored result
    if same -> return cached result
    if different -> re-run function

TWO TYPES OF CACHE :
    1. DATA CACHE : (returns copy)
            CSV loading
            API Resources
            Data transformation
    2. RESOURCE CACHE :
            ML models
            DB Connections
            Large Objects
'''
# time based cache
@st.cache_data(ttl=60)
def get_data():
    return pd.read_csv("file.csv")

# memory management
@st.cache_data(max_entries=10)

# Manual Cache Clear
# st.cache_data.clear()
# st.cache_resource.clear()

#@st.cache_data
def load_data():
    print("Loading data...")
    return pd.read_csv("chai_sale.csv")