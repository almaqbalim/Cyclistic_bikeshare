import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ─────────────────────────────────────
# 🔧 Config & Styling
# ─────────────────────────────────────
st.set_page_config(page_title="Cyclistic Bike-Share Report", layout="wide")
sns.set_style("whitegrid")
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["figure.facecolor"] = "white"
st.title("🚲 Cyclistic Bike-Share Report")
