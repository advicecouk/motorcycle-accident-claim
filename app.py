<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Motorcycle Accident Claims - No Win No Fee Compensation</title>
    <style>
        :root {
            --primary: #1a4b8c;
            --secondary: #ff6b00;
            --light: #f8f9fa;
            --dark: #343a40;
            --success: #28a745;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        /* Header Styles */
        header {
            background-color: var(--primary);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .nav-menu {
            display: flex;
            list-style: none;
        }
        
        .nav-menu li {
            margin-left: 1.5rem;
        }
        
        .nav-menu a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .nav-menu a:hover {
            color: var(--secondary);
        }
        
        .contact-number {
            background-color: var(--secondary);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 30px;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1549399542-7e82138d0d71?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 5rem 0;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .btn {
            display: inline-block;
            background-color: var(--secondary);
            color: white;
            padding: 1rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            margin: 0.5rem;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: #e55f00;
        }
        
        .btn-outline {
            background-color: transparent;
            border: 2px solid white;
        }
        
        .btn-outline:hover {
            background-color: white;
            color: var(--primary);
        }
        
        /* Features Section */
        .features {
            padding: 4rem 0;
            background-color: var(--light);
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 3rem;
            color: var(--primary);
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .feature-card {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .feature-card i {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }
        
        .feature-card h3 {
            margin-bottom: 1rem;
            color: var(--primary);
        }
        
        /* Compensation Section */
        .compensation {
            padding: 4rem 0;
        }
        
        .comp-table {
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .comp-table th, .comp-table td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .comp-table th {
            background-color: var(--primary);
            color: white;
        }
        
        .comp-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        
        /* Process Section */
        .process {
            padding: 4rem 0;
            background-color: var(--light);
        }
        
        .process-steps {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-top: 2rem;
        }
        
        .step {
            flex: 1;
            min-width: 250px;
            text-align: center;
            padding: 1.5rem;
            position: relative;
        }
        
        .step-number {
            width: 50px;
            height: 50px;
            background-color: var(--primary);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1rem;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        /* CTA Section */
        .cta {
            padding: 4rem 0;
            background-color: var(--primary);
            color: white;
            text-align: center;
        }
        
        .cta h2 {
            margin-bottom: 2rem;
        }
        
        /* Footer */
        footer {
            background-color: var(--dark);
            color: white;
            padding: 3rem 0 1rem;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        
        .footer-links h3 {
            margin-bottom: 1rem;
            color: var(--secondary);
        }
        
        .footer-links ul {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 0.5rem;
        }
        
        .footer-links a {
            color: #ddd;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: var(--secondary);
        }
        
        .copyright {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid #555;
            margin-top: 2rem;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
            }
            
            .nav-menu {
                margin-top: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .nav-menu li {
                margin: 0.5rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
            
            .process-steps {
                flex-direction: column;
            }
            
            .step {
                margin-bottom: 2rem;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-container">
            <div class="logo">Advice.co.uk</div>
            <ul class="nav-menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Claims</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
            <a href="tel:01616969685" class="contact-number">0161 696 9685</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>Motorcycle Accident Claims - No Win No Fee Compensation</h1>
            <p>If you've been injured in a motorcycle accident that wasn't your fault, you could be entitled to compensation. Our expert solicitors are here to help you get what you deserve.</p>
            <div class="hero-buttons">
                <a href="#contact" class="btn">Start Your Claim Now</a>
                <a href="#learn-more" class="btn btn-outline">Learn More</a>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features" id="learn-more">
        <div class="container">
            <h2 class="section-title">Why Choose Us For Your Motorcycle Accident Claims</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <i class="fas fa-gavel"></i>
                    <h3>No Win No Fee</h3>
                    <p>You don't pay anything upfront, and only pay if your claim is successful.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-clock"></i>
                    <h3>24/7 Support</h3>
                    <p>Our team is available around the clock to provide advice and support.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-pound-sign"></i>
                    <h3>Maximize Your Claim</h3>
                    <p>We fight to ensure you receive the maximum compensation you're entitled to.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Compensation Section -->
    <section class="compensation">
        <div class="container">
            <h2 class="section-title">Potential Compensation Amounts</h2>
            <p>Compensation varies based on the severity of your injuries and circumstances. Below are guideline amounts for different types of injuries from motorcycle accidents:</p>
            
            <table class="comp-table">
                <thead>
                    <tr>
                        <th>Type of Injury</th>
                        <th>Compensation Range</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Very Severe Brain and Head Injury</td>
                        <td>£344,150 to £493,000</td>
                    </tr>
                    <tr>
                        <td>Moderately Severe Brain and Head Injury</td>
                        <td>£267,340 to £344,150</td>
                    </tr>
                    <tr>
                        <td>Severe Back Injury</td>
                        <td>£111,150 to £196,450</td>
                    </tr>
                    <tr>
                        <td>Severe Neck Injury</td>
                        <td>£80,240 to £159,770</td>
                    </tr>
                    <tr>
                        <td>Serious Leg Injuries</td>
                        <td>£66,920 to £109,290</td>
                    </tr>
                </tbody>
            </table>
            
            <p>These amounts are guidelines from the Judicial College Guidelines. You may also claim for financial losses including lost earnings, medical expenses, and care costs.</p>
            
            <p>For more detailed information about <a href="https://www.advice.co.uk/road-traffic-accident-claims/motorcycle-accident-claims" style="color: var(--primary); font-weight: bold;">motorcycle accident claims</a>, visit our comprehensive guide.</p>
        </div>
    </section>

    <!-- Process Section -->
    <section class="process">
        <div class="container">
            <h2 class="section-title">Our Simple Claims Process</h2>
            <div class="process-steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Free Consultation</h3>
                    <p>Contact us for a free, no-obligation assessment of your case.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3>Evidence Gathering</h3>
                    <p>We'll help gather all necessary evidence to support your claim.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3>Claim Submission</h3>
                    <p>We handle all paperwork and negotiations on your behalf.</p>
                </div>
                <div class="step">
                    <div class="step-number">4</div>
                    <h3>Compensation</h3>
                    <p>Receive the compensation you deserve for your injuries and losses.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta" id="contact">
        <div class="container">
            <h2>Start Your Motorcycle Accident Claim Today</h2>
            <p>Don't delay - there are time limits for making a claim. Contact us now for free advice.</p>
            <a href="tel:01616969685" class="btn">Call 0161 696 9685</a>
            <p>Open 7 days a week, 24 hours</p>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-links">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h3>Our Services</h3>
                    <ul>
                        <li><a href="#">Motorcycle Accident Claims</a></li>
                        <li><a href="#">Road Traffic Accident Claims</a></li>
                        <li><a href="#">Accident At Work Claims</a></li>
                        <li><a href="#">Medical Negligence</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h3>Contact Us</h3>
                    <ul>
                        <li><i class="fas fa-phone"></i> 0161 696 9685</li>
                        <li><i class="fas fa-envelope"></i> info@advice.co.uk</li>
                        <li><i class="fas fa-map-marker-alt"></i> 301 The Tea Factory, St Peter's Square, Liverpool L1 4DQ</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>© 2025 Advice.co.uk. All Rights Reserved. Advice is a trading name of Velasco Limited.</p>
                <p>Velasco is a claims management company authorised by the Financial Conduct Authority (FCA).</p>
            </div>
        </div>
    </footer>
</body>
</html>
