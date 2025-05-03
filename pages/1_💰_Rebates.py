import streamlit as st

st.title("💰 Find Local Rebates")
st.markdown("Rebates can significantly reduce the cost of upgrades! Check these resources (always verify current offers):")

st.markdown("""
* **California Water Service (Cal Water):** Visit the Cal Water website and search for their conservation or rebate programs specific to the Stockton district. They often have rebates for toilets, washers, irrigation controllers.
* **City of Stockton Municipal Utilities:** Check the City of Stockton's official website under Public Works or Utilities for any city-managed water conservation programs or incentives.
* **EPA WaterSense Program:** Look for the WaterSense label when shopping. These products are certified for efficiency and often required for rebates. ([www.epa.gov/watersense](https://www.epa.gov/watersense))
* **PG&E:** Check PG&E's website for potential rebates on energy-efficient appliances like water heaters or washing machines that also save water.
""")

st.info("Tip: Search online for '[Utility Name] + Stockton water rebates' for the latest info.")

# Optional Gamification Badge
if st.button("I checked for money-saving rebates!", key="rebate_check_button_page"):
    st.session_state.rebates_checked_flag = True # Use flag from app.py
    st.success("💰 Rebate Hunter! Smart move checking for discounts.")
    st.balloons()

if st.session_state.get('rebates_checked_flag', False): # Show if already clicked
     st.success("✅ Rebates Checked!")