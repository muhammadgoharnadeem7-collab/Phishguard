import streamlit as st
import re

# Web page ki basic settings
st.set_page_config(page_title="PhishGuard Security Tool", page_icon="🛡️", layout="centered")

# Main Title & Subtitle
st.title("🛡️ PhishGuard: Cyber Safety Analyzer")
st.write("Build by a Future Cyber Security Expert. Protect yourself from digital threats!")

# Sidebar navigation
menu = ["Home", "Password Checker", "Link Analyzer"]
choice = st.sidebar.selectbox("Select Security Tool", menu)

# --- FEATURE 1: PASSWORD CHECKER ---
if choice == "Password Checker":
    st.subheader("🔑 Password Strength Analyzer")
    password = st.text_input("Enter a password to test its security:", type="password")
    
    if password:
        score = 0
        tips = []
        
        if len(password) >= 8: score += 1
        else: tips.append("Length should be at least 8 characters.")
            
        if any(char.isdigit() for char in password): score += 1
        else: tips.append("Add at least one number (0-9).")
            
        if any(char.isupper() for char in password): score += 1
        else: tips.append("Add at least one uppercase letter (A-Z).")
            
        if any(char in "@#$%^&*()_+={}[]|:;<>,.?/~`" for char in password): score += 1
        else: tips.append("Add at least one special character (e.g., @, #, $).")
        
        # Display Results
        if score == 4:
            st.success("🔒 STRONG PASSWORD! This is highly safe from brute-force attacks.")
        elif score == 3:
            st.warning("⚠️ MEDIUM PASSWORD! It could be stronger.")
        else:
            st.error("🚨 WEAK PASSWORD! A hacker can easily crack this.")
            
        if tips:
            st.write("### Security Tips to Improve:")
            for tip in tips:
                st.write(f"- {tip}")

# --- FEATURE 2: LINK ANALYZER ---
elif choice == "Link Analyzer":
    st.subheader("🌐 Phishing & Fake Link Detector")
    url = st.text_input("Paste a URL/Link to analyze:")
    
    if url:
        st.write("Analyzing link structure...")
        is_suspicious = False
        reasons = []
        
        # Check 1: Sensitive keywords in the URL (Common in phishing)
        suspicious_keywords = ["login", "bank", "secure", "update", "free", "gift", "verify", "facebook", "google-login"]
        if any(keyword in url.lower() for keyword in suspicious_keywords):
            is_suspicious = True
            reasons.append("Contains sensitive keywords often used by hackers to mimic real login pages.")
            
        # Check 2: IP address used instead of a standard domain name
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
            is_suspicious = True
            reasons.append("Uses a raw IP address instead of a secure domain name (e.g., google.com).")
            
        # Check 3: Shortened URLs (Often used to hide destination)
        shorteners = ["bit.ly", "goo.gl", "tinyurl.com", "t.co"]
        if any(sh in url.lower() for sch in shorteners):
            is_suspicious = True
            reasons.append("Uses a URL shortener which can mask the final malicious destination.")

        # Final Verdict
        if is_suspicious:
            st.error("🚨 SUSPICIOUS LINK! Be careful before clicking this URL.")
            st.write("### Warnings found:")
            for reason in reasons:
                st.write(f"⚠️ {reason}")
        else:
            st.success("✅ LOOKS CLEAN! No basic phishing indicators detected in the link syntax.")

elif choice == "Home":
    st.write("### Welcome to PhishGuard!")
    st.write("This tool helps everyday users identify potential cyber risks in their passwords and the links they receive on WhatsApp or social media.")
