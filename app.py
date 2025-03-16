# This generates a deployable app online

# Importing libraries
import streamlit as st
from risk_calc import calculate_lymphocele_risk

st.title("Lymphocele Risk Stratification Tool")
st.write("Estimate the risk of lymphocele formation after robotic prostatectomy.")

# User inputs (checkboxes)
bmi = st.checkbox("BMI ≥ 30 kg/m²")
anticoagulation = st.checkbox("Preoperative Anticoagulation")
surgery_history = st.checkbox("Prior Abdominal/Pelvic Surgery")
isup_ggg = st.checkbox("ISUP-GGG Grade ≥ 3")
lymph_nodes = st.checkbox("Lymph Nodes Removed (>15)")
surgery_time = st.checkbox("Prolonged Surgery (>3 hours)")
retzius_sparing = st.checkbox("Retzius-Sparing Prostatectomy")
drains = st.checkbox("Lack of Postoperative Drains")
peritoneal_flap = st.checkbox("Use of Peritoneal Flaps (PIF/PFF)")
lymphatic_embolization = st.checkbox("Lymphatic Embolization (LE)")

if st.button("Calculate Risk"):
    risk, category = calculate_lymphocele_risk(bmi, anticoagulation, surgery_history, isup_ggg, 
                                               lymph_nodes, surgery_time, retzius_sparing, drains, 
                                               peritoneal_flap, lymphatic_embolization)
    st.success(f"Risk Score: {risk}")
    st.subheader(category)


st.markdown(
    """
    ---
    **© 2025 Tanvir Singh Sethi** and **Dr. Kainaat Shergill**  
    All rights reserved. Unauthorized duplication is prohibited.
    Git Repo:https://github.com/tanvirss13/calculate_lymphocele_risk
    """,
    unsafe_allow_html=True
)