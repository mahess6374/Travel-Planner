import streamlit as st
from data import cities
st.markdown("""
<style>
/* Background */
body {
    background-color: #0e1117;
    color: white;
}
/* Title */
h1 {
    color: #00BFFF;
    text-align: center;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Buttons */
.stButton>button {
    background-color: #00BFFF;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

/* Cards effect */
.block-container {
    padding: 2rem;
}
</style>
""", unsafe_allow_html=True)
from planner import generate_itinerary, calculate_budget

# Page settings
st.set_page_config(page_title="Travel Planner Pro", layout="wide")

# Title
st.title("🌍..1 Smart Travel Planner Pro")
st.caption("Plan your trips intelligently with budget optimization and smart itineraries")
st.markdown("### ✈️ Plan smarter, travel better")
st.divider()

# Sidebar inputs
st.sidebar.header("Trip Details")

city = st.sidebar.selectbox("Select City", list(cities.keys()))
days = st.sid=labelk
webar.slider("Number of Days", 1, 7, 3)
budget = st.sidebar.number_input("Total Budget ₹", value=5000)
style = st.sidebar.selectbox("Travel Style", ["Budget", "Balanced", "Luxury"])

# Generate plan
if st.sidebar.button("✨ Create My Trip"):

    if budget < 1000:
        st.warning("⚠️ Budget too low. Increase budget.")
    else:
        city_data = cities[city] z,k
        if budget < city_data["hotel_cost_per_day"] * days:
            st.error("⚠️ Budget too low to cover hotel costs!")

        itinerary = generate_itinerary(city_data, days)
        budget_data = calculate_budget(city_data, days, budget, style)

        col1, col2 = st.columns(2)
    
        # Itinerary  
        with col1:
            st.subheader
            ("📅 Itinerary")
            for i, place in enumerate(itinerary):
            st.markdown(
        f"""n
        ### 📍 Day {i+1}
        **Place:** {place['name']}  
        **Type:** {place['type']}
        """
    )

            st.info("💡 Tip: Visit places in morning or evening for best experience.")

        # Budget
        with col2:
            st.subheader("💰 Expense Overview")
            for key, value in budget_data.items():
                st.metric(label=key, value=f"₹{value:.0f}")
                st.success("✅ Plan generated based on your travel style and budget constraints.")
                