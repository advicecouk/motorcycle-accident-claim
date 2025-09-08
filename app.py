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

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS
local_css("style.css")

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
