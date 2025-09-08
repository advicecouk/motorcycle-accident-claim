import streamlit as st
import pandas as pd
import numpy as np
import time

# Set page configuration
st.set_page_config(
    page_title="Motorcycle Accident Claims Specialist | UK Legal Experts",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Montserrat', sans-serif;
    box-sizing: border-box;
}

.main-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.main-header {
    font-size: 2.8rem;
    font-weight: 800;
    color: #1a3a6c;
    text-align: center;
    margin-bottom: 1rem;
    line-height: 1.2;
}

.subheader {
    font-size: 1.4rem;
    font-weight: 500;
    color: #4a6fa5;
    text-align: center;
    margin-bottom: 2rem;
    line-height: 1.5;
}

.section-header {
    font-size: 2rem;
    font-weight: 700;
    color: #1a3a6c;
    padding-bottom: 0.5rem;
    border-bottom: 3px solid #e63946;
    margin: 2.5rem 0 1.5rem 0;
}

.highlight {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    margin: 1.5rem 0;
    height: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.highlight:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

.stat-box {
    background: linear-gradient(135deg, #1a3a6c 0%, #4a6fa5 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    margin: 1rem 0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.cta-button {
    background-color: #e63946;
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    display: inline-block;
    margin: 1rem auto;
    transition: background-color 0.3s, transform 0.2s;
    text-decoration: none;
    text-align: center;
}

.cta-button:hover {
    background-color: #c1121f;
    transform: translateY(-2px);
    color: white;
    text-decoration: none;
}

.footer {
    background-color: #1a3a6c;
    color: white;
    padding: 2.5rem 1rem;
    text-align: center;
    margin-top: 3rem;
    border-radius: 12px 12px 0 0;
}

.testimonial {
    background-color: white;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    border-left: 4px solid #4a6fa5;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.step-number {
    background-color: #4a6fa5;
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: 1rem;
    flex-shrink: 0;
}

.calculator {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    margin: 2rem 0;
}

.calc-result {
    background-color: white;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 1.5rem;
    border-left: 4px solid #e63946;
}

.seo-content {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

.location-badge {
    display: inline-block;
    background-color: #e6f2ff;
    color: #1a3a6c;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    margin: 0.3rem;
    font-weight: 500;
    font-size: 0.9rem;
}

.stats-container {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding: 2rem;
    border-radius: 12px;
    margin: 2rem 0;
}

.hero-section {
    background: linear-gradient(rgba(26, 58, 108, 0.9), rgba(26, 58, 108, 0.8)), url('https://images.unsplash.com/photo-1558981806-ec527fa84c39?ixlib=rb-4.0.3');
    background-size: cover;
    background-position: center;
    color: white;
    padding: 4rem 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
}

@media (max-width: 768px) {
    .main-header {
        font-size: 2.2rem;
    }
    
    .section-header {
        font-size: 1.7rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Compensation calculator function
def calculate_compensation(injury_type, severity, lost_income, medical_expenses, rehabilitation_costs):
    # Base compensation amounts for different injury types (in GBP)
    injury_compensation = {
        'whiplash': {'mild': 2000, 'moderate': 4000, 'severe': 8000},
        'fracture': {'mild': 4000, 'moderate': 9000, 'severe': 16000},
        'head_injury': {'mild': 3000, 'moderate': 12000, 'severe': 25000},
        'back_injury': {'mild': 3500, 'moderate': 10000, 'severe': 20000},
        'soft_tissue': {'mild': 1500, 'moderate': 3500, 'severe': 6000}
    }
    
    # Calculate base compensation
    base_comp = injury_compensation.get(injury_type, {}).get(severity, 0)
    
    # Calculate special damages (financial losses)
    special_damages = lost_income + medical_expenses + rehabilitation_costs
    
    # Total compensation (general damages + special damages)
    total_comp = base_comp + special_damages
    
    return base_comp, special_damages, total_comp

# Header section
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="main-header">Motorcycle Accident Claims</h1>
    <p class="subheader">Expert Legal Support for UK Riders | No Win No Fee</p>
    <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" target="_blank" class="cta-button">Free Case Evaluation</a>
</div>
""", unsafe_allow_html=True)

# Stats section
st.markdown('<div class="section-header">Why Choose Our Services?</div>', unsafe_allow_html=True)

stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown("""
        <div class="stat-box">
            <h3 style="margin:0; font-size: 2rem;">98%</h3>
            <p style="margin:0;">Success Rate</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
        <div class="stat-box">
            <h3 style="margin:0; font-size: 2rem;">£50M+</h3>
            <p style="margin:0;">Recovered for Clients</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
        <div class="stat-box">
            <h3 style="margin:0; font-size: 2rem;">15+</h3>
            <p style="margin:0;">Years Experience</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown("""
        <div class="stat-box">
            <h3 style="margin:0; font-size: 1.5rem;">No Win No Fee</h3>
            <p style="margin:0;">Policy</p>
        </div>
    """, unsafe_allow_html=True)

# Compensation Calculator
st.markdown('<div class="section-header">Compensation Calculator</div>', unsafe_allow_html=True)
st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <p>Use our calculator to get an estimate of how much compensation you might be entitled to after a motorcycle accident.</p>
    </div>
""", unsafe_allow_html=True)

calculator_col1, calculator_col2 = st.columns(2)

with calculator_col1:
    injury_type = st.selectbox(
        "Type of Injury",
        ("whiplash", "fracture", "head_injury", "back_injury", "soft_tissue"),
        help="Select the primary injury you sustained"
    )
    
    severity = st.select_slider(
        "Severity of Injury",
        options=["mild", "moderate", "severe"],
        help="How severe was your injury?"
    )
    
    lost_income = st.number_input(
        "Lost Income (£)",
        min_value=0,
        max_value=100000,
        value=0,
        step=500,
        help="Approximate income you've lost due to the accident"
    )

with calculator_col2:
    medical_expenses = st.number_input(
        "Medical Expenses (£)",
        min_value=0,
        max_value=50000,
        value=0,
        step=250,
        help="Cost of medical treatment related to your accident"
    )
    
    rehabilitation_costs = st.number_input(
        "Rehabilitation Costs (£)",
        min_value=0,
        max_value=30000,
        value=0,
        step=250,
        help="Cost of ongoing rehabilitation or therapy"
    )
    
    # Calculate compensation when button is clicked
    if st.button("Calculate Compensation", use_container_width=True, type="primary"):
        with st.spinner("Calculating your estimated compensation..."):
            time.sleep(1.5)  # Simulate processing time
            base_comp, special_damages, total_comp = calculate_compensation(
                injury_type, severity, lost_income, medical_expenses, rehabilitation_costs
            )
            
            st.markdown(f"""
                <div class="calc-result">
                    <h3 style="text-align: center; color: #1a3a6c;">Estimated Compensation</h3>
                    <p style="text-align: center; font-size: 2.5rem; font-weight: bold; color: #e63946;">£{total_comp:,.0f}</p>
                    <div style="background-color: #f8f9fa; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <p><strong>Breakdown:</strong></p>
                        <p>Injury Compensation: £{base_comp:,.0f}</p>
                        <p>Financial Losses: £{special_damages:,.0f}</p>
                    </div>
                    <p style="text-align: center; margin-top: 1rem; font-style: italic; font-size: 0.9rem;">
                        This is an estimate. Actual compensation may vary based on your specific circumstances.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# Services section
st.markdown('<div class="section-header">Our Services</div>', unsafe_allow_html=True)
services_col1, services_col2, services_col3 = st.columns(3)

with services_col1:
    st.markdown("""
        <div class="highlight">
            <h3>🩺 Personal Injury Claims</h3>
            <p>Compensation for injuries sustained in motorcycle accidents, including whiplash, fractures, and more serious injuries.</p>
        </div>
    """, unsafe_allow_html=True)

with services_col2:
    st.markdown("""
        <div class="highlight">
            <h3>🔧 Vehicle Repair Costs</h3>
            <p>Recover the costs of repairing or replacing your motorcycle and any damaged equipment or clothing.</p>
        </div>
    """, unsafe_allow_html=True)

with services_col3:
    st.markdown("""
        <div class="highlight">
            <h3>💰 Financial Loss Recovery</h3>
            <p>Claim for lost earnings, medical expenses, and other financial impacts resulting from your accident.</p>
        </div>
    """, unsafe_allow_html=True)

# SEO-optimized content for UK audience
st.markdown('<div class="section-header">Motorcycle Accident Claims in the UK</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="seo-content">
        <h3>Expert Legal Support for Motorcyclists Across the United Kingdom</h3>
        <p>If you've been involved in a motorcycle accident in <strong>London, Manchester, Birmingham, Glasgow, Cardiff, Edinburgh, Leeds, Liverpool, Bristol,</strong> or anywhere else in the UK, our specialist solicitors can help you claim the compensation you deserve.</p>
        
        <h4>Understanding UK Motorcycle Accident Claims</h4>
        <p>In the United Kingdom, motorcycle riders have the same rights to compensation as other road users when involved in accidents that weren't their fault. The UK legal system allows claims for:</p>
        <ul>
            <li>General damages (compensation for pain, suffering, and loss of amenity)</li>
            <li>Special damages (financial losses including medical expenses, lost earnings, and travel costs)</li>
            <li>Future losses (ongoing care costs, future lost earnings, and future medical treatment)</li>
        </ul>
        
        <h4>Why Choose Our UK-Based Legal Team?</h4>
        <p>Our solicitors specialize exclusively in motorcycle accident claims across England, Scotland, Wales, and Northern Ireland. We understand the unique challenges faced by motorcyclists on UK roads and have extensive experience dealing with UK insurance companies and the court system.</p>
        
        <div style="text-align: center; margin: 1.5rem 0;">
            <span class="location-badge">London</span>
            <span class="location-badge">Manchester</span>
            <span class="location-badge">Birmingham</span>
            <span class="location-badge">Glasgow</span>
            <span class="location-badge">Cardiff</span>
            <span class="location-badge">Edinburgh</span>
            <span class="location-badge">Leeds</span>
            <span class="location-badge">Liverpool</span>
            <span class="location-badge">Bristol</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Process section
st.markdown('<div class="section-header">Our Simple Process</div>', unsafe_allow_html=True)

process_col1, process_col2, process_col3, process_col4 = st.columns(4)

with process_col1:
    st.markdown("""
        <div style="display: flex; align-items: flex-start; margin-bottom: 2rem;">
            <div class="step-number">1</div>
            <div>
                <h3 style="margin-top: 0;">Contact Us</h3>
                <p>Reach out for a free initial consultation to discuss your case.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with process_col2:
    st.markdown("""
        <div style="display: flex; align-items: flex-start; margin-bottom: 2rem;">
            <div class="step-number">2</div>
            <div>
                <h3 style="margin-top: 0;">Case Evaluation</h3>
                <p>Our experts will assess the merits of your claim and advise on the best approach.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with process_col3:
    st.markdown("""
        <div style="display: flex; align-items: flex-start; margin-bottom: 2rem;">
            <div class="step-number">3</div>
            <div>
                <h3 style="margin-top: 0;">Claim Progression</h3>
                <p>We handle all paperwork and negotiations on your behalf.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with process_col4:
    st.markdown("""
        <div style="display: flex; align-items: flex-start; margin-bottom: 2rem;">
            <div class="step-number">4</div>
            <div>
                <h3 style="margin-top: 0;">Resolution</h3>
                <p>We work to secure the maximum compensation you're entitled to.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Testimonials
st.markdown('<div class="section-header">Client Testimonials</div>', unsafe_allow_html=True)

testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.markdown("""
        <div class="testimonial">
            <p style="font-style: italic;">"After my motorcycle accident in London, I was overwhelmed with medical bills and insurance paperwork. 
            The team handled everything professionally and secured me a settlement that covered all my expenses 
            and lost income. I couldn't be happier with the service."</p>
            <p><strong>- James R., London</strong></p>
        </div>
    """, unsafe_allow_html=True)

with testimonial_col2:
    st.markdown("""
        <div class="testimonial">
            <p style="font-style: italic;">"I was hesitant to make a claim after my accident in Manchester, but I'm so glad I contacted these specialists. 
            They were compassionate, knowledgeable, and fought hard to get me the compensation I deserved. 
            Highly recommended for any motorcyclist needing legal support in the UK."</p>
            <p><strong>- Sarah L., Manchester</strong></p>
        </div>
    """, unsafe_allow_html=True)

# CTA section
st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem; background: linear-gradient(135deg, #1a3a6c 0%, #4a6fa5 100%); color: white; border-radius: 12px; margin: 2rem 0;">
        <h2 style="color: white; margin-bottom: 1.5rem;">Start Your Claim Today</h2>
        <p style="font-size: 1.2rem; margin-bottom: 2rem;">Contact us for a free, no-obligation consultation to discuss your motorcycle accident claim.</p>
        <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" target="_blank" class="cta-button" style="background-color: #e63946; color: white;">Free Case Evaluation</a>
    </div>
""", unsafe_allow_html=True)

# Footer with do-follow link
st.markdown("""
    <div class="footer">
        <p style="font-size: 1.1rem; font-weight: 600;">© 2023 Motorcycle Accident Claims Specialist | All Rights Reserved</p>
        <p style="margin: 1rem 0;">This site provides general information about motorcycle accident claims. For specialized legal advice regarding your situation, please contact us directly.</p>
        <p style="margin: 1rem 0;">Return to <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" style="color: #4cc9f0; text-decoration: none; font-weight: 600;" rel="dofollow">Motorcycle Accident Claims</a> at Advice.co.uk</p>
        <p style="margin: 1rem 0;">Regulated by the Solicitors Regulation Authority (SRA)</p>
        <p>Office locations: London | Manchester | Birmingham | Glasgow | Cardiff</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
