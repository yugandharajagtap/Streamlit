'''
Basic python library for  plotting graphs
produces static charts
good for learning fundamentrals

Types :
1. Linechart
2. Bar chart
3. Scatter plot
4. Histogram

core concept :

Figure(fig) : full chart
Axes(ax) : actual graph area

'''
# import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [10,20,15,25]

# fig , ax = plt.subplots()
# ax.plot(x,y)

# plt.show()

# matplotlib in streamilt 
import streamlit as st
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

fig , ax = plt.subplots()
ax.plot(x,y)

st.pyplot(fig)



