import streamlit as st

from fuzzy_system import predict_performance
from llm_guidance import generate_guidance


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #0f0f0f;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #bbbbbb;
    margin-bottom: 30px;
}

.section-title {
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🎓 Smart Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict student performance using academic and participation factors</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">Enter Student Details</div>',
    unsafe_allow_html=True
)


attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter attendance",
    step=1,
    format="%d"
)


study_hours = st.number_input(
    "Daily Study Hours",
    min_value=0,
    max_value=12,
    value=None,
    placeholder="Enter study hours",
    step=1,
    format="%d"
)


assignment_score = st.number_input(
    "Assignment Score (%)",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter assignment score",
    step=1,
    format="%d"
)


exam_score = st.number_input(
    "Previous Exam Score (%)",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter exam score",
    step=1,
    format="%d"
)


participation = st.number_input(
    "Class Participation (%)",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter participation",
    step=1,
    format="%d"
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("Predict Performance"):

    # Check whether all fields are filled
    if any(value is None for value in [
        attendance,
        study_hours,
        assignment_score,
        exam_score,
        participation
    ]):

        st.warning("Please enter all values before predicting.")

    else:

        # ====================================================
        # AI/ML FUZZY LOGIC PREDICTION
        # ====================================================

        result = predict_performance(
            attendance,
            study_hours,
            assignment_score,
            exam_score,
            participation
        )

        # Get prediction values FIRST
        predicted_score = result["score"]
        performance_level = result["category"]


        # ====================================================
        # DISPLAY PREDICTION
        # ====================================================

        st.markdown(
            f"### 🎯 Predicted Performance: {predicted_score:.2f}%"
        )

        st.markdown(
            f"### 📊 Performance Level: {performance_level}"
        )

        st.success("Prediction completed successfully!")
            # Suggestions for Improvement
    suggestions = []

    if attendance < 75:
        suggestions.append("Improve your attendance by attending classes regularly.")

    if study_hours < 2:
        suggestions.append("Increase your daily study time to at least 2–3 hours.")

    if assignment_score < 50:
        suggestions.append("Complete assignments regularly and focus on improving your assignment scores.")

    if exam_score < 50:
        suggestions.append("Revise important topics and practice previous exam questions.")

    if participation < 50:
        suggestions.append("Participate more actively in classroom discussions and activities.")

    if not suggestions:
        suggestions.append("Great work! Maintain your current study habits and continue improving.")

    st.subheader("💡 Suggestions for Improvement")

    for suggestion in suggestions:
        st.write("• " + suggestion)

        # ====================================================
        # AI / LANGCHAIN GUIDANCE
        # ====================================================

        st.subheader("🤖 AI / LangChain Guidance")

        guidance = generate_guidance(
            attendance,
            study_hours,
            assignment_score,
            exam_score,
            participation,
            predicted_score,
            performance_level
        )

        st.write(guidance)
