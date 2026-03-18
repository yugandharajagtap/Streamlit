import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Chai Dashboard", layout="wide")

st.title("☕ Chai Visualization Dashboard")

# ------------------ CACHE FUNCTIONS ------------------ #

# Cache data loading
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Cache filtering
@st.cache_data
def filter_data(df, city, chai_type):
    df = df.copy()

    if city != "All":
        df = df[df["City"] == city]

    if chai_type:
        df = df[df["Chai_Type"].isin(chai_type)]

    return df

# ------------------ FILE UPLOAD ------------------ #
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = load_data(file)
else:
    df = load_data("chai_sale.csv")

# ------------------ SIDEBAR FILTERS ------------------ #
st.sidebar.header("🔍 Filter Data")

city = st.sidebar.selectbox(
    "Select City",
    ["All"] + list(df["City"].unique())
)

chai_type = st.sidebar.multiselect(
    "Select Chai Type",
    df["Chai_Type"].unique()
)

# ------------------ APPLY FILTER ------------------ #
filtered_df = filter_data(df, city, chai_type)

# ------------------ KPIs ------------------ #
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Orders", len(filtered_df))

with col2:
    st.metric("Unique Cities", filtered_df["City"].nunique())

with col3:
    st.metric("Chai Types", filtered_df["Chai_Type"].nunique())

# ------------------ DATA PREVIEW ------------------ #
with st.expander("📂 View Dataset"):
    st.dataframe(filtered_df)

# ------------------ CHARTS ------------------ #
st.subheader("📈 Visual Insights")

col1, col2 = st.columns(2)

# Matplotlib Chart
with col1:
    st.subheader("Chai Type (Matplotlib)")
    chai_count = filtered_df["Chai_Type"].value_counts()

    fig, ax = plt.subplots()
    ax.bar(chai_count.index, chai_count.values)
    ax.set_title("Chai Distribution")
    st.pyplot(fig)

# Plotly Pie Chart
with col2:
    st.subheader("Chai Type (Plotly)")
    fig_plotly = px.pie(
        filtered_df,
        names="Chai_Type",
        title="Chai Distribution",
        hole=0.4
    )
    st.plotly_chart(fig_plotly, use_container_width=True)

# ------------------ CITY ANALYSIS ------------------ #
st.subheader("🏙 Chai by City")

fig_city = px.bar(
    filtered_df,
    x="City",
    color="Chai_Type",
    barmode="group",
    title="City-wise Chai Sales"
)

st.plotly_chart(fig_city, use_container_width=True)

# ------------------ ADVANCED CHART ------------------ #
st.subheader("🔥 Advanced Insight")

fig_heatmap = px.histogram(
    filtered_df,
    x="City",
    color="Chai_Type",
    title="Distribution Heatmap"
)

st.plotly_chart(fig_heatmap, use_container_width=True)