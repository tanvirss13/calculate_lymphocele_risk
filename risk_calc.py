# Python Script for Risk Calculation
# This script allows users to input patient/surgical factors and calculates their risk score.

# Basic Function for setup and calcualtion

def calculate_lymphocele_risk(bmi, anticoagulation, surgery_history, isup_ggg, 
                              lymph_nodes, surgery_time, retzius_sparing, drains, 
                              peritoneal_flap, lymphatic_embolization):
    # Assign risk points
    risk_score = 0
    if bmi: risk_score += 3
    if anticoagulation: risk_score += 2
    if surgery_history: risk_score += 2
    if isup_ggg: risk_score += 2
    if lymph_nodes: risk_score += 3
    if surgery_time: risk_score += 2
    if retzius_sparing: risk_score += 3
    if not drains: risk_score += 2
    if peritoneal_flap: risk_score -= 4
    if lymphatic_embolization: risk_score -= 3

    # Determine risk category
    if risk_score <= 3:
        return risk_score, "🟢 Low Risk (Minimal risk of symptomatic lymphocele formation)"
    elif 4 <= risk_score <= 6:
        return risk_score, "🟡 Moderate Risk (Closer follow-up required)"
    else:
        return risk_score, "🔴 High Risk (Preventive measures strongly recommended)"
    