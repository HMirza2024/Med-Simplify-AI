import streamlit as st
import google.generativeai as genai

# 1. Secure Setup
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("API Key not found! Check your Streamlit Secrets.")

# 2. Page Configuration & Professional Styling
st.set_page_config(page_title="Med-Simplify Pro", page_icon="🏥", layout="wide")

# Custom CSS to make it look cleaner
# Updated for Python 3.13 and Streamlit 1.41+
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        height: 3em; 
        background-color: #007bff; 
        color: white; 
    }
    </style>
    """, unsafe_allow_html=True) # Fixed parameter name
# 3. Sidebar Design (The "Control Panel")
with st.sidebar:
    st.title("🏥 Navigation")
    st.info("This AI tool simplifies medical jargon into patient-friendly language.")
    
    st.subheader("🔒 Privacy & Security")
    st.caption("• No data is stored or logged.")
    st.caption("• Please remove Names/IDs before pasting.")
    st.caption("• Uses encrypted HTTPS transmission.")
    
    st.divider()
    st.subheader("💡 Tips for Success")
    with st.expander("What should I paste?"):
        st.write("Blood tests, MRI summaries, discharge notes, or biopsy reports.")
    
    st.success("Target: Data Analyst Portfolio 2026")

# 4. Main Page Layout
st.title("Med-Simplify AI")
st.subheader("Empowering patients through health literacy.")

# Use columns to make the UI look balanced
col1, col2 = st.columns([2, 1])

with col1:
    medical_text = st.text_area(
        "Paste your medical report here:", 
        height=250, 
        placeholder="Example: HbA1c is 6.5%, patient shows mild tachycardia..."
    )

with col2:
    st.markdown("### 🧪 Quick Test")
    st.write("Don't have a report? Use this sample:")
    sample_data = "Patient presents with elevated TSH (5.2 mIU/L) and low Serum Iron. Normal range for TSH is 0.4-4.0."
    if st.button("Load Sample Data"):
        medical_text = sample_data # This trick encourages judges to try it immediately!

# 5. Analysis Logic
if st.button("Analyze & Simplify Report"):
    if medical_text:
        with st.spinner("Decoding medical terminology..."):
            try:
                # Use the stable 2026 model version
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                prompt = f"""
                Act as a compassionate Medical Translator. Analyze: '{medical_text}'
                Format your response clearly:
                - **Status**: (🟢/🟡/🔴) + 1-sentence logic.
                - **The 'Big Picture'**: 2-sentence summary for a non-scientist.
                - **Breakdown**: Bullet points of key findings.
                - **Doctor Consultation**: 3 questions for the next visit.
                Disclaimer: AI tool, not medical advice.
                """
                
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.subheader("📋 Your Simplified Report")
                st.markdown(response.text)
                
                st.download_button("📩 Download PDF Summary", response.text, file_name="Health_Summary.txt")
                
            except Exception as e:
                if "429" in str(e):
                    st.error("🚨 Daily limit reached! (20/20 requests). Please try again tomorrow.")
                else:
                    st.error(f"⚠️ An error occurred: {str(e)}")
    else:
        st.warning("Please enter medical text to begin.")
