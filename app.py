import streamlit as st
import google.generativeai as genai

# 1. Secure Setup
# This pulls the key from your secrets.toml file instead of showing it in code
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("API Key not found! Check your secrets.toml file.")

# 2. Page Configuration
st.set_page_config(page_title="Med-Simplify Pro", page_icon="🏥", layout="centered")

st.title("🏥 Med-Simplify AI")
st.markdown("### Turning complex medical reports into clear, actionable steps.")

# 3. User Input Section
st.divider()
medical_text = st.text_area("Paste your medical report or lab results here:", height=200, placeholder="Example: Hemoglobin 10.5 g/dL, TSH 5.2 mIU/L...")

# 4. The Logic (The "Brain")
if st.button("Analyze & Simplify"):
    if medical_text:
        with st.spinner("Analyzing data..."):
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # This 'System Prompt' is what makes your project "Top 10" quality
            prompt = f"""
            You are a world-class medical translator. Analyze the following medical text:
            '{medical_text}'
            
            Please provide the output in this EXACT format:
            
            1. **Status Traffic Light**: (Start with 🟢 for Normal, 🟡 for 'Needs Attention', or 🔴 for Urgent). Explain WHY you chose that color in one sentence.
            2. **The 'Simple English' Summary**: Explain what this report says like I am 10 years old. Avoid jargon.
            3. **Key Markers**: List the most important numbers and what they mean.
            4. **Questions for your Doctor**: Provide 3 specific, smart questions the user should ask their doctor based on these results.
            
            Disclaimer: End with a bold warning that this is an AI tool and not medical advice.
            """
            
            response = model.generate_content(prompt)
            
            # 5. Professional UI Output
            st.success("Analysis Complete!")
            
            # Visual separation for better UX
            st.markdown("---")
            st.markdown(response.text)
            
            # Add a 'Download' button to make it feel like a real tool
            st.download_button("Download Summary", response.text, file_name="Medical_Summary.txt")
    else:
        st.warning("Please paste some text first!")
