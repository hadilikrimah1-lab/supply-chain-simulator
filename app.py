import streamlit as st
import pandas as pd

st.title("🌍 Supply Chain Cost Simulator")

fuel_price = st.sidebar.slider("Fuel Price ($/barrel)", 50, 150, 80)
tariff_rate = st.sidebar.slider("Import Tariff Rate (%)", 0, 50, 15)
exchange_rate = st.sidebar.slider("USD to CNY Exchange Rate", 6.0, 7.5, 6.8)

base_cost = 100000
adjusted_cost = base_cost + (fuel_price-80)*500 + tariff_rate*200 + (exchange_rate-6.8)*1000

st.metric("Total Supply Chain Cost", f"${adjusted_cost:,.0f}")
