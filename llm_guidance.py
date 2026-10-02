import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


def generate_guidance(
    attendance,
    study_hours,
    assignment_score,
    exam_score,
    participation,
    predicted_score,
    performance_level
):
    """
    Generate personalized academic guidance using
    LangChain + Google Gemini.
    """

    # ========================================================
    # GET API KEY FROM STREAMLIT SECRETS
    # ========================================================

    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except Exception:
        api_key = None

    if not api_key:
        return (
            "Gemini API key is not configured. "
            "Please add GOOGLE_API_KEY to Streamlit secrets."
        )

    # ========================================================
    # CREATE GEMINI MODEL
    # ========================================================

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=api_key,
            temperature=0.3,
            max_retries=2,
            timeout=60
        )

        # ====================================================
        # PROMPT
        # ====================================================

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are an AI academic performance assistant.

A student's performance has already been predicted
using a Fuzzy Logic system.

Analyze the student's provided academic information
and the predicted performance.

Provide:

1. A short explanation of the predicted performance.
2. The main factors affecting the student's performance.
3. Three practical and personalized suggestions for improvement.
4. Include the concept of Abhyasa from Indian Knowledge
   Systems, meaning consistent practice, regular effort,
   discipline, and continuous learning.

Keep the response concise, clear, student-friendly,
and directly related to the student's actual inputs.

Do not invent information.
Do not calculate or change the predicted score.
"""
                ),
                (
                    "human",
                    """
Student Information:

Attendance: {attendance}%
Daily Study Hours: {study_hours}
Assignment Score: {assignment_score}%
Previous Exam Score: {exam_score}%
Class Participation: {participation}%

Fuzzy Logic Predicted Performance:
{predicted_score}%

Performance Level:
{performance_level}

Generate personalized academic guidance based on
these values.
"""
                )
            ]
        )

        # ====================================================
        # CREATE LANGCHAIN CHAIN
        # ====================================================

        chain = prompt | llm

        # ====================================================
        # SEND DATA TO GEMINI
        # ====================================================

        response = chain.invoke(
            {
                "attendance": attendance,
                "study_hours": study_hours,
                "assignment_score": assignment_score,
                "exam_score": exam_score,
                "participation": participation,
                "predicted_score": predicted_score,
                "performance_level": performance_level
            }
        )

        # ====================================================
        # RETURN RESPONSE
        # ====================================================

        if hasattr(response, "content"):
            content = response.content

            if isinstance(content, str):
                return content

            if isinstance(content, list):
                text_parts = []

                for item in content:
                    if isinstance(item, dict) and "text" in item:
                        text_parts.append(item["text"])
                    elif isinstance(item, str):
                        text_parts.append(item)

                if text_parts:
                    return "\n".join(text_parts)

        return str(response)

    # ========================================================
    # GEMINI ERROR
    # ========================================================

    except Exception as e:
        return (
            "Gemini could not generate AI guidance right now. "
            "The Fuzzy Logic prediction was completed successfully."
        )
