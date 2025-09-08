import streamlit as st
import streamlit.components.v1 as components
import requests
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Motorcycle Accident Claims | Expert Solicitors | No Win No Fee",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling - embedded directly
def local_css():
    st.markdown("""
    <style>
        /* CSS Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --primary-blue: #1A3A5F;
            --secondary-blue: #0078D4;
            --accent-orange: #FF6B00;
            --light-gray: #F5F7FA;
            --white: #FFFFFF;
            --text-dark: #333333;
            --text-light: #666666;
            --border-light: #E0E0E0;
            --shadow: 0 4px 12px rgba(0,0,0,0.08);
            --transition: all 0.3s ease;
        }
        
        body {
            font-family: 'Open Sans', sans-serif;
            color: var(--text-dark);
            line-height: 1.6;
            overflow-x: hidden;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            line-height: 1.3;
            margin-bottom: 1rem;
        }
        
        h1 {
            font-size: 3rem;
            font-weight: 700;
        }
        
        h2 {
            font-size: 2.2rem;
        }
        
        h3 {
            font-size: 1.5rem;
        }
        
        a {
            text-decoration: none;
            color: var(--secondary-blue);
            transition: var(--transition);
        }
        
        a:hover {
            color: var(--accent-orange);
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .btn {
            display: inline-block;
            padding: 14px 28px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            text-align: center;
        }
        
        .btn-primary {
            background-color: var(--accent-orange);
            color: white;
        }
        
        .btn-primary:hover {
            background-color: #e55a00;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(255, 107, 0, 0.2);
        }
        
        .btn-secondary {
            background-color: white;
            color: var(--secondary-blue);
            border: 2px solid var(--secondary-blue);
        }
        
        .btn-secondary:hover {
            background-color: var(--secondary-blue);
            color: white;
        }
        
        .btn-outline {
            background-color: transparent;
            color: var(--accent-orange);
            border: 2px solid var(--accent-orange);
        }
        
        .btn-outline:hover {
            background-color: var(--accent-orange);
            color: white;
        }
        
        /* Header Styles */
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
            padding: 15px 0;
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 1.8rem;
            color: var(--primary-blue);
        }
        
        .logo span {
            color: var(--accent-orange);
        }
        
        .nav-menu {
            display: flex;
            list-style: none;
        }
        
        .nav-menu li {
            margin-left: 30px;
        }
        
        .nav-menu a {
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
            color: var(--primary-blue);
            font-size: 1rem;
        }
        
        .nav-menu a:hover {
            color: var(--accent-orange);
        }
        
        .header-contact {
            display: flex;
            align-items: center;
        }
        
        .header-phone {
            display: flex;
            align-items: center;
            margin-right: 20px;
            font-weight: 600;
            color: var(--primary-blue);
        }
        
        .header-phone i {
            margin-right: 8px;
            color: var(--accent-orange);
        }
        
        .mobile-toggle {
            display: none;
            font-size: 1.5rem;
            color: var(--primary-blue);
            cursor: pointer;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(26, 58, 95, 0.85), rgba(26, 58, 95, 0.85)), url('https://images.unsplash.com/photo-1558981285-6f0ce9c8cf54?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80') center/cover no-repeat;
            color: white;
            padding: 180px 0 100px;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            color: white;
        }
        
        .hero p {
            font-size: 1.3rem;
            max-width: 800px;
            margin: 0 auto 2.5rem;
            color: rgba(255, 255, 255, 0.9);
        }
        
        .hero-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        
        /* Trust Indicators */
        .trust-indicators {
            background-color: var(--light-gray);
            padding: 30px 0;
            border-bottom: 1px solid var(--border-light);
        }
        
        .trust-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .trust-item {
            display: flex;
            align-items: center;
        }
        
        .trust-item i {
            font-size: 2rem;
            margin-right: 15px;
            color: var(--accent-orange);
        }
        
        .trust-item h4 {
            font-size: 1.1rem;
            margin-bottom: 0;
        }
        
        .trust-item p {
            font-size: 0.9rem;
            color: var(--text-light);
        }
        
        /* Section Styles */
        section {
            padding: 80px 0;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .section-title h2 {
            color: var(--primary-blue);
            position: relative;
            display: inline-block;
        }
        
        .section-title h2:after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 3px;
            background-color: var(--accent-orange);
        }
        
        /* Introduction Section */
        .intro {
            background-color: white;
        }
        
        .intro-content {
            display: flex;
            align-items: center;
            gap: 50px;
        }
        
        .intro-text {
            flex: 1;
        }
        
        .intro-image {
            flex: 1;
        }
        
        .intro-image img {
            width: 100%;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }
        
        .benefits {
            margin-top: 30px;
        }
        
        .benefits ul {
            list-style: none;
        }
        
        .benefits li {
            padding: 12px 0;
            border-bottom: 1px solid var(--border-light);
            display: flex;
            align-items: center;
        }
        
        .benefits li i {
            margin-right: 15px;
            color: var(--accent-orange);
            font-size: 1.2rem;
        }
        
        /* Eligibility Section */
        .eligibility {
            background-color: var(--light-gray);
        }
        
        .eligibility-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .eligibility-card {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: var(--shadow);
            text-align: center;
            transition: var(--transition);
        }
        
        .eligibility-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        
        .eligibility-card i {
            font-size: 3rem;
            color: var(--accent-orange);
            margin-bottom: 20px;
        }
        
        .eligibility-card h3 {
            color: var(--primary-blue);
            margin-bottom: 15px;
        }
        
        /* Compensation Calculator */
        .compensation {
            background-color: white;
        }
        
        .calculator {
            background-color: var(--light-gray);
            padding: 40px;
            border-radius: 8px;
            margin-top: 40px;
        }
        
        .calculator-tabs {
            display: flex;
            border-bottom: 2px solid var(--border-light);
            margin-bottom: 30px;
        }
        
        .calculator-tab {
            padding: 15px 25px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: var(--transition);
        }
        
        .calculator-tab.active {
            color: var(--accent-orange);
            border-bottom-color: var(--accent-orange);
        }
        
        .calculator-content {
            display: none;
        }
        
        .calculator-content.active {
            display: block;
        }
        
        .compensation-range {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 30px 0;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        .compensation-min, .compensation-max {
            text-align: center;
        }
        
        .compensation-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary-blue);
            margin-bottom: 5px;
        }
        
        .compensation-label {
            color: var(--text-light);
            font-size: 0.9rem;
        }
        
        .compensation-arrow {
            font-size: 2rem;
            color: var(--accent-orange);
        }
        
        .disclaimer {
            font-size: 0.9rem;
            color: var(--text-light);
            margin-top: 20px;
            font-style: italic;
        }
        
        /* Financial Losses Section */
        .financial {
            background-color: var(--light-gray);
        }
        
        .financial-items {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .financial-item {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: var(--shadow);
            text-align: center;
            transition: var(--transition);
        }
        
        .financial-item:hover {
            background-color: var(--primary-blue);
            color: white;
        }
        
        .financial-item:hover i {
            color: white;
        }
        
        .financial-item i {
            font-size: 2.5rem;
            color: var(--accent-orange);
            margin-bottom: 20px;
        }
        
        /* Time Limits Section */
        .timeline {
            background-color: white;
        }
        
        .timeline-container {
            position: relative;
            margin-top: 40px;
        }
        
        .timeline-line {
            position: absolute;
            left: 50%;
            top: 0;
            height: 100%;
            width: 4px;
            background-color: var(--border-light);
            transform: translateX(-50%);
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 50px;
        }
        
        .timeline-content {
            background-color: var(--light-gray);
            padding: 25px;
            border-radius: 8px;
            width: 45%;
            box-shadow: var(--shadow);
        }
        
        .timeline-item:nth-child(odd) .timeline-content {
            margin-left: auto;
        }
        
        .timeline-dot {
            position: absolute;
            left: 50%;
            top: 30px;
            width: 20px;
            height: 20px;
            background-color: var(--accent-orange);
            border-radius: 50%;
            transform: translateX(-50%);
        }
        
        .timeline-date {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            color: var(--accent-orange);
            margin-bottom: 10px;
        }
        
        /* Evidence Section */
        .evidence {
            background: linear-gradient(rgba(26, 58, 95, 0.9), rgba(26, 58, 95, 0.9)), url('https://images.unsplash.com/photo-1554224154-260325b9e8b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80') center/cover no-repeat;
            color: white;
        }
        
        .evidence-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }
        
        .evidence-item {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 8px;
            backdrop-filter: blur(5px);
            transition: var(--transition);
        }
        
        .evidence-item:hover {
            background-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-5px);
        }
        
        .evidence-item i {
            font-size: 2rem;
            margin-bottom: 15px;
            color: var(--accent-orange);
        }
        
        /* Examples Section */
        .examples {
            background-color: var(--light-gray);
        }
        
        .example-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .example-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }
        
        .example-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }
        
        .example-image {
            height: 200px;
            overflow: hidden;
        }
        
        .example-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }
        
        .example-card:hover .example-image img {
            transform: scale(1.1);
        }
        
        .example-content {
            padding: 25px;
        }
        
        .example-content h3 {
            color: var(--primary-blue);
            margin-bottom: 15px;
        }
        
        /* Process Section */
        .process {
            background-color: white;
        }
        
        .process-steps {
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
            position: relative;
        }
        
        .process-steps:after {
            content: '';
            position: absolute;
            top: 40px;
            left: 10%;
            right: 10%;
            height: 4px;
            background-color: var(--border-light);
            z-index: 1;
        }
        
        .process-step {
            position: relative;
            z-index: 2;
            text-align: center;
            width: 20%;
        }
        
        .step-number {
            width: 80px;
            height: 80px;
            background-color: var(--primary-blue);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: 700;
            margin: 0 auto 20px;
        }
        
        .step-title {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            margin-bottom: 10px;
            color: var(--primary-blue);
        }
        
        /* How We Help Section */
        .help {
            background-color: var(--light-gray);
        }
        
        .help-content {
            display: flex;
            align-items: center;
            gap: 50px;
        }
        
        .help-image {
            flex: 1;
        }
        
        .help-image img {
            width: 100%;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }
        
        .help-text {
            flex: 1;
        }
        
        .help-list {
            list-style: none;
            margin: 25px 0;
        }
        
        .help-list li {
            padding: 12px 0;
            display: flex;
            align-items: center;
        }
        
        .help-list li i {
            margin-right: 15px;
            color: var(--accent-orange);
            font-size: 1.2rem;
        }
        
        .no-fee-box {
            background-color: var(--primary-blue);
            color: white;
            padding: 25px;
            border-radius: 8px;
            margin-top: 30px;
        }
        
        .no-fee-box h3 {
            color: white;
            margin-bottom: 15px;
        }
        
        /* Contact Section */
        .contact {
            background-color: var(--primary-blue);
            color: white;
            padding: 80px 0;
        }
        
        .contact h2 {
            color: white;
        }
        
        .contact-options {
            display: flex;
            justify-content: space-between;
            gap: 30px;
            margin-top: 40px;
        }
        
        .contact-option {
            flex: 1;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 8px;
            text-align: center;
            transition: var(--transition);
        }
        
        .contact-option:hover {
            background-color: rgba(255, 255, 255, 0.2);
        }
        
        .contact-option i {
            font-size: 3rem;
            margin-bottom: 20px;
            color: var(--accent-orange);
        }
        
        .contact-option h3 {
            color: white;
            margin-bottom: 15px;
        }
        
        .contact-phone {
            font-size: 1.8rem;
            font-weight: 700;
            color: white;
            margin: 15px 0;
        }
        
        .contact-form {
            margin-top: 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 4px;
            font-family: 'Open Sans', sans-serif;
            font-size: 1rem;
        }
        
        .form-group textarea {
            resize: vertical;
            min-height: 120px;
        }
        
        /* Footer */
        footer {
            background-color: #0a192f;
            color: rgba(255, 255, 255, 0.7);
            padding: 60px 0 30px;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }
        
        .footer-column h3 {
            color: white;
            margin-bottom: 20px;
            font-size: 1.3rem;
        }
        
        .footer-column ul {
            list-style: none;
        }
        
        .footer-column ul li {
            margin-bottom: 12px;
        }
        
        .footer-column ul li a {
            color: rgba(255, 255, 255, 0.7);
            transition: var(--transition);
        }
        
        .footer-column ul li a:hover {
            color: var(--accent-orange);
        }
        
        .footer-bottom {
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 30px;
            text-align: center;
            font-size: 0.9rem;
        }
        
        /* Responsive Styles */
        @media (max-width: 992px) {
            h1 {
                font-size: 2.8rem;
            }
            
            h2 {
                font-size: 1.8rem;
            }
            
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .hero p {
                font-size: 1.1rem;
            }
            
            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .intro-content,
            .help-content {
                flex-direction: column;
            }
            
            .timeline-line {
                left: 30px;
            }
            
            .timeline-content {
                width: calc(100% - 60px);
                margin-left: 60px !important;
            }
            
            .timeline-dot {
                left: 30px;
            }
            
            .process-steps {
                flex-direction: column;
                align-items: center;
            }
            
            .process-steps:after {
                display: none;
            }
            
            .process-step {
                width: 100%;
                margin-bottom: 30px;
            }
            
            .contact-options {
                flex-direction: column;
            }
        }
        
        @media (max-width: 768px) {
            .nav-menu {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background-color: white;
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
                padding-top: 50px;
                transition: var(--transition);
            }
            
            .nav-menu.active {
                left: 0;
            }
            
            .nav-menu li {
                margin: 0 0 30px 0;
            }
            
            .header-contact {
                display: none;
            }
            
            .mobile-toggle {
                display: block;
            }
            
            .trust-container {
                flex-direction: column;
                gap: 20px;
            }
            
            .timeline-line {
                display: none;
            }
            
            .timeline-content {
                width: 100%;
                margin-left: 0 !important;
            }
            
            .timeline-dot {
                display: none;
            }
        }
        
        @media (max-width: 576px) {
            h1 {
                font-size: 2.2rem;
            }
            
            h2 {
                font-size: 1.5rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
            
            .btn {
                padding: 12px 20px;
                font-size: 0.9rem;
            }
            
            .section-title h2:after {
                width: 40px;
            }
            
            .calculator-tabs {
                flex-direction: column;
                border-bottom: none;
            }
            
            .calculator-tab {
                border-bottom: 1px solid var(--border-light);
                padding: 12px;
            }
            
            .compensation-range {
                flex-direction: column;
                gap: 20px;
            }
            
            .compensation-arrow {
                transform: rotate(90deg);
            }
        }
        
        /* Streamlit-specific adjustments */
        .stTabs {
            margin-bottom: 30px;
        }
        
        .stTextInput > div > div > input {
            padding: 15px;
            border-radius: 4px;
        }
        
        .stTextArea > div > div > textarea {
            padding: 15px;
            border-radius: 4px;
            min-height: 120px;
        }
    </style>
    """, unsafe_allow_html=True)

