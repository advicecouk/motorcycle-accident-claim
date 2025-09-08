import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Motorcycle Accident Claims Assistance",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #ff4b4b; font-weight: 700;}
    .section-header {font-size: 2rem; color: #1f77b4; border-bottom: 2px solid #ff4b4b; padding-bottom: 0.3rem;}
    .highlight-box {background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0;}
    .stat-box {background-color: #1f77b4; color: white; padding: 15px; border-radius: 10px; text-align: center;}
    .contact-form {background-color: #f0f2f6; padding: 20px; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<h1 class="main-header">Motorcycle Accident Claims Assistance</h1>', unsafe_allow_html=True)
    st.markdown("### Expert legal support for motorcycle accident victims across the UK")
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=100)

st.markdown("---")

# Introduction
st.markdown("""
If you've been involved in a motorcycle accident that wasn't your fault, you may be entitled to compensation. 
Our specialist solicitors have years of experience helping riders get the compensation they deserve for their injuries and losses.
""")

# Key Statistics
st.markdown('<h2 class="section-header">Why Choose Our Services?</h2>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-box"><h3>98%</h3><p>Success Rate</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><h3>£50M+</h3><p>Recovered for Clients</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><h3>24/7</h3><p>Legal Support</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-box"><h3>No Win No Fee</h3><p>Available</p></div>', unsafe_allow_html=True)

# Types of Claims
st.markdown("---")
st.markdown('<h2 class="section-header">Types of Motorcycle Accident Claims We Handle</h2>', unsafe_allow_html=True)

claims_data = {
    "Accident Type": [
        "Car pulling out from side road",
        "Left-turn accidents",
        "Right-turn accidents",
        "Rear-end collisions",
        "Dooring accidents",
        "Hit and run incidents",
        "Road defect accidents",
        "Multi-vehicle collisions"
    ],
    "Description": [
        "When a car fails to give way and pulls out in front of you",
        "When a vehicle turns left across your path",
        "When a vehicle turns right across your path",
        "When you're hit from behind by another vehicle",
        "When a car door is opened into your path",
        "When the responsible party flees the scene",
        "Accidents caused by poor road maintenance or design",
        "Complex accidents involving multiple vehicles"
    ]
}

df = pd.DataFrame(claims_data)
st.table(df)

# Compensation Calculator
st.markdown("---")
st.markdown('<h2 class="section-header">Compensation Estimate Calculator</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    injury_type = st.selectbox(
        "Type of Injury",
        ["Whiplash", "Broken bones", "Head injury", "Spinal injury", "Soft tissue damage", "Psychological trauma"]
    )
    recovery_time = st.slider("Expected Recovery Time (months)", 1, 36, 6)
    
with col2:
    lost_income = st.number_input("Estimated Lost Income (£)", 0, 100000, 5000)
    other_costs = st.number_input("Other Costs (vehicle repair, medical bills, etc.) (£)", 0, 50000, 2000)

# Simple calculation (this is a simplified example)
base_compensation = {
    "Whiplash": 3000,
    "Broken bones": 8000,
    "Head injury": 15000,
    "Spinal injury": 25000,
    "Soft tissue damage": 5000,
    "Psychological trauma": 6000
}

if injury_type:
    estimated_comp = base_compensation[injury_type] * (recovery_time/6) + lost_income + other_costs
    st.markdown(f'<div class="highlight-box"><h3>Estimated Compensation: £{estimated_comp:,.0f}</h3></div>', unsafe_allow_html=True)
    st.caption("Note: This is only an estimate. Actual compensation may vary based on specific circumstances.")

# Process Explanation
st.markdown("---")
st.markdown('<h2 class="section-header">Our Claims Process</h2>', unsafe_allow_html=True)

process_steps = [
    {"step": "1", "title": "Free Consultation", "desc": "We'll discuss your accident and assess your claim with no obligation."},
    {"step": "2", "title": "Evidence Gathering", "desc": "We'll help collect evidence including police reports, witness statements, and medical records."},
    {"step": "3", "title": "Medical Assessment", "desc": "We'll arrange an independent medical assessment to document your injuries."},
    {"step": "4", "title": "Claim Submission", "desc": "We'll handle all negotiations with the other party's insurers."},
    {"step": "5", "title": "Settlement", "desc": "We'll work to secure the maximum compensation you're entitled to."}
]

for step in process_steps:
    with st.expander(f"Step {step['step']}: {step['title']}"):
        st.write(step['desc'])

# Contact Form
st.markdown("---")
st.markdown('<h2 class="section-header">Contact Us for a Free Consultation</h2>', unsafe_allow_html=True)

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
    with col2:
        phone = st.text_input("Phone Number")
        accident_date = st.date_input("Date of Accident")
    
    accident_details = st.text_area("Brief Description of the Accident")
    
    submitted = st.form_submit_button("Submit Inquiry")
    if submitted:
        st.success("Thank you for your inquiry. We'll contact you within 24 hours to discuss your claim.")

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.markdown("**Contact Info**")
    st.markdown("📞 0800 123 4567")
    st.mark("📧 claims@motorcyclelegal.uk")
with footer_col2:
    st.markdown("**Office Hours**")
    st.markdown("Monday-Friday: 8am-8pm")
    st.markdown("Weekends: 10am-4pm")
with footer_col3:
    st.markdown("**Legal**")
    st.markdown("Privacy Policy")
    st.markdown("Terms of Service")

st.markdown("<div style='text-align: center; margin-top: 20px;'>© 2023 Motorcycle Accident Claims Assistance. All rights reserved.</div>", unsafe_allow_html=True)
