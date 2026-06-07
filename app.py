import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI LinkedIn Post Generator",
    page_icon="💼",
    layout="centered"
)

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #F4F7FC;
}

/* Title */
h1 {
    color: #0F172A !important;
    text-align: center;
    font-weight: bold;
}

/* Caption */
.stCaption {
    color: #334155 !important;
    text-align: center;
    font-size: 16px;
}

/* Labels */
label {
    color: #1E293B !important;
    font-weight: 600;
}

/* Text Input */
.stTextInput input {
    background-color: white !important;
    color: #111827 !important;
    border: 2px solid #CBD5E1 !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
    color: #111827 !important;
    border-radius: 10px !important;
    border: 2px solid #CBD5E1 !important;
}

/* Buttons */
.stButton > button {
    background-color: #2563EB !important;
    color: white !important;
    border-radius: 10px !important;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
    font-weight: bold;
}

/* Button Hover */
.stButton > button:hover {
    background-color: #1D4ED8 !important;
    color: white !important;
}

/* Success Box */
.stSuccess {
    background-color: #DCFCE7 !important;
    color: #166534 !important;
    border-radius: 10px;
}

/* Warning Box */
.stWarning {
    background-color: #FEF3C7 !important;
    color: #92400E !important;
    border-radius: 10px;
}

/* Subheader */
h3 {
    color: #0F172A !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("💼 AI LinkedIn Post Generator")

st.caption(
    "Generate professional LinkedIn posts using AI-style formatting."
)

st.markdown("---")

# ---------------- INPUTS ----------------
topic = st.text_input(
    "📌 Enter Topic"
)

tone = st.selectbox(
    "🎯 Select Tone",
    [
        "Professional",
        "Friendly",
        "Motivational",
        "Formal"
    ]
)

audience = st.text_input(
    "👥 Target Audience"
)

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Post"):

    if topic and audience:

        # ---------------- POST GENERATION ----------------
        post = f"""
🚀 Excited to share my latest work on {topic}.

This project was created for {audience} and focuses on delivering practical and useful solutions.

✨ Key Highlights:
✔ Clean UI
✔ AI-powered workflow
✔ Python & Streamlit based
✔ Beginner-friendly experience

I’m continuously improving my AI and automation skills by building real-world projects.

#Python #AI #Streamlit #LinkedIn #Developer
"""

        # ---------------- OUTPUT ----------------
        st.success("✅ LinkedIn Post Generated Successfully")

        st.subheader("📄 Generated LinkedIn Post")

        st.write(post)

        # ---------------- DOWNLOAD BUTTON ----------------
        st.download_button(
            label="📥 Download Post",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain"
        )

    else:
        st.warning("⚠️ Please fill all fields.")
