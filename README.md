# Smart Student Performance Predictor

## Project Description

Smart Student Performance Predictor is a web-based application that predicts a student's academic performance based on important educational factors.

The system takes student inputs such as **attendance, daily study hours, assignment score, previous exam score, and class participation**. A **fuzzy logic-based system** processes these inputs and generates a predicted performance percentage and performance level.

The application also provides **suggestions for improvement** based on the student's entered values.

## Features

* Student performance input form
* Fuzzy logic-based performance prediction
* Attendance-based analysis
* Daily study hours analysis
* Assignment score analysis
* Previous exam score analysis
* Class participation analysis
* Predicted performance percentage
* Performance level classification
* Personalized suggestions for improvement
* Input validation
* User-friendly interface
* Responsive and visually styled web interface

## Technologies Used

### Programming Language

* Python

### Framework

* Streamlit

### Libraries

* NumPy
* scikit-fuzzy

### Development Tools

* Visual Studio Code
* Git
* GitHub

### Deployment

* Streamlit Community Cloud

### AI/ML Components

* Fuzzy Logic
* Fuzzy Control System

**LangChain:** Not used in this project.

**LLM/API:** Not used in this project.

**Database/Vector Database:** Not used in this project.

## Project Structure

```text
smart-student-performance-predictor/
│
├── app.py
├── fuzzy_system.py
├── requirements.txt
├── README.md
└── screenshots/
```

> The project structure should be updated if additional files are present in your actual GitHub repository.

## How the System Works

The system uses fuzzy logic to evaluate different student performance factors.

```text
Student Input
      ↓
Attendance
Study Hours
Assignment Score
Previous Exam Score
Class Participation
      ↓
Fuzzy Logic Processing
      ↓
Performance Calculation
      ↓
Predicted Performance %
      ↓
Performance Level
      ↓
Suggestions for Improvement
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vaishuk2006/smart-student-performance-predictorr.git
```

### 2. Open the project folder

```bash
cd smart-student-performance-predictorr
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

### 7. Open the application

Streamlit will provide a local URL in the terminal, normally:

```text
http://localhost:8501
```

## Usage

1. Open the Smart Student Performance Predictor application.
2. Enter the student's attendance percentage.
3. Enter daily study hours.
4. Enter the assignment score.
5. Enter the previous exam score.
6. Enter the class participation percentage.
7. Click **Predict Performance**.
8. The fuzzy logic system processes the entered values.
9. The predicted performance percentage is displayed.
10. The corresponding performance level is displayed.
11. Suggestions for improvement are provided based on the student's inputs.

## Suggestions for Improvement

The application provides suggestions according to the entered student information.

For example, if attendance is low, the system may suggest improving attendance. If daily study hours are low, it may suggest increasing study time.

This makes the system more useful than simply displaying a prediction because students can identify areas that may require improvement.

## Indian Knowledge Systems (IKS) Connection

The project has a connection with the **Indian Knowledge Systems (IKS)** through the idea of holistic student development.

Traditional Indian educational approaches emphasize the development of students through multiple aspects of learning, discipline, regular practice, participation, and continuous improvement rather than focusing only on examination marks.

The Smart Student Performance Predictor considers multiple factors such as attendance, study habits, assignments, examination performance, and classroom participation. This supports a broader approach to understanding student performance.

The project therefore connects the modern use of **fuzzy logic and educational technology** with the IKS principle of considering learning and development through multiple dimensions.

## Screenshots

Add screenshots of the actual working application to the `screenshots` folder.

### Home Page

```markdown
![Home Page](screenshots/home-page.png)
```

### Student Input Form

```markdown
![Student Input Form](screenshots/input-form.png)
```

### Prediction Result

```markdown
![Prediction Result](screenshots/prediction-result.png)
```

### Suggestions

```markdown
![Suggestions](screenshots/suggestions.png)
```

## Testing

The application can be tested using different combinations of student performance inputs.

Examples of test cases include:

* Low attendance and low study hours
* Average attendance and study hours
* High attendance and high study hours
* Low examination and assignment scores
* High overall performance factors

The output should change according to the values entered by the user.

## Limitations

* The prediction depends on the fuzzy rules defined in the system.
* The system does not consider every possible factor affecting student performance.
* The prediction is an analytical estimate and should not be treated as a definitive assessment of a student's ability.
* The current system does not use a large trained dataset or an external AI model.

## Future Scope

* Add more student performance factors.
* Improve and expand the fuzzy rules.
* Add performance visualization and charts.
* Provide more detailed personalized academic recommendations.
* Add student progress tracking.
* Develop a teacher dashboard.
* Extend the system with a larger educational dataset.
* Deploy the system for wider educational use.

## Deployment

[### Live Demo](https://smart-student-performance-predictor.streamlit.app/?utm_source=chatgpt.com)

**Deployment Link:**

https://smart-student-performance-predictor.streamlit.app/

### GitHub Repository

**Repository:**

https://github.com/vaishuk2006/smart-student-performance-predictorr

## Conclusion

The Smart Student Performance Predictor demonstrates how **fuzzy logic can be used to estimate student academic performance** from multiple educational factors.

The system provides a simple interface where users can enter attendance, study hours, assignment score, previous exam score, and class participation. It then generates a predicted performance percentage, performance level, and suggestions for improvement.

The project demonstrates the application of Python, Streamlit, NumPy, and scikit-fuzzy in developing an educational performance prediction system.

## Author

**Name:** Vaishnavi Kurikyala
**Course:** TY B.Sc Information Technology
**Project:** Smart Student Performance Predictor