# Header section
def header():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown("""
        <div class="logo">
            Advice<span>.co.uk</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <ul class="nav-menu">
            <li><a href="https://www.advice.co.uk/">Home</a></li>
            <li><a href="https://www.advice.co.uk/">Services</a></li>
            <li><a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims">Motorcycle Accident Claims</a></li>
            <li><a href="https://www.advice.co.uk/contact-us">Contact</a></li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="header-contact">
            <div class="header-phone">
                <i class="fas fa-phone-alt"></i>
                <span>0161 696 9685</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("[Get Free Advice](https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims)", unsafe_allow_html=True)

# Hero section
def hero_section():
    st.markdown("""
    <section class="hero">
        <div class="container">
            <h1>Expert Motorcycle Accident Claims Solicitors</h1>
            <p>Maximum Compensation. 100% No Win No Fee. Free Advice 24/7.</p>
            <div class="hero-buttons">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Get Free Advice Now</a>
                <a href="tel:01616969685" class="btn btn-secondary">Call Us: 0161 696 9685</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Trust indicators section
def trust_indicators():
    st.markdown("""
    <section class="trust-indicators">
        <div class="container">
            <div class="trust-container">
                <div class="trust-item">
                    <i class="fas fa-certificate"></i>
                    <div>
                        <h4>Authorised and Regulated</h4>
                        <p>By the Financial Conduct Authority</p>
                    </div>
                </div>
                <div class="trust-item">
                    <i class="fas fa-clock"></i>
                    <div>
                        <h4>24/7 Free Advice</h4>
                        <p>Available 7 days a week</p>
                    </div>
                </div>
                <div class="trust-item">
                    <i class="fas fa-shield-alt"></i>
                    <div>
                        <h4>No Win No Fee Guarantee</h4>
                        <p>No upfront costs required</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Introduction section
def introduction_section():
    st.markdown("""
    <section class="intro">
        <div class="container">
            <div class="section-title">
                <h2>Your Guide to Motorcycle Accident Claims</h2>
            </div>
            <div class="intro-content">
                <div class="intro-text">
                    <p>If you've been injured in a motorcycle accident that wasn't your fault, you may be entitled to compensation. Our expert solicitors specialize in <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims">motorcycle accident claims</a> and can help you get the compensation you deserve.</p>
                    <p>Being involved in a road accident can affect your life financially, physically, and mentally, but deciding to claim could help you move forward. Our panel of solicitors will guide you through the entire process with expert advice and support.</p>
                    <p>With years of experience handling <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims">motorcycle injury claims</a>, we understand the unique challenges faced by motorcyclists on the road. We're committed to ensuring you receive the maximum compensation for your injuries and financial losses.</p>
                    <div class="benefits">
                        <ul>
                            <li><i class="fas fa-check-circle"></i> Expert legal advice from specialist solicitors</li>
                            <li><i class="fas fa-check-circle"></i> 100% No Win No Fee service</li>
                            <li><i class="fas fa-check-circle"></i> Maximum compensation for your injuries</li>
                            <li><i class="fas fa-check-circle"></i> Free advice with no obligation</li>
                        </ul>
                    </div>
                    <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Learn More About Motorcycle Accident Claims</a>
                </div>
                <div class="intro-image">
                    <img src="https://images.unsplash.com/photo-1583121274602-3e2820c69888?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Motorcycle accident claim">
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Eligibility section
def eligibility_section():
    st.markdown("""
    <section class="eligibility">
        <div class="container">
            <div class="section-title">
                <h2>Who Can Make Motorcycle Accident Claims?</h2>
            </div>
            <p>If you suffered harm in a motorcycle accident due to a breached duty of care, you could be eligible to claim. The eligibility criteria are:</p>
            <div class="eligibility-cards">
                <div class="eligibility-card">
                    <i class="fas fa-handshake"></i>
                    <h3>Duty of Care Owed</h3>
                    <p>You were owed a duty of care by another road user. All road users have a legal obligation to take reasonable steps to ensure your safety.</p>
                </div>
                <div class="eligibility-card">
                    <i class="fas fa-exclamation-triangle"></i>
                    <h3>Breach of Duty</h3>
                    <p>This duty of care was breached by the other party through negligent or reckless behavior such as speeding, distraction, or failing to follow road rules.</p>
                </div>
                <div class="eligibility-card">
                    <i class="fas fa-user-injured"></i>
                    <h3>Harm Suffered</h3>
                    <p>You suffered harm as a result of this breach, including physical injuries, psychological trauma, or financial losses due to the accident.</p>
                </div>
            </div>
            <div style="text-align: center; margin-top: 40px;">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Check Your Eligibility Now</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Compensation calculator section
def compensation_calculator():
    st.markdown("""
    <section class="compensation">
        <div class="container">
            <div class="section-title">
                <h2>What Motorcycle Accident Compensation Could I Get?</h2>
            </div>
            <p>Compensation amounts vary based on the severity of your injuries and other factors. Use our calculator to see potential compensation ranges for <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims">motorcycle collision claims</a>:</p>
    """, unsafe_allow_html=True)
    
    # Enhanced compensation calculator with interactive tabs
    calculator_tabs = st.tabs(["Head Injuries", "Back Injuries", "Neck Injuries", "Leg Injuries"])
    
    with calculator_tabs[0]:
        st.markdown("""
        <h3>Head Injury Compensation</h3>
        <div class="compensation-range">
            <div class="compensation-min">
                <div class="compensation-value">£344,150</div>
                <div class="compensation-label">Minimum</div>
            </div>
            <div class="compensation-arrow">→</div>
            <div class="compensation-max">
                <div class="compensation-value">£493,000</div>
                <div class="compensation-label">Maximum</div>
            </div>
        </div>
        <p>For very severe brain and head injuries resulting in double incontinence, little ability to follow basic commands, and full-time nursing care required. This includes traumatic brain injuries that significantly impact quality of life and cognitive function.</p>
        """, unsafe_allow_html=True)
    
    with calculator_tabs[1]:
        st.markdown("""
        <h3>Back Injury Compensation</h3>
        <div class="compensation-range">
            <div class="compensation-min">
                <div class="compensation-value">£90,510</div>
                <div class="compensation-label">Minimum</div>
            </div>
            <div class="compensation-arrow">→</div>
            <div class="compensation-max">
                <div class="compensation-value">£196,450</div>
                <div class="compensation-label">Maximum</div>
            </div>
        </div>
        <p>For severe back injuries including damage to the spinal cord and nerve roots causing ongoing serious disability. These injuries often result in chronic pain, limited mobility, and may require surgery or long-term treatment.</p>
        """, unsafe_allow_html=True)
    
    with calculator_tabs[2]:
        st.markdown("""
        <h3>Neck Injury Compensation</h3>
        <div class="compensation-range">
            <div class="compensation-min">
                <div class="compensation-value">£80,240</div>
                <div class="compensation-label">Minimum</div>
            </div>
            <div class="compensation-arrow">→</div>
            <div class="compensation-max">
                <div class="compensation-value">£181,020</div>
                <div class="compensation-label">Maximum</div>
            </div>
        </div>
        <p>For severe neck injuries including incomplete paraplegia or permanent spastic quadriparesis. These injuries can severely impact daily activities, work capabilities, and overall quality of life.</p>
        """, unsafe_allow_html=True)
    
    with calculator_tabs[3]:
        st.markdown("""
        <h3>Leg Injury Compensation</h3>
        <div class="compensation-range">
            <div class="compensation-min">
                <div class="compensation-value">£66,920</div>
                <div class="compensation-label">Minimum</div>
            </div>
            <div class="compensation-arrow">→</div>
            <div class="compensation-max">
                <div class="compensation-value">£165,860</div>
                <div class="compensation-label">Maximum</div>
            </div>
        </div>
        <p>For the most serious leg injuries short of amputation, including extensive degloving or other extremely serious injuries. These injuries often result in permanent mobility issues and may require multiple surgeries.</p>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <p class="disclaimer">These figures are based on the Judicial College Guidelines and should be used as guidance only. Actual compensation amounts may vary based on individual circumstances. For a personalized assessment, speak to one of our advisors about your <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims">motorbike accident compensation</a> case.</p>
        
        <div style="text-align: center; margin-top: 30px;">
            <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Get Your Personalized Estimate</a>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Financial losses section
def financial_losses():
    st.markdown("""
    <section class="financial">
        <div class="container">
            <div class="section-title">
                <h2>Can Motorbike Accident Claims Payout For Financial Losses?</h2>
            </div>
            <p>Yes – the special damages you are awarded as part of your motorcycle accident compensation will compensate you financially. You can claim special damages for:</p>
            
            <div class="financial-items">
                <div class="financial-item">
                    <i class="fas fa-briefcase"></i>
                    <h3>Loss of Earnings</h3>
                    <p>If you have had to take time off work or leave your job completely. This includes both past and future lost earnings.</p>
                </div>
                <div class="financial-item">
                    <i class="fas fa-wheelchair"></i>
                    <h3>Mobility Aids</h3>
                    <p>Such as crutches, wheelchairs, or other equipment needed due to your injury. This includes both temporary and permanent aids.</p>
                </div>
                <div class="financial-item">
                    <i class="fas fa-user-nurse"></i>
                    <h3>At-Home Care</h3>
                    <p>Including compensation if loved ones act as carers for you. We can help calculate the value of this care based on professional rates.</p>
                </div>
                <div class="financial-item">
                    <i class="fas fa-hospital"></i>
                    <h3>Medical Treatment</h3>
                    <p>Private medical treatment or other relevant medical costs not covered by the NHS. This includes physiotherapy, counseling, and specialist consultations.</p>
                </div>
                <div class="financial-item">
                    <i class="fas fa-ambulance"></i>
                    <h3>Transportation</h3>
                    <p>Costs for traveling to and from medical appointments. If you can no longer drive, we can claim for alternative transport costs.</p>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Calculate Your Financial Losses</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Time limits section
def time_limits():
    st.markdown("""
    <section class="timeline">
        <div class="container">
            <div class="section-title">
                <h2>What Is The Motorbike Injury Claims Time Limit?</h2>
            </div>
            <p>A 3-year time limit applies to motorcycle accident claims, as outlined in the Limitation Act 1980. This begins on the date of the accident in the majority of cases.</p>
            
            <div class="timeline-container">
                <div class="timeline-line"></div>
                
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="timeline-date">Standard Time Limit</div>
                        <h3>3 Years From Accident Date</h3>
                        <p>For most motorcycle accident claims, you have 3 years from the date of the accident to start your claim. It's important to begin the process as early as possible while evidence is still fresh.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="timeline-date">Exception 1</div>
                        <h3>Claims for Under 18s</h3>
                        <p>If the person injured is under 18, the time limit begins on their 18th birthday, giving them until they turn 21 to make a claim. A litigation friend can claim on their behalf before this date.</p>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="timeline-date">Exception 2</div>
                        <h3>Lack of Mental Capacity</h3>
                        <p>If the person lacks the mental capacity to claim, there is no time limit unless they regain capacity, at which point the 3-year time limit begins. A litigation friend can act on their behalf.</p>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Check If You're Within Time Limit</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Evidence section
def evidence_section():
    st.markdown("""
    <section class="evidence">
        <div class="container">
            <div class="section-title">
                <h2 style="color: white;">What Evidence Will I Need?</h2>
            </div>
            <p>You will need evidence such as CCTV footage, photos, and the contact details of witnesses to make a claim. It needs to prove liability for the injuries you sustained.</p>
            
            <div class="evidence-list">
                <div class="evidence-item">
                    <i class="fas fa-video"></i>
                    <h3>CCTV Footage</h3>
                    <p>Contact the owner within 30 days before footage is deleted. This can include traffic cameras, shop security cameras, or dashcam footage from other vehicles.</p>
                </div>
                <div class="evidence-item">
                    <i class="fas fa-car-crash"></i>
                    <h3>Dash-cam Footage</h3>
                    <p>Especially useful if there was no CCTV in the area. If you have a dashcam, save the footage immediately. If another vehicle has one, try to get their details.</p>
                </div>
                <div class="evidence-item">
                    <i class="fas fa-users"></i>
                    <h3>Witness Details</h3>
                    <p>Phone numbers or email addresses of witnesses to the accident. Independent witnesses can significantly strengthen your claim by providing an unbiased account.</p>
                </div>
                <div class="evidence-item">
                    <i class="fas fa-id-card"></i>
                    <h3>Contact/Insurance Details</h3>
                    <p>Details of the person responsible for the accident. If they don't provide this, take a photo of their license plate and report the accident to the police.</p>
                </div>
                <div class="evidence-item">
                    <i class="fas fa-camera"></i>
                    <h3>Photos and Videos</h3>
                    <p>Visual evidence of injuries, accident scene, or perpetrator. Take photos of vehicle damage, road conditions, weather, and any visible injuries immediately after the accident.</p>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-outline">Download Our Evidence Checklist</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Examples section
def examples_section():
    st.markdown("""
    <section class="examples">
        <div class="container">
            <div class="section-title">
                <h2>Common Examples of Motorcycle Accident Claims</h2>
            </div>
            <p>Motorcycle accidents can happen in many different ways. The examples below show how the duty of care was breached in each situation:</p>
            
            <div class="example-cards">
                <div class="example-card">
                    <div class="example-image">
                        <img src="https://www.advice.co.uk/wp-content/uploads/2025/05/motorcycle-under-car-300x200.jpg" alt="Motorcycle under car">
                    </div>
                    <div class="example-content">
                        <h3>Distracted Driver Collision</h3>
                        <p>A driver is distracted by their phone while on the motorway, causing them to crash into your motorcycle. You suffer a severe head injury and soft tissue injuries due to the crash. The driver breached their duty of care by not paying attention to the road.</p>
                    </div>
                </div>
                
                <div class="example-card">
                    <div class="example-image">
                        <img src="https://www.advice.co.uk/wp-content/uploads/2025/05/motorcycle-on-road-300x200.jpg" alt="Motorcycle on road">
                    </div>
                    <div class="example-content">
                        <h3>Speeding Motorcyclist</h3>
                        <p>A motorcyclist goes over the speed limit on a busy road, causing you to lose balance and fall off your motorcycle. You suffer a broken arm and a fractured collarbone due to the fall. The other motorcyclist breached their duty by exceeding the speed limit.</p>
                    </div>
                </div>
                
                <div class="example-card">
                    <div class="example-image">
                        <img src="https://www.advice.co.uk/wp-content/uploads/2025/05/people-on-road-300x196.jpg" alt="People on road">
                    </div>
                    <div class="example-content">
                        <h3>Dangerous Overtaking</h3>
                        <p>You are side by side with another motorcycle at a junction. It overtakes you by speeding up when it is not safe to do so. Your motorcycle skids and you fall, leading to a fractured ankle and a minor head injury. The other rider breached their duty by dangerous overtaking.</p>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">See More Examples</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Process section
def process_section():
    st.markdown("""
    <section class="process">
        <div class="container">
            <div class="section-title">
                <h2>How Long Will A Motorbike Injury Claim Take?</h2>
            </div>
            <p>The majority of motorbike accident claims are settled within a year. However, a claim can take longer depending on several factors:</p>
            
            <div class="process-steps">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <div class="step-title">Initial Consultation</div>
                    <p>Free advice to assess your claim eligibility. We'll listen to your situation and provide honest feedback on your chances of success.</p>
                </div>
                
                <div class="process-step">
                    <div class="step-number">2</div>
                    <div class="step-title">Gathering Evidence</div>
                    <p>Collecting all necessary documentation including medical records, witness statements, and evidence of financial losses.</p>
                </div>
                
                <div class="process-step">
                    <div class="step-number">3</div>
                    <div class="step-title">Medical Assessment</div>
                    <p>Independent medical evaluation of injuries to understand their severity and long-term impact on your life.</p>
                </div>
                
                <div class="process-step">
                    <div class="step-number">4</div>
                    <div class="step-title">Negotiation</div>
                    <p>Securing the best possible compensation through skilled negotiation with the responsible party's insurers.</p>
                </div>
                
                <div class="process-step">
                    <div class="step-number">5</div>
                    <div class="step-title">Settlement</div>
                    <p>Receiving your compensation payout. Most claims are settled out of court, but we're prepared to take your case to trial if necessary.</p>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary">Start Your Claim Today</a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# How we help section
def how_we_help():
    st.markdown("""
    <section class="help">
        <div class="container">
            <div class="section-title">
                <h2>How Advice Can Help With Your Motorcycle Injury Claim</h2>
            </div>
            
            <div class="help-content">
                <div class="help-image">
                    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Motorcycle accident lawyer">
                </div>
                
                <div class="help-text">
                    <p>If your claim is eligible, our panel of motorbike accident solicitors will ensure you get the settlement you deserve. In addition to negotiating a settlement, our panel of solicitors will:</p>
                    
                    <ul class="help-list">
                        <li><i class="fas fa-file-contract"></i> Explain legal terminology in simple terms so you understand every aspect of your claim</li>
                        <li><i class="fas fa-user-md"></i> Put you in contact with specialists like physiotherapists and medical experts</li>
                        <li><i class="fas fa-comments"></i> Communicate with all relevant parties on your behalf, including insurers and medical professionals</li>
                        <li><i class="fas fa-balance-scale"></i> Advise you on settlement offers to ensure you receive fair compensation</li>
                        <li><i class="fas fa-stethoscope"></i> Arrange an independent medical assessment where necessary to document your injuries</li>
                    </ul>
                    
                    <div class="no-fee-box">
                        <h3>No Win No Fee Claims</h3>
                        <p>Our panel of solicitors take on claims on a No Win No Fee basis via a Conditional Fee Agreement (CFA). This means you don't have to pay solicitor's fees before or during your claim, and you won't need to pay this fee if you do not receive a compensation payout. If your case is successful, a success fee will be deducted from your compensation, but this is legally limited and agreed upon in advance.</p>
                    </div>
                    
                    <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary" style="margin-top: 20px;">Speak to an Advisor</a>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Contact section
def contact_section():
    st.markdown("""
    <section class="contact">
        <div class="container">
            <div class="section-title">
                <h2>Ready to Make Your Claim?</h2>
            </div>
            <p>It's completely free to speak to one of our experienced advisors about road traffic accidents and the claims process.</p>
            
            <div class="contact-options">
                <div class="contact-option">
                    <i class="fas fa-phone-alt"></i>
                    <h3>Call Us Now</h3>
                    <div class="contact-phone">0161 696 9685</div>
                    <p>Our advisors are available 24/7 to provide free advice on your claim</p>
                    <a href="tel:01616969685" class="btn btn-primary" style="margin-top: 20px;">Call Now</a>
                </div>
                
                <div class="contact-option">
                    <i class="fas fa-comments"></i>
                    <h3>Live Chat</h3>
                    <p>Chat with one of our advisors online for instant answers to your questions</p>
                    <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" class="btn btn-primary" style="margin-top: 20px;">Chat With Us Now</a>
                </div>
                
                <div class="contact-option">
                    <i class="fas fa-envelope"></i>
                    <h3>Contact Form</h3>
                    <p>Fill in your details and we'll get back to you as soon as possible</p>
    """, unsafe_allow_html=True)
    
    # Enhanced contact form with Streamlit
    with st.form("contact_form"):
        name = st.text_input("Your Name", key="name")
        phone = st.text_input("Phone Number", key="phone")
        email = st.text_input("Email Address", key="email")
        message = st.text_area("Brief description of your accident", key="message", height=100)
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            # Here you would normally process the form data
            # For demo purposes, we'll just show a success message
            st.success("Thank you for your message. We will contact you shortly.")
            
            # Log the form submission (in a real app, you'd save this to a database)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - New contact form submission: {name}, {phone}, {email}"
            st.write(log_entry)
    
    st.markdown("""
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Footer section
def footer():
    st.markdown("""
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>Advice.co.uk</h3>
                    <p>301 The Tea Factory, St Peter's Square, Liverpool L1 4DQ</p>
                    <p>Email: info@advice.co.uk</p>
                    <p>Phone: 0161 696 9685</p>
                </div>
                
                <div class="footer-column">
                    <h3>Regulatory Information</h3>
                    <p>Advice is a trading name of Velasco Limited. Velasco is a claims management company authorised by the Financial Conduct Authority (FCA).</p>
                    <p>We receive a fee for recommending a solicitor. This fee is not passed on to customers.</p>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 Advice.co.uk. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# Main app function
def main():
    # Load Font Awesome
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)
    
    # Load Google Fonts
    st.markdown('<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap" rel="stylesheet">', unsafe_allow_html=True)
    
    # Apply custom CSS
    local_css()
    
    # Render all sections
    header()
    hero_section()
    trust_indicators()
    introduction_section()
    eligibility_section()
    compensation_calculator()
    financial_losses()
    time_limits()
    evidence_section()
    examples_section()
    process_section()
    how_we_help()
    contact_section()
    footer()

# Run the app
if __name__ == "__main__":
    main()
