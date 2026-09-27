import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# ---------------------------------------------------------
# SMART STUDENT PERFORMANCE PREDICTOR
# Fuzzy Logic System
# ---------------------------------------------------------

# -----------------------------
# INPUT VARIABLES
# -----------------------------

attendance = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "attendance"
)

study_hours = ctrl.Antecedent(
    np.arange(0, 13, 1),
    "study_hours"
)

assignment_score = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "assignment_score"
)

exam_score = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "exam_score"
)

participation = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "participation"
)


# -----------------------------
# OUTPUT VARIABLE
# -----------------------------

performance = ctrl.Consequent(
    np.arange(0, 101, 1),
    "performance"
)


# =========================================================
# MEMBERSHIP FUNCTIONS
# =========================================================

# Attendance
attendance["low"] = fuzz.trimf(
    attendance.universe,
    [0, 0, 50]
)

attendance["medium"] = fuzz.trimf(
    attendance.universe,
    [30, 60, 80]
)

attendance["high"] = fuzz.trimf(
    attendance.universe,
    [65, 100, 100]
)


# Study Hours
study_hours["low"] = fuzz.trimf(
    study_hours.universe,
    [0, 0, 4]
)

study_hours["medium"] = fuzz.trimf(
    study_hours.universe,
    [2, 5, 8]
)

study_hours["high"] = fuzz.trimf(
    study_hours.universe,
    [6, 12, 12]
)


# Assignment Score
assignment_score["low"] = fuzz.trimf(
    assignment_score.universe,
    [0, 0, 50]
)

assignment_score["medium"] = fuzz.trimf(
    assignment_score.universe,
    [35, 60, 80]
)

assignment_score["high"] = fuzz.trimf(
    assignment_score.universe,
    [65, 100, 100]
)


# Exam Score
exam_score["low"] = fuzz.trimf(
    exam_score.universe,
    [0, 0, 50]
)

exam_score["medium"] = fuzz.trimf(
    exam_score.universe,
    [35, 60, 80]
)

exam_score["high"] = fuzz.trimf(
    exam_score.universe,
    [65, 100, 100]
)


# Participation
participation["low"] = fuzz.trimf(
    participation.universe,
    [0, 0, 40]
)

participation["medium"] = fuzz.trimf(
    participation.universe,
    [25, 55, 75]
)

participation["high"] = fuzz.trimf(
    participation.universe,
    [60, 100, 100]
)


# -----------------------------
# PERFORMANCE OUTPUT
# -----------------------------

performance["poor"] = fuzz.trimf(
    performance.universe,
    [0, 0, 40]
)

performance["average"] = fuzz.trimf(
    performance.universe,
    [25, 50, 70]
)

performance["good"] = fuzz.trimf(
    performance.universe,
    [55, 72, 88]
)

performance["excellent"] = fuzz.trimf(
    performance.universe,
    [78, 100, 100]
)


# =========================================================
# FUZZY RULES
# =========================================================

