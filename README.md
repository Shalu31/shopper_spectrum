# 🛍️ Shopper Spectrum
A Streamlit web app for Product Recommendation and Customer Segmentation using collaborative filtering and RFM analysis.
A Streamlit web application that provides:
- 🎯 **Product Recommendations** using collaborative filtering.
- 🧠 **Customer Segmentation** based on RFM (Recency, Frequency, Monetary) inputs.

<img width="883" height="464" alt="image" src="https://github.com/user-attachments/assets/4319adfb-a027-4056-8a69-77582d685685" />
<img width="873" height="469" alt="image" src="https://github.com/user-attachments/assets/f13da6c6-d4fb-4157-a49e-5876a740d68f" />
# 🛍️ Shopper Spectrum



## 🚀 Features

### 1️⃣ Product Recommendation Module
- 🔍 Enter a product name
- 🤖 Get 5 similar product suggestions
- 📋 Displayed in a clean, user-friendly format

### 2️⃣ Customer Segmentation Module
- 📅 Input Recency (days)
- 🔁 Input Frequency (number of purchases)
- 💰 Input Monetary (total spend)
- 🧠 Predicts cluster label like:
  - High-Value
  - Regular
  - Occasional
  - At-Risk

---

## 🛠️ Tech Stack
- Python
- Streamlit
- NumPy / Pandas

---

## 🧪 Run Locally

```bash
# Clone the repo
git clone https://github.com/Shalu31/shopper-spectrum.git
cd shopper-spectrum-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

