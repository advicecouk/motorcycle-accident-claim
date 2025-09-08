import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="Motorcycle Accident Claims Specialist",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Montserrat', sans-serif;
    }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .subheader {
        font-size: 1.8rem;
        font-weight: 600;
        color: #3498db;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        font-size: 2.2rem;
        font-weight: 600;
        color: #2c3e50;
        border-left: 5px solid #e74c3c;
        padding-left: 15px;
        margin: 2.5rem 0 1.5rem 0;
    }
    
    .highlight {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #3498db 0%, #2c3e50 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .cta-button {
        background-color: #e74c3c;
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 5px;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        display: block;
        margin: 2rem auto;
        transition: background-color 0.3s;
    }
    
    .cta-button:hover {
        background-color: #c0392b;
    }
    
    .footer {
        background-color: #2c3e50;
        color: white;
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
    }
    
    .testimonial {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #3498db;
    }
    
    .step-number {
        background-color: #3498db;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<h1 class="main-header">Motorcycle Accident Claims</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subheader">Expert Legal Support for Riders</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <p style="font-size: 1.2rem;">If you've been involved in a motorcycle accident that wasn't your fault, 
            you may be entitled to compensation. Our specialist solicitors are here to help you 
            through the claims process.</p>
        </div>
    """, unsafe_allow_html=True)

# Stats section
st.markdown('<div class="section-header">Why Choose Our Services?</div>', unsafe_allow_html=True)
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown("""
        <div class="stat-box">
            <h3>98%</h3>
            <p>Success Rate</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
        <div class="stat-box">
            <h3>£50M+</h3>
            <p>Recovered for Clients</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
        <div class="stat-box">
            <h3>15+</h3>
            <p>Years Experience</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown("""
        <div class="stat-box">
            <h3>No Win</h3>
            <p>No Fee Policy</p>
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

# Process section
st.markdown('<div class="section-header">Our Simple Process</div>', unsafe_allow_html=True)

process_col1, process_col2, process_col3, process_col4 = st.columns(4)

with process_col1:
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div class="step-number">1</div>
            <h3>Contact Us</h3>
        </div>
        <p>Reach out for a free initial consultation to discuss your case.</p>
    """, unsafe_allow_html=True)

with process_col2:
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div class="step-number">2</div>
            <h3>Case Evaluation</h3>
        </div>
        <p>Our experts will assess the merits of your claim and advise on the best approach.</p>
    """, unsafe_allow_html=True)

with process_col3:
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div class="step-number">3</div>
            <h3>Claim Progression</h3>
        </div>
        <p>We handle all paperwork and negotiations on your behalf.</p>
    """, unsafe_allow_html=True)

with process_col4:
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div class="step-number">4</div>
            <h3>Resolution</h3>
        </div>
        <p>We work to secure the maximum compensation you're entitled to.</p>
    """, unsafe_allow_html=True)

# Testimonials
st.markdown('<div class="section-header">Client Testimonials</div>', unsafe_allow_html=True)

testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.markdown("""
        <div class="testimonial">
            <p>"After my motorcycle accident, I was overwhelmed with medical bills and insurance paperwork. 
            The team handled everything professionally and secured me a settlement that covered all my expenses 
            and lost income. I couldn't be happier with the service."</p>
            <p><strong>- James R., Manchester</strong></p>
        </div>
    """, unsafe_allow_html=True)

with testimonial_col2:
    st.markdown("""
        <div class="testimonial">
            <p>"I was hesitant to make a claim after my accident, but I'm so glad I contacted these specialists. 
            They were compassionate, knowledgeable, and fought hard to get me the compensation I deserved. 
            Highly recommended for any motorcyclist needing legal support."</p>
            <p><strong>- Sarah L., Birmingham</strong></p>
        </div>
    """, unsafe_allow_html=True)

# CTA section
st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem; background-color: #f8f9fa; border-radius: 10px; margin: 2rem 0;">
        <h2 style="color: #2c3e50; margin-bottom: 1.5rem;">Start Your Claim Today</h2>
        <p style="font-size: 1.2rem; margin-bottom: 2rem;">Contact us for a free, no-obligation consultation to discuss your motorcycle accident claim.</p>
        <button class="cta-button" onclick="window.open('https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims', '_blank')">Free Case Evaluation</button>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2023 Motorcycle Accident Claims Specialist | All Rights Reserved</p>
        <p>This site provides general information about motorcycle accident claims. For specialized legal advice regarding your situation, please contact us directly.</p>
        <p>Return to <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" style="color: #3498db; text-decoration: none;">Advice.co.uk Motorcycle Accident Claims</a></p>
    </div>
""", unsafe_allow_html=True)
