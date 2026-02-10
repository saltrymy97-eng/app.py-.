# app.py-.
"Retrofitting global water assets with AI to transform existing pumps into smart, self-funding, and sustainable networks."


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------
# 1. AI & ANALYTICAL ENGINE
# ---------------------------------------------------------

def ai_predict_energy(temp, sunlight_hrs, panel_efficiency=0.18):
    # Simulating a more complex relationship for solar energy
    # Energy (kWh) = Area * Solar Irradiance * Efficiency
    # We assume a base area for the community system
    base_irradiance = (sunlight_hrs * 1000) * (1 + (temp - 25) * -0.004) # Temp coefficient
    prediction = base_irradiance * panel_efficiency * 50 # 50sqm panels
    return max(0, prediction)

def ai_predict_water_demand(temp, population):
    # Water demand increases non-linearly with temperature
    base_consumption = 50 # liters per person
    temp_factor = 1 + (max(0, temp - 20) * 0.05) 
    demand = population * base_consumption * temp_factor
    return demand

def calculate_carbon_credits(solar_energy_kwh):
    # Financial Value = (Solar Energy Produced × Diesel Emission Factor) × Carbon Market Price
    DIESEL_EMISSION_FACTOR = 0.85 # kg CO2 per kWh
    CARBON_MARKET_PRICE = 0.04   # $ per kg of CO2 (average price)
    
    co2_saved = solar_energy_kwh * DIESEL_EMISSION_FACTOR
    financial_value = co2_saved * CARBON_MARKET_PRICE
    return co2_saved, financial_value

# ---------------------------------------------------------
# 2. STREAMLIT UI SETUP
# ---------------------------------------------------------
st.set_page_config(page_title="AquaFlow AI Dashboard", layout="wide")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_content_id=True)

st.title("🌊 AquaFlow AI: Smart Water & Energy Hub")
st.markdown("---")

# ---------------------------------------------------------
# 3. SIDEBAR INPUTS
# ---------------------------------------------------------
st.sidebar.header("📍 Real-time Parameters")
temp = st.sidebar.slider("🌡️ Ambient Temperature (°C)", 0, 50, 25)
sunlight = st.sidebar.slider("☀️ Sunlight Exposure (Hours)", 0, 14, 8)
population = st.sidebar.number_input("👥 Community Population", value=1000, step=100)
st.sidebar.markdown("---")
st.sidebar.info("This AI agent optimizes existing infrastructure by balancing clean energy and water demand.")

# ---------------------------------------------------------
# 4. EXECUTION & RESULTS
# ---------------------------------------------------------
if st.sidebar.button("🚀 Run AI Diagnostic"):
    energy_output = ai_predict_energy(temp, sunlight)
    water_demand = ai_predict_water_demand(temp, population)
    co2_saved, credits_value = calculate_carbon_credits(energy_output)
    
    # Row 1: Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Solar Production", f"{energy_output:.1f} kWh", delta="Renewable")
    with col2:
        st.metric("Water Demand", f"{water_demand/1000:.1f} m³", delta="- Consumption", delta_color="inverse")
    with col3:
        st.metric("CO2 Offset", f"{co2_saved:.1f} kg", delta="Clean Energy")
    with col4:
        st.metric("Green Assets", f"${credits_value:.2f}", delta="Carbon Credits")

    st.markdown("### 🧠 AI System Recommendation")
    
    # Decision Logic
    efficiency_ratio = energy_output / (water_demand * 0.005) # Assume 0.005kWh per liter for pump/purification
    
    if efficiency_ratio >= 1.0:
        st.success(f"**Optimal Performance:** Solar energy covers 100% of demand. System is allocating surplus energy to 'Green Asset' conversion.")
    elif efficiency_ratio > 0.6:
        st.warning(f"**Partial Support:** Solar covers {efficiency_ratio*100:.1f}% of demand. AI recommends activating Grid-Hybrid mode during peak hours.")
    else:
        st.error(f"**Critical Alert:** Energy deficit detected. AI suggests prioritizing purification units over secondary irrigation.")

    # Row 2: Visualizations
    st.markdown("---")
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Energy vs Demand Balance")
        fig, ax = plt.subplots()
        labels = ['Energy Supply (Scaled)', 'Water Demand (Scaled)']
        values = [energy_output, water_demand / 10] # Scaling for visibility
        ax.bar(labels, values, color=['#ffaa00', '#0088ff'])
        st.pyplot(fig)

    with c2:
        st.subheader("Carbon Credit Growth Projection")
        # Simulating a 7-day forecast
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        forecast_data = [credits_value * (1 + np.random.uniform(-0.1, 0.2)) for _ in range(7)]
        st.line_chart(pd.DataFrame(forecast_data, index=days, columns=["Estimated Revenue ($)"]))

else:
    st.image("https://images.unsplash.com/photo-1509391366360-feaffa64e58b?auto=format&fit=crop&w=1000&q=80", caption="Smart Solar Infrastructure Management")
    st.info("Adjust parameters in the sidebar and click 'Run AI Diagnostic' to see the system in action.")

# ---------------------------------------------------------
# 5. FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption("AquaFlow AI | Built for Code Spring Hackathon 2026 | Sustainable Development Goal 6 & 7")

streamlit
pandas
matplotlib
numpy
