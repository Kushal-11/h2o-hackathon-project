import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Home", # Renamed slightly for clarity as home page
    page_icon="💧",
    layout="centered",
    # initial_sidebar_state="expanded" # Optional: Keep sidebar open initially
)

# --- Initialize Session State for Badges (Optional) ---
# Need to initialize these here so they persist across pages if used
if 'rebates_checked_flag' not in st.session_state:
    st.session_state.rebates_checked_flag = False
if 'tips_read_flag' not in st.session_state:
    st.session_state.tips_read_flag = False
if 'leaks_acknowledged_flag' not in st.session_state:
    st.session_state.leaks_acknowledged_flag = False

# --- Data Constants ---
APPLIANCE_SAVINGS = {
    "Toilet": {"gallons_month": 1000, "cost_month": 3.00, "info": "Older models use 3.5+ gal/flush."},
    "Showerhead": {"gallons_month": 750, "cost_month": 2.25, "info": "Older models use > 2.5 gal/min."},
    "Faucet": {"gallons_month": 500, "cost_month": 1.50, "info": "Aerator upgrades save water."},
    "Washing Machine": {"gallons_month": 1500, "cost_month": 4.50, "info": "HE models use much less water."},
    "Dishwasher": {"gallons_month": 200, "cost_month": 0.60, "info": "Energy Star models are efficient."},
    "Irrigation": {"gallons_month": 5000, "cost_month": 15.00, "info": "Smart controllers/drip systems save huge amounts."},
}
FIXED_SERVICE_FEE = 33.24 # Approx. Cal Water fixed fee for Stockton

# --- Main Page Content Function ---
def main_page():
    # --- App Header ---
    st.image("https://i.imgur.com/v9a1DHC.jpeg", width=200)
    st.title("💧 AquaSave Stockton: Savings Calculator")
    st.markdown("Estimate potential savings by upgrading inefficient appliances!")
    # st.markdown("Average Stockton Cal Water bill: $ 49/month, including a fixed fee of $33.24.")
    st.markdown("Average Stockton Cal Water bill is 49/month, including a fixed service fee of 33.24.")
    st.divider()


    # --- 1. Appliance Selection ---
    st.header("1. Identify Potential Upgrades")
    st.caption("Check the items you have that might be older or inefficient:")

    selections = {}
    col1, col2 = st.columns(2)
    with col1:
        selections["Toilet"] = st.checkbox(f"**Toilet(s)** ({APPLIANCE_SAVINGS['Toilet']['info']})", key="toilet")
        selections["Showerhead"] = st.checkbox(f"**Showerhead(s)** ({APPLIANCE_SAVINGS['Showerhead']['info']})", key="shower")
        selections["Faucet"] = st.checkbox(f"**Faucet(s)** ({APPLIANCE_SAVINGS['Faucet']['info']})", key="faucet")
    with col2:
        selections["Washing Machine"] = st.checkbox(f"**Washing Machine** ({APPLIANCE_SAVINGS['Washing Machine']['info']})", key="washer")
        selections["Dishwasher"] = st.checkbox(f"**Dishwasher** ({APPLIANCE_SAVINGS['Dishwasher']['info']})", key="dishwasher")
        selections["Irrigation"] = st.checkbox(f"**Irrigation System** ({APPLIANCE_SAVINGS['Irrigation']['info']})", key="irrigation")

    leak_check = st.checkbox("**Concerned about potential Leaks?** (Check the 'Leaks' page for info!)")
    st.divider()

    # --- 2. Calculate and Display Savings ---
    st.header("2. Your Estimated Monthly Savings Potential")

    total_gallons_saved = 0
    total_cost_saved = 0.0
    details_list = []

    for appliance, selected in selections.items():
        if selected:
            savings = APPLIANCE_SAVINGS[appliance]
            gallons = savings["gallons_month"]
            cost = savings["cost_month"]
            total_gallons_saved += gallons
            total_cost_saved += cost
            details_list.append(f"* **{appliance}:** ~{gallons:,} gal / ~${cost:.2f}")

    if not details_list and not leak_check:
        st.info("Check some appliances above to see potential savings!")
    else:
        col_gallons, col_cost = st.columns(2)
        with col_gallons:
            st.metric(label="Potential Gallons Saved", value=f"{total_gallons_saved:,} gal")
        with col_cost:
            st.metric(label="Potential Bill Reduction", value=f"${total_cost_saved:.2f}")

        if details_list:
            st.subheader("Savings Breakdown:")
            st.markdown("\n".join(details_list))

        if leak_check:
             st.warning("**Leaks:** Fixing leaks saves water and money! See the 'Leaks' page for how to check.")

        # --- Gamification: Bill Buster Progress ---
        st.divider()
        st.subheader("📈 Bill Buster Progress")
        st.caption(f"See how much of the typical ${FIXED_SERVICE_FEE:.2f} monthly fixed service fee your potential savings could cover!")

        if total_cost_saved > 0:
            progress_percentage = min(total_cost_saved / FIXED_SERVICE_FEE, 1.0)
            st.progress(progress_percentage)

            if progress_percentage >= 1.0:
                st.success(f"🏆 Goal Met! Your potential savings of ${total_cost_saved:.2f}/month could cover the entire fixed fee!")
            elif progress_percentage >= 0.75:
                st.info(f"👍 Almost there! Covering about {int(progress_percentage*100)}% of the fixed fee.")
            elif progress_percentage >= 0.50:
                st.info(f"💪 Good progress! Covering about {int(progress_percentage*100)}% of the fixed fee.")
            elif progress_percentage > 0:
                 st.info(f"🌱 Starting point! Covering about {int(progress_percentage*100)}% of the fixed fee.")
        else:
            if not leak_check:
                 st.info("Select potential upgrades above to see your Bill Buster progress!")

    st.divider()
    st.caption("Disclaimer: All savings shown are estimates. Actual savings vary. See resource pages for more info.")

# --- Run the main page content ---
# Streamlit automatically handles page switching based on the pages/ directory
main_page() # Call the main page function directly