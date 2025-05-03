import streamlit as st

st.title("💧 Check for Leaks")
st.markdown("Leaks are silent water wasters! Finding them can save hundreds or thousands of gallons per month.")

st.subheader("How to Check:")
st.markdown("""
* **1. Meter Check:**
    * Safely locate your water meter (usually near the curb under a concrete/metal lid).
    * Turn off *all* water inside and outside your house (faucets, showers, washer, ice maker, sprinklers).
    * Carefully lift the meter lid. Watch the meter dial (it might have a small triangle, star, or a low-flow indicator wheel).
    * If this indicator is moving, even *very slowly*, you likely have a leak somewhere in your system (after the meter).
* **2. Toilet Test:**
    * Toilets are common culprits! Remove the lid from the toilet *tank* (the back part).
    * Add several drops of dark food coloring (or a dye tablet available at hardware stores) into the *tank water*.
    * Wait 10-15 minutes. **Do NOT flush the toilet during this time.**
    * Look in the toilet *bowl*. If any colored water appears in the bowl, the flapper valve (at the bottom of the tank) is leaking and needs replacement. This is usually an inexpensive and easy DIY fix! Repeat for all toilets.
* **3. Visual Check:**
    * Regularly look for drips under sinks, behind toilets, around faucet bases, showerheads, outdoor hose bibs, and appliance connections (washer, dishwasher, water heater).
    * Check your irrigation system regularly for broken sprinkler heads, leaky valves, or damp spots in the lawn when the system hasn't run.
""")
st.warning("If you suspect a major leak or aren't comfortable checking, contact a licensed plumber.")





st.divider()
st.subheader("Reporting Leaks")
st.warning("It's important to report leaks beyond your property line or if you need assistance.")
st.markdown("""
* **For leaks on your property:** You are typically responsible. Use the checks above or contact a qualified plumber.
* **For leaks in the street, public areas, or from fire hydrants:**
    * Contact **California Water Service (Cal Water) Stockton Customer Center**. Search online for their current **Stockton customer service phone number** or leak reporting line.
    * You might also be able to report issues via the **City of Stockton** website or their general service request line (search 'City of Stockton report issue').
""")
# Keep the optional gamification button if desired
st.divider()
if st.button("I understand how to check for leaks!", key="leaks_check_button_page"):
    st.session_state.leaks_acknowledged_flag = True # Use flag from Home.py
    st.info("🕵️ Leak Detective! Finding leaks is key to saving water.")

if st.session_state.get('leaks_acknowledged_flag', False): # Show if already clicked
     st.success("✅ Leak Check Acknowledged!")