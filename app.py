import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="Motorcycle Accident Claims: Your Guide To Compensation",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Global styles */
    .main {
        padding: 0;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Navigation */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #1a237e;
        color: white;
        padding: 10px 0;
        z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .nav-container {
        display: flex;
        justify-content: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    .nav-item {
        margin: 0 15px;
        color: white;
        text-decoration: none;
        font-weight: 500;
        padding: 5px 10px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }
    .nav-item:hover {
        background-color: #283593;
        color: white;
    }
    
    /* Hero section */
    .hero {
        background: linear-gradient(rgba(26, 35, 126, 0.8), rgba(26, 35, 126, 0.8)), url('https://images.unsplash.com/photo-1558980663-3685c1d673c4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 120px 20px 80px;
        text-align: center;
        margin-top: 60px;
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        padding: 25px;
        margin: 20px 0;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Buttons */
    .stButton button {
        background-color: #1a237e;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 6px;
        font-weight: 600;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #283593;
        color: white;
    }
    
    /* Contact form */
    .contact-form {
        background-color: #f5f5f5;
        padding: 30px;
        border-radius: 10px;
        margin: 30px 0;
    }
    
    /* Footer */
    .footer {
        background-color: #1a237e;
        color: white;
        padding: 20px;
        text-align: center;
        margin-top: 50px;
    }
    .footer a {
        color: white;
        margin: 0 10px;
        text-decoration: none;
    }
    
    /* Floating button */
    .floating-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #d32f2f;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 25px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        z-index: 999;
        cursor: pointer;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .nav-container {
            flex-wrap: wrap;
        }
        .nav-item {
            margin: 5px;
            font-size: 14px;
        }
        .hero {
            padding: 100px 15px 60px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<div class="navbar">
    <div class="nav-container">
        <a href="#hero" class="nav-item">Home</a>
        <a href="#vulnerable" class="nav-item">Why Vulnerable</a>
        <a href="#eligibility" class="nav-item">Eligibility</a>
        <a href="#compensation" class="nav-item">Compensation</a>
        <a href="#timeline" class="nav-item">Timeline</a>
        <a href="#evidence" class="nav-item">Evidence</a>
        <a href="#process" class="nav-item">Process</a>
        <a href="#support" class="nav-item">Legal Support</a>
        <a href="#contact" class="nav-item">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero" id="hero">
    <h1 style="font-size: 2.8rem; margin-bottom: 20px;">Motorcycle Accident Claims: Your Guide To Compensation</h1>
    <p style="font-size: 1.4rem; margin-bottom: 30px; max-width: 800px; margin-left: auto; margin-right: auto;">
        Understand your rights, the claims process, and how to secure the compensation you deserve after a motorcycle accident.
    </p>
    <a href="https://www.advice.co.uk" target="_blank">
        <button style="background-color: #d32f2f; color: white; border: none; padding: 15px 30px; border-radius: 6px; font-size: 1.1rem; font-weight: 600; cursor: pointer;">
            Get Free Legal Advice
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# Main content container
with st.container():
    col1, col2, col3 = st.columns([1, 8, 1])
    
    with col2:
        # Why Riders Are More Vulnerable
        st.markdown('<div id="vulnerable"></div>', unsafe_allow_html=True)
        with st.expander("### Why Riders Are More Vulnerable", expanded=True):
            st.markdown("""
            Motorcyclists are among the most vulnerable road users. Without the protective shell of a vehicle, 
            riders are exposed to direct impact in collisions. Common injuries tend to be more severe, including:
            
            - Head and brain injuries (even with helmets)
            - Spinal cord damage and paralysis
            - Multiple fractures and broken bones
            - Severe lacerations and road rash
            - Psychological trauma and PTSD
            
            Statistics show that motorcyclists are approximately **38 times more likely** to be killed in a crash 
            than car occupants per mile traveled. This heightened risk underscores the importance of proper 
            compensation when accidents occur due to others' negligence.
            """)
        
        # Do You Have The Right To Claim?
        st.markdown('<div id="eligibility"></div>', unsafe_allow_html=True)
        with st.expander("### Do You Have The Right To Claim?", expanded=False):
            st.markdown("""
            You may have grounds for a compensation claim if your motorcycle accident was caused by:
            
            - Another driver's negligence (careless driving, speeding, etc.)
            - Poor road conditions or defective road maintenance
            - Faulty motorcycle parts or equipment
            - Inadequate signage or road design
            
            **Key eligibility factors:**
            
            1. The accident occurred within the last three years (see time limits)
            2. Another party was wholly or partially at fault
            3. You sustained verifiable injuries or losses
            
            Even if you believe you may have been partially at fault, you could still claim compensation under 
            the principle of "contributory negligence." It's advisable to seek professional legal advice to 
            assess your specific situation.
            """)
        
        # What Could Compensation Include?
        st.markdown('<div id="compensation"></div>', unsafe_allow_html=True)
        with st.expander("### What Could Compensation Include?", expanded=False):
            st.markdown("""
            A successful motorcycle accident claim can provide compensation for:
            
            **General Damages:**
            - Pain and suffering from injuries
            - Psychological trauma and emotional distress
            - Loss of amenity (reduced quality of life)
            
            **Special Damages (financial losses):**
            - Medical expenses (current and future)
            - Loss of earnings and future earning capacity
            - Cost of care and rehabilitation
            - Motorcycle repair or replacement costs
            - Travel expenses to medical appointments
            - Adapted accommodation or vehicle modifications
            
            Compensation amounts vary significantly based on injury severity, impact on your life, 
            and financial losses incurred. Serious injuries leading to long-term disability typically 
            result in higher compensation awards.
            """)
        
        # How Long Do You Have To Claim?
        st.markdown('<div id="timeline"></div>', unsafe_allow_html=True)
        with st.expander("### How Long Do You Have To Claim?", expanded=False):
            st.markdown("""
            In the UK, the standard time limit for personal injury claims is:
            
            **Three years from the accident date**
            
            However, exceptions apply in certain circumstances:
            
            - For children: The three-year limit begins on their 18th birthday
            - For those lacking mental capacity: The time limit may be paused
            - If the injury wasn't immediately apparent: The limit may run from the date of knowledge
            
            While three years might seem ample, starting the process early is strongly recommended. 
            Gathering evidence becomes more difficult with time, and early legal advice can significantly 
            strengthen your case.
            
            Don't assume you have plenty of time - contact a solicitor as soon as you're able after your accident.
            """)
        
        # Gathering Evidence For Your Case
        st.markdown('<div id="evidence"></div>', unsafe_allow_html=True)
        with st.expander("### Gathering Evidence For Your Case", expanded=False):
            st.markdown("""
            Strong evidence is crucial for a successful claim. If possible after an accident, try to collect:
            
            **At the scene:**
            - Photographs of the accident scene, vehicle positions, and road conditions
            - Contact details of any witnesses
            - The other driver's information and insurance details
            - Police incident number (if they attended)
            
            **Medical evidence:**
            - Comprehensive medical reports detailing all injuries
            - Records of all treatments, medications, and therapies
            - Photographs of visible injuries over time
            
            **Financial evidence:**
            - Receipts for all accident-related expenses
            - Documentation of lost income (payslips, employer letters)
            - Records of care costs and other financial impacts
            
            Even if you couldn't gather evidence at the scene, a solicitor can help reconstruct events 
            and collect crucial evidence later through accident reconstruction experts, CCTV footage 
            requests, and witness statements.
            """)
        
        # How Long Might A Claim Take?
        st.markdown('<div id="process"></div>', unsafe_allow_html=True)
        with st.expander("### How Long Might A Claim Take?", expanded=False):
            st.markdown("""
            Claim duration varies significantly based on case complexity:
            
            - **Straightforward cases** (clear liability, minor injuries): 6-12 months
            - **Moderately complex cases** (disputed liability, multiple injuries): 12-24 months
            - **Highly complex cases** (serious injuries, multiple parties, disputed facts): 2-5 years
            
            **Factors affecting timeline:**
            
            1. Liability disputes - if fault is contested, resolution takes longer
            2. Injury severity - serious injuries require longer medical assessment
            3. Defendant response - insurance companies vary in their responsiveness
            4. Court availability - if litigation is necessary, this adds time
            
            Your solicitor can provide a more accurate timeline after evaluating your specific case. 
            While some claims resolve quickly, it's important to prepare for a process that may take 
            considerable time, especially for serious injuries where long-term prognosis needs assessment.
            """)
        
        # Why Many Choose Legal Support
        st.markdown('<div id="support"></div>', unsafe_allow_html=True)
        with st.expander("### Why Many Choose Legal Support", expanded=False):
            st.markdown("""
            Most motorcycle accident claimants benefit from professional legal representation because:
            
            - **Expert knowledge**: Solicitors understand complex personal injury law and procedures
            - **Evidence gathering**: Legal teams know what evidence is needed and how to obtain it
            - **Proper valuation**: Lawyers ensure all damages are identified and properly valued
            - **Negotiation skills**: Experienced negotiators can maximize your compensation
            - **Reduced stress**: Handling the claim process allows you to focus on recovery
            - **No-win, no-fee options**: Many solicitors offer conditional fee agreements
            
            Insurance companies have legal teams working to minimize payouts. Having your own legal 
            representation levels the playing field and significantly increases your chances of 
            receiving full and fair compensation.
            
            Initial consultations are typically free, allowing you to understand your options without 
            financial commitment.
            """)
        
        # Final Thoughts
        with st.expander("### Final Thoughts", expanded=False):
            st.markdown("""
            Being involved in a motorcycle accident can be a life-changing experience with physical, 
            emotional, and financial consequences. Understanding your rights to compensation is an 
            important step toward recovery.
            
            **Key takeaways:**
            
            1. You may have a claim if someone else was at fault for your accident
            2. Time limits apply - generally three years from the accident date
            3. Compensation can cover both physical injuries and financial losses
            4. Professional legal support typically improves outcomes
            
            If you've been involved in a motorcycle accident, don't navigate the complex claims 
            process alone. Seek professional advice to understand your options and ensure your 
            rights are protected.
            
            > *This guide provides general information but does not constitute legal advice. 
            > For advice specific to your situation, consult with a qualified solicitor.*
            """)
        
        # Contact form
        st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
        st.markdown("### Contact Us For a Free Case Assessment")
        st.markdown("Complete the form below and our specialist motorcycle claims team will contact you for a free, no-obligation consultation.")
        
        with st.form("contact_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name*")
            with col2:
                email = st.text_input("Email Address*")
            message = st.text_area("Brief Description of Your Accident*")
            submitted = st.form_submit_button("Submit Inquiry")
            if submitted:
                if name and email and message:
                    st.success("Thank you for your inquiry. We'll contact you within 24 hours.")
                else:
                    st.error("Please complete all required fields.")

# Floating contact button
st.markdown("""
<a href="https://www.advice.co.uk" target="_blank">
    <button class="floating-btn">Contact a Solicitor</button>
</a>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2023 Motorcycle Accident Claims Guide. All rights reserved.</p>
    <div>
        <a href="#">Privacy Policy</a> | 
        <a href="#">Disclaimer</a> | 
        <a href="#">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Smooth scroll JavaScript
components.html("""
<script>
// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if(targetId !== '#') {
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Make navbar sticky
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    } else {
        navbar.style.boxShadow = 'none';
    }
});
</script>
""", height=0)
