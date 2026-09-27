from flask import Flask, render_template, request
from fuzzy_system import predict_performance


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        try:

            # -----------------------------------------
            # GET VALUES FROM FORM
            # -----------------------------------------

            attendance = float(
                request.form.get("attendance", "")
            )

            study_hours = float(
                request.form.get("study_hours", "")
            )

            assignment_score = float(
                request.form.get("assignment_score", "")
            )

            exam_score = float(
                request.form.get("exam_score", "")
            )

            participation = float(
                request.form.get("participation", "")
            )


            # -----------------------------------------
            # INPUT VALIDATION
            # -----------------------------------------

            if not 0 <= attendance <= 100:
                raise ValueError(
                    "Attendance must be between 0 and 100."
                )

            if not 0 <= study_hours <= 12:
                raise ValueError(
                    "Study hours must be between 0 and 12."
                )

            if not 0 <= assignment_score <= 100:
                raise ValueError(
                    "Assignment score must be between 0 and 100."
                )

            if not 0 <= exam_score <= 100:
                raise ValueError(
                    "Exam score must be between 0 and 100."
                )

            if not 0 <= participation <= 100:
                raise ValueError(
                    "Participation must be between 0 and 100."
                )


            # -----------------------------------------
            # FUZZY PREDICTION
            # -----------------------------------------

            result = predict_performance(
                attendance,
                study_hours,
                assignment_score,
                exam_score,
                participation
            )


        except ValueError as e:

            error = str(e)

        except Exception as e:

            error = (
                "Unable to calculate the prediction. "
                "Please check your input values."
            )


    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)