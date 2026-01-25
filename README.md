# 🏥 Med-Simplify AI: Bridging the Health Literacy Gap
Med-Simplify AI is a specialized health literacy tool designed to transform complex, jargon-heavy medical reports into clear, actionable, and patient-friendly insights. Built by a Biomedical Science student, this app aims to empower patients to have more informed and confident conversations with their healthcare providers.

## Key Features
- Visual Health "Traffic Light" System: Instantly categorizes report findings into Green (Normal), Yellow (Monitor), or Red (Urgent) status for immediate clarity.

- Plain Language Translation: Uses advanced AI to "de-jargonize" medical terms into a summary a 10-year-old could understand.

- Actionable "Questions for My Doctor": Automatically generates a list of three targeted questions based on the specific results to prepare patients for their next consultation.

- Secure & Privacy-Conscious: Built with a "zero-retention" philosophy, encouraging users to remove personal identifiers before analysis.

## Technology Stack
- Frontend: Streamlit (Python-based web framework)

- Brain: Google Gemini 2.5 Flash API (LLM)

- Security: Encrypted secrets management for API protection

- Language: Python 3.10+

## Security & Privacy
- API Security: This project utilizes Streamlit's encrypted Secrets management and a .gitignore protocol to ensure API keys are never exposed in public version control.

- Data Handling: This app is a stateless prototype. It does not store user data or uploaded text in any database, ensuring a high level of privacy for demonstration purposes.

- Rate Limiting: To remain cost-effective and secure, the app operates on a free-tier quota (20 requests per day).

## How to Use
- Paste Text: Copy the text from your lab result or medical summary.

- Remove PII: Ensure you remove your name, DOB, or hospital ID for privacy.

- Analyze: Click the "Analyze & Simplify" button.

- Download: Save your simplified summary and doctor's questions for your next visit.

## Medical Disclaimer
This tool is for educational purposes only. Med-Simplify AI is not a medical professional. It does not provide diagnoses or treatment advice. Always consult with a qualified healthcare provider regarding any medical condition or report interpretation.

## About the Author
I am a Biomedical Science student (Class of 2026) passionate about the intersection of healthcare and data. My goal is to use data-driven tools to solve real-world problems in the medical field.

Portfolio: [HMirza2024]

Project Goal: Created as a capstone/competition project to improve patient-doctor communication.
