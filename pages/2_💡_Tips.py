# import streamlit as st

# st.title("💡 Quick Conservation Tips")
# st.markdown("""
# * Run washing machines and dishwashers only with **full loads**.
# * Take **shorter showers** (aim for 5 minutes!).
# * Turn off the tap while brushing teeth or shaving.
# * Fix **leaky faucets and toilets** immediately (see 'Leaks' page!).
# * Use a **broom**, not a hose, to clean driveways/sidewalks.
# * Water lawns **efficiently**: early morning/late evening, check for leaks, adjust sprinklers seasonally, consider drought-tolerant plants. Use mulch in garden beds.
# * Install faucet **aerators** and efficient showerheads.
# * Use **water-wise landscaping** (xeriscaping) where possible.
# """)

# # Optional Gamification Badge
# if st.button("I learned these tips!", key="tips_learn_button_page"):
#     st.session_state.tips_read_flag = True # Use flag from app.py
#     st.success("✅ Knowledge Gained! Every tip helps save water.")

# if st.session_state.get('tips_read_flag', False): # Show if already clicked
#      st.success("✅ Tips Reviewed!")

import streamlit as st

st.set_page_config(page_title="Tips & Tools", page_icon="💡")

st.title("💡 Water-Saving Tips & Tools")

tab1, tab2, tab3 = st.tabs(["Bathroom", "Kitchen & Laundry", "Outdoors"])

with tab1:
    st.header("Bathroom Savings")
    st.markdown("""
    * **Showers:** Take shorter showers (aim for 5 minutes!). Install a WaterSense labeled showerhead (< 2.0 gpm).
    * **Toilets:** Don't use the toilet as a wastebasket. Check regularly for leaks using the dye test (see Leaks page!). Upgrade older toilets (pre-1994) to WaterSense models.
    * **Faucets:** Turn off the tap while brushing teeth or shaving. Install faucet aerators. Fix drips immediately.
    """)

with tab2:
    st.header("Kitchen & Laundry Savings")
    st.markdown("""
    * **Dishwasher:** Run only with full loads. Scrape food off plates, don't pre-rinse excessively. Upgrade to an Energy Star / WaterSense model when replacing.
    * **Washing Machine:** Run only with full loads. Adjust water level settings if possible. Use cold water when feasible (saves energy). Upgrade to a high-efficiency (HE) model when replacing.
    * **Faucets:** Fix drips promptly. Use a basin for washing vegetables instead of running water. Keep drinking water in the fridge instead of running the tap until cool.
    """)

with tab3:
    st.header("Outdoor Savings")
    st.markdown("""
    * **Watering:** Water lawns early morning or late evening to reduce evaporation. Water deeply but less frequently. Adjust sprinklers to avoid watering pavement. Check for leaks regularly.
    * **Landscaping:** Use mulch around plants/trees to retain moisture. Consider drought-tolerant or native plants (xeriscaping). Group plants with similar water needs.
    * **Cleaning:** Use a broom, not a hose, to clean driveways, sidewalks, and patios. Wash cars using a bucket and hose with an auto-shutoff nozzle.
    * **Pools:** Use a cover to reduce evaporation.
    """)

# Optional Gamification Badge (Keep as is or modify)
st.divider()
if st.button("I reviewed these tips!", key="tips_learn_button_page"):
    st.session_state.tips_read_flag = True # Use flag from Home.py
    st.success("✅ Knowledge Gained! Every tip helps save water.")

if st.session_state.get('tips_read_flag', False): # Show if already clicked
     st.success("✅ Tips Reviewed!")

# Link placeholder - replace if you find a real link quickly
st.divider()
st.markdown("Downloadable Tip Sheets (Example Links - Find Real Ones!):")
st.markdown("* [EPA WaterSense Tips](https://www.epa.gov/watersense/start-saving)")
st.markdown("* Search 'Cal Water Conservation Tips PDF'")