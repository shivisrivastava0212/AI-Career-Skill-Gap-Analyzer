import os
import time
from dotenv import load_dotenv
from google import genai
import streamlit as st

# --------------------------------------------------
# ENVIRONMENT & CLIENT SETUP
# --------------------------------------------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="AI Career Skill Gap Analyzer",
    page_icon="🚀",
    layout="centered"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🚀 AI Career Skill Gap Analyzer")
st.write(
    "Discover the skills you need for your target career "
    "and identify what you should learn next."
)

st.divider()

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
st.subheader("👤 Tell us about yourself")

target_role = st.text_input(
    "Target Role",
    placeholder="e.g. AI Engineer Intern"
)

current_skills = st.text_area(
    "Your Current Skills",
    placeholder="e.g. Python, Machine Learning, Pandas, Scikit-learn, Git"
)

experience = st.selectbox(
    "Experience Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

st.divider()

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------
if st.button("🔍 Analyze My Skill Gap", use_container_width=True):
    if not target_role:
        st.warning("Please enter your target role.")
    elif not current_skills:
        st.warning("Please enter your current skills.")
    else:
        st.success("Analysis started!")
        
        st.subheader("📊 Your Profile")
        st.write(f"**Target Role:** {target_role}")
        st.write(f"**Experience Level:** {experience}")
        
        st.subheader("💻 Current Skills")
        skills = [
            skill.strip()
            for skill in current_skills.split(",")
            if skill.strip()
        ]
        
        for skill in skills:
            st.write(f"✔ {skill}")
            
        st.subheader("📈 Skill Gap Analysis")
        
        with st.spinner("Analyzing your career gap with Gemini (auto-retrying if busy)..."):
            prompt = f"""
            Act as an expert career coach and technical mentor.
            Target Role: {target_role}
            Experience Level: {experience}
            Current Skills: {current_skills}

            Please provide:
            1. Missing key skills required for the target role.
            2. A structured learning roadmap (what to learn next).
            3. Recommended free resources or projects to bridge the gap.
            Keep the response clear, structured, and encouraging.
            """

            max_retries = 3
            success = False
            response = None

            for attempt in range(max_retries):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt
                    )
                    if response and response.text:
                        success = True
                        break
                except Exception as e:
                    if "503" in str(e) or "UNAVAILABLE" in str(e):
                        if attempt < max_retries - 1:
                            time.sleep(2)  # Wait 2 seconds before retrying
                            continue
                    # If it's another error or final attempt failed, raise it
                    if attempt == max_retries - 1:
                        st.error(f"An error occurred: {e}")

            if success and response and response.text:
                st.markdown(response.text)
            elif not success:
                st.warning("⚠️ Gemini servers are heavily loaded right now. Please try clicking the button again!")
                