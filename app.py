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

    result = predict_performance(
        attendance,
        study_hours,
        assignment_score,
        exam_score,
        participation
    )

    # Extract values returned by fuzzy logic
    predicted_score = result["score"]
    performance_level = result["category"]

   

    

    # Show predicted score
    st.subheader("🎯 Predicted Performance")
    st.write(f"{predicted_score:.2f}%")

     # Show Performance Level
    st.subheader("📊 Performance Level")
    st.write(performance_level)
    

    
    # Success message
    st.success("✅ Prediction completed successfully!")


    # Suggestions
    st.subheader("💡 Suggestions for Improvement")

    suggestions = []

    if attendance is not None and attendance <= 75:
        suggestions.append(
            "Improve your attendance by attending classes regularly."
        )

    if study_hours is not None and study_hours <= 2:
        suggestions.append(
            "Increase your daily study time and maintain a regular study schedule."
        )

    if assignment_score is not None and assignment_score <= 50:
        suggestions.append(
            "Complete assignments regularly and improve your assignment scores."
        )

    if exam_score is not None and exam_score <= 50:
        suggestions.append(
            "Revise important topics and practice previous exam questions."
        )

    if participation is not None and participation <= 50:
        suggestions.append(
            "Participate more actively in classroom discussions and activities."
        )

    if not suggestions:
        suggestions.append(
            "Great work! Maintain your current study habits and continue improving."
        )

    for suggestion in suggestions:
        st.write("• " + suggestion)

    # AI Guidance
    st.subheader("🤖 AI / LangChain Guidance")

    try:
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

    except Exception:
        st.warning(
            "AI guidance could not be generated at this time. "
            "However, the fuzzy logic prediction was completed successfully."
        )
