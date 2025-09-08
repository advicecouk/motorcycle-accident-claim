import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="Motorcycle Accident Claims | Advice UK",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #1E3A8A; font-weight: 700;}
    .sub-header {font-size: 1.8rem; color: #1E3A8A; font-weight: 600;}
    .highlight-box {background-color: #F0F9FF; padding: 2rem; border-radius: 10px; margin: 1rem 0;}
    .stat-box {background-color: #1E3A8A; color: white; padding: 1.5rem; border-radius: 10px; text-align: center;}
    .bullet-point {margin-left: 1.5rem; margin-bottom: 0.5rem;}
    .contact-button {background-color: #FF4B4B; color: white; padding: 0.7rem 1.5rem; border-radius: 5px; border: none; font-weight: 600;}
    .contact-button:hover {background-color: #FF6B6B;}
    .stProgress > div > div > div > div {background-color: #1E3A8A;}
    .footer {text-align: center; margin-top: 3rem; padding: 1rem; background-color: #F0F2F6;}
</style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="main-header">Motorcycle Accident Claims</p>', unsafe_allow_html=True)
    st.markdown("### Expert legal support for motorcyclists injured on the road")
with col2:
    # This would be your logo - using placeholder text for now
    st.markdown("""
    <div style="text-align: right; padding: 1rem;">
        <h3 style="color: #1E3A8A;">ADVICE UK</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Introduction section
st.markdown("""
<div class="highlight-box">
    <h2>Have you been injured in a motorcycle accident that wasn't your fault?</h2>
    <p>Our specialist solicitors are here to help you get the compensation you deserve. 
    With over 15 years of experience in motorcycle accident claims, we understand the unique challenges riders face.</p>
</div>
""", unsafe_allow_html=True)

# Key statistics section
st.markdown("## Why Choose Our Motorcycle Claim Services?")
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown('<div class="stat-box"><h3>98%</h3><p>Success Rate</p></div>', unsafe_allow_html=True)
with stats_col2:
    st.markdown('<div class="stat-box"><h3>£50M+</h3><p>Recovered for Clients</p></div>', unsafe_allow_html=True)
with stats_col3:
    st.markdown('<div class="stat-box"><h3>24/7</h3><p>Legal Support</p></div>', unsafe_allow_html=True)
with stats_col4:
    st.markdown('<div class="stat-box"><h3>No Win</h3><p>No Fee Policy</p></div>', unsafe_allow_html=True)

# Process explanation
st.markdown("## Our Simple Claims Process")
steps = st.columns(4)

with steps[0]:
    st.markdown("### 1. Contact Us")
    st.markdown("Free initial consultation to discuss your case")
with steps[1]:
    st.markdown("### 2. Case Review")
    st.markdown("We gather evidence and assess your claim")
with steps[2]:
    st.markdown("### 3. Claim Submission")
    st.markdown("We handle all paperwork and negotiations")
with steps[3]:
    st.markdown("### 4. Compensation")
    st.markdown("We work to maximize your settlement")

# Progress visualization
st.markdown("### Typical Claim Timeline")
timeline_data = pd.DataFrame({
    'Phase': ['Initial Contact', 'Evidence Gathering', 'Medical Assessment', 'Negotiation', 'Settlement'],
    'Duration (weeks)': [1, 4, 4, 6, 2]
})

fig = px.bar(timeline_data, x='Phase', y='Duration (weeks)', 
             color='Phase', color_discrete_sequence=px.colors.qualitative.Dark2)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# Compensation calculator
st.markdown("## Estimate Your Compensation")
col1, col2 = st.columns(2)

with col1:
    injury_type = st.selectbox("Type of Injury", 
                              ["Whiplash", "Broken Bones", "Head Injury", "Soft Tissue Damage", "Psychological Trauma"])
    recovery_time = st.slider("Expected Recovery Time (months)", 1, 36, 6)
    
with col2:
    lost_income = st.number_input("Lost Income (£)", min_value=0, max_value=100000, value=5000, step=1000)
    other_expenses = st.number_input("Other Expenses (£)", min_value=0, max_value=20000, value=1000, step=500)

# Calculate compensation (simplified estimation)
base_compensation = {
    "Whiplash": 3000,
    "Broken Bones": 8000,
    "Head Injury": 15000,
    "Soft Tissue Damage": 5000,
    "Psychological Trauma": 6000
}

if injury_type in base_compensation:
    injury_comp = base_compensation[injury_type] * (recovery_time / 6)
    total_comp = injury_comp + lost_income + other_expenses
    
    st.markdown(f"""
    <div class="highlight-box">
        <h3>Estimated Compensation: £{total_comp:,.0f}</h3>
        <p><small>This is a rough estimate based on the information provided. 
        Actual compensation may vary based on the specific circumstances of your case.</small></p>
    </div>
    """, unsafe_allow_html=True)

# Common accident types
st.markdown("## Common Motorcycle Accident Scenarios")
scenarios = st.columns(3)

with scenarios[0]:
    st.markdown("""
    <div style="padding: 1rem; background-color: #F0F9FF; border-radius: 10px; height: 200px;">
        <h4>Right of Way Violations</h4>
        <p>When drivers fail to yield to motorcycles at intersections</p>
    </div>
    """, unsafe_allow_html=True)

with scenarios[1]:
    st.markdown("""
    <div style="padding: 1rem; background-color: #F0F9FF; border-radius: 10px; height: 200px;">
        <h4>Left Turn Accidents</h4>
        <p>When cars turn left across the path of an approaching motorcycle</p>
    </div>
    """, unsafe_allow_html=True)

with scenarios[2]:
    st.markdown("""
    <div style="padding: 1rem; background-color: #F0F9FF; border-radius: 10px; height: 200px;">
        <h4>Lane Changing Incidents</h4>
        <p>When drivers change lanes without noticing motorcycles in their blind spots</p>
    </div>
    """, unsafe_allow_html=True)

# FAQ section
st.markdown("## Frequently Asked Questions")
with st.expander("How long do I have to make a motorcycle accident claim?"):
    st.write("In most cases, you have three years from the date of the accident to make a claim. There are some exceptions, so it's best to contact us as soon as possible.")

with st.expander("What if the accident was partially my fault?"):
    st.write("You may still be able to claim compensation even if you were partly to blame. This is called 'contributory negligence' and we can advise how it might affect your claim.")

with st.expander("How much will it cost to make a claim?"):
    st.write("We operate on a 'no win, no fee' basis for most motorcycle accident claims. This means you won't pay anything if your claim is unsuccessful.")

with st.expander("What compensation can I claim for?"):
    st.write("You can claim for pain and suffering, loss of earnings, medical expenses, travel costs, motorcycle repairs, and other expenses directly resulting from your accident.")

# Contact form
st.markdown("## Start Your Claim Today")
contact_form = st.form(key='contact_form')
with contact_form:
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
    with col2:
        phone = st.text_input("Phone Number")
        accident_date = st.date_input("Date of Accident")
    
    case_details = st.text_area("Briefly describe your accident")
    submitted = st.form_submit_button("Submit Your Inquiry")
    
    if submitted:
        st.success("Thank you for your inquiry. We'll contact you within 24 hours to discuss your case.")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2023 Advice UK | Road Traffic Accident Claims | Motorcycle Accident Claims</p>
    <p>Regulated by the Solicitors Regulation Authority | Privacy Policy | Terms of Use</p>
</div>
""", unsafe_allow_html=True)
