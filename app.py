# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# --- Title ---
st.title(" 🧠 Customer Segmentation using RFM and Clustering")

st.markdown("""
Welcome to the **Customer Segmentation Dashboard**!  
This app performs **RFM (Recency, Frequency, Monetary) analysis** on retail data  
and uses **KMeans clustering** to identify key customer segments like:

- 🥇 High-Value Customers  
- 📦 Regular Buyers  
- 💤 At-Risk Customers  
- 🎯 Occasional Shoppers  

Upload your dataset, explore insightful visuals, and understand customer behavior better.
""")

# --- Upload CSV ---
file = st.file_uploader("Upload Retail Dataset", type=['csv'])

if file is not None:
    df = pd.read_csv(file)

    # --- Preprocessing ---
    df.dropna(subset=['CustomerID'], inplace=True)
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    
    df['CustomerID'] = df['CustomerID'].astype(int)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    # --- RFM Calculation ---
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalPrice': 'Monetary'
    })

    # --- Normalization ---
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    # --- Clustering ---
    kmeans = KMeans(n_clusters=4, random_state=1)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    st.subheader("RFM Table with Cluster Labels")
    st.dataframe(rfm.reset_index())

    # --- Cluster Summary ---
    st.subheader("📊 Cluster Summary (RFM Means)")
    st.dataframe(rfm.groupby('Cluster').mean().round(2))

    # --- Plotting ---
    st.subheader("📈 Recency vs Monetary (Colored by Cluster)")
    fig, ax = plt.subplots()
    sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', palette='Set2', ax=ax)
    st.pyplot(fig)
