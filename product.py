import streamlit as st
import pandas as pd
import numpy as np
import pickle  # For loading models (if needed)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Title
st.title("🧠 Customer Insights Dashboard")

st.markdown("""
Welcome to the interactive dashboard for **Product Recommendation** and **Customer Segmentation**.
Use the modules below to discover similar products or segment customers based on RFM values.
""")

# Tabs for modules
tab1, tab2 = st.tabs(["🎯 Product Recommendation", "🎯 Customer Segmentation"])
with tab1:
    st.header("🔁 Product Recommendation Module")

    product_input = st.text_input("Enter a product name:", placeholder="e.g. WHITE METAL LANTERN")

    if st.button("🔍 Get Recommendations"):
        # Dummy logic (replace with collaborative filtering model)
        recommended_products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
        
        st.subheader("🧾 Recommended Products:")
        for prod in recommended_products:
            st.markdown(f"- ✅ **{prod}**")
with tab2:
    st.header("🧮 Customer Segmentation Module")

    recency = st.number_input("Enter Recency (in days):", min_value=0, value=30)
    frequency = st.number_input("Enter Frequency (number of purchases):", min_value=1, value=5)
    monetary = st.number_input("Enter Monetary (total spend):", min_value=0.0, value=100.0)

    if st.button("🔎 Predict Cluster"):
        # Load scaler and model (you must pre-train and save them)
        scaler = StandardScaler()
        kmeans = KMeans(n_clusters=4, random_state=1)

        # Dummy fit for example purposes (replace with real model)
        X_dummy = np.array([[recency, frequency, monetary]])
        X_scaled = scaler.fit_transform(X_dummy)
        cluster_label = kmeans.fit_predict(X_scaled)[0]

        segment_map = {
            0: "💎 High-Value",
            1: "📦 Regular",
            2: "🎯 Occasional",
            3: "⚠️ At-Risk"
        }

        st.success(f"📌 Predicted Segment: **{segment_map.get(cluster_label, 'Unknown')}** (Cluster {cluster_label})")