rules = [

    # -------------------------
    # POOR PERFORMANCE
    # -------------------------

    ctrl.Rule(
        attendance["low"] &
        exam_score["low"],
        performance["poor"]
    ),

    ctrl.Rule(
        study_hours["low"] &
        exam_score["low"],
        performance["poor"]
    ),

    ctrl.Rule(
        assignment_score["low"] &
        exam_score["low"],
        performance["poor"]
    ),

    ctrl.Rule(
        attendance["low"] &
        study_hours["low"] &
        participation["low"],
        performance["poor"]
    ),

    ctrl.Rule(
        attendance["low"] &
        assignment_score["low"] &
        exam_score["low"],
        performance["poor"]
    ),


    # -------------------------
    # AVERAGE PERFORMANCE
    # -------------------------

    ctrl.Rule(
        attendance["medium"] &
        exam_score["medium"],
        performance["average"]
    ),

    ctrl.Rule(
        study_hours["medium"] &
        exam_score["medium"],
        performance["average"]
    ),

    ctrl.Rule(
        assignment_score["medium"] &
        exam_score["medium"],
        performance["average"]
    ),

    ctrl.Rule(
        attendance["medium"] &
        assignment_score["medium"] &
        participation["medium"],
        performance["average"]
    ),

    ctrl.Rule(
        study_hours["medium"] &
        exam_score["medium"] &
        assignment_score["medium"],
        performance["average"]
    ),

    ctrl.Rule(
        attendance["low"] &
        exam_score["medium"],
        performance["average"]
    ),


    # -------------------------
    # GOOD PERFORMANCE
    # -------------------------

    ctrl.Rule(
        attendance["high"] &
        exam_score["medium"],
        performance["good"]
    ),

    ctrl.Rule(
        attendance["medium"] &
        exam_score["high"],
        performance["good"]
    ),

    ctrl.Rule(
        study_hours["high"] &
        exam_score["medium"],
        performance["good"]
    ),

    ctrl.Rule(
        assignment_score["high"] &
        exam_score["medium"],
        performance["good"]
    ),

    ctrl.Rule(
        attendance["high"] &
        assignment_score["high"] &
        participation["medium"],
        performance["good"]
    ),

    ctrl.Rule(
        study_hours["high"] &
        assignment_score["medium"] &
        exam_score["high"],
        performance["good"]
    ),


    # -------------------------
    # EXCELLENT PERFORMANCE
    # -------------------------

    ctrl.Rule(
        attendance["high"] &
        study_hours["high"] &
        exam_score["high"],
        performance["excellent"]
    ),

    ctrl.Rule(
        attendance["high"] &
        assignment_score["high"] &
        exam_score["high"],
        performance["excellent"]
    ),

    ctrl.Rule(
        study_hours["high"] &
        assignment_score["high"] &
        exam_score["high"],
        performance["excellent"]
    ),

    ctrl.Rule(
        attendance["high"] &
        study_hours["high"] &
        participation["high"] &
        exam_score["high"],
        performance["excellent"]
    ),

    ctrl.Rule(
        attendance["high"] &
        study_hours["high"] &
        assignment_score["high"] &
        exam_score["high"] &
        participation["high"],
        performance["excellent"]
    )
]


# =========================================================
# CONTROL SYSTEM
# =========================================================

performance_control = ctrl.ControlSystem(rules)


# =========================================================
# PREDICTION FUNCTION
# =========================================================

def predict_performance(
    attendance_value,
    study_hours_value,
    assignment_score_value,
    exam_score_value,
    participation_value
):

    system = ctrl.ControlSystemSimulation(performance_control)

    system.input["attendance"] = attendance_value
    system.input["study_hours"] = study_hours_value
    system.input["assignment_score"] = assignment_score_value
    system.input["exam_score"] = exam_score_value
    system.input["participation"] = participation_value

    system.compute()

    score = system.output["performance"]

    # Keep the score within 0–100
    score = max(0, min(100, score))

    # -----------------------------
    # PERFORMANCE CATEGORY
    # -----------------------------

    if score < 40:
        category = "Poor"

    elif score < 60:
        category = "Average"

    elif score < 80:
        category = "Good"

    else:
        category = "Excellent"

    # -----------------------------
    # IKS / ABHYASA GUIDANCE
    # -----------------------------

    if category == "Poor":

        guidance = (
            "Focus on building regular learning habits. "
            "The IKS concept of Abhyasa emphasizes consistent "
            "practice and sustained learning. Start with small "
            "daily study goals and improve consistency."
        )

    elif category == "Average":

        guidance = (
            "Your performance shows scope for improvement. "
            "Following the principle of Abhyasa, maintain regular "
            "study practice and gradually strengthen attendance, "
            "assignments and participation."
        )

    elif category == "Good":

        guidance = (
            "Your performance is in the good range. Continue "
            "consistent learning and regular practice. The principle "
            "of Abhyasa can be applied by maintaining disciplined "
            "study habits and continuously improving weak areas."
        )

    else:

        guidance = (
            "Your performance is in the excellent range. Continue "
            "your consistent learning and practice. The principle "
            "of Abhyasa emphasizes sustained practice, which can "
            "help maintain long-term learning and improvement."
        )

    return {
        "score": round(score, 2),
        "category": category,
        "guidance": guidance
    }