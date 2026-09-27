# Smart Student Performance Predictor

## Project Description

Smart Student Performance Predictor is a web-based machine learning project designed to predict a student's academic performance based on relevant educational factors such as study hours, attendance, previous marks, and other performance-related inputs.

The system accepts student information through an easy-to-use interface, processes the input using a trained machine learning model, and provides a predicted performance result.

## Features

* Student data input form
* Performance prediction using machine learning
* User-friendly web interface
* Automatic prediction based on entered student data
* Clear prediction/result display
* Input validation
* Responsive design for desktop and mobile devices
* Easy-to-use interface for students and educators

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Development Tools

* Visual Studio Code
* Git
* GitHub

## Project Structure

```text
smart-student-performance-predictor/
│
├── app.py
├── model/
│   └── student_performance_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── student_data.csv
│
├── requirements.txt
├── README.md
└── screenshots/
```

> Update the file structure above if your actual project folders/files are different.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/smart-student-performance-predictor.git
```

### 2. Open the project folder

```bash
cd smart-student-performance-predictor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install required dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open the application

Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Usage

1. Open the Smart Student Performance Predictor website.
2. Enter the required student information.
3. Provide values such as study hours, attendance, previous marks, and other required inputs.
4. Click the **Predict Performance** button.
5. The machine learning model processes the entered information.
6. The predicted student performance is displayed on the screen.

## Screenshots

### Home Page

Add a screenshot of your website here:

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

> Create a `screenshots` folder in your repository and upload your actual screenshots there.

## Machine Learning Workflow

```text
Student Data
     ↓
Data Preprocessing
     ↓
Feature Selection
     ↓
Model Training
     ↓
Trained ML Model
     ↓
Student Input
     ↓
Performance Prediction
     ↓
Prediction Result
```

## Deployment

### Live Demo

**Deployment Link:**
`ADD-YOUR-LIVE-DEPLOYMENT-LINK-HERE`

Replace the above placeholder with your actual deployed website URL.

### GitHub Repository

**Repository:**
https://github.com/vaishuk2006/smart-student-performance-predictorr/tree/main

Replace `YOUR-USERNAME` with your actual GitHub username.

## Future Scope

* Add more student performance factors
* Improve prediction accuracy with additional training data
* Add performance visualization and charts
* Provide personalized academic recommendations
* Add student progress tracking
* Develop a dashboard for teachers and administrators
* Deploy the system for wider educational use

## Limitations

* Prediction quality depends on the quality and size of the training dataset.
* The model may not capture every factor affecting student performance.
* Predictions should be treated as an analytical aid rather than a definitive assessment of a student's ability.

## Conclusion

The Smart Student Performance Predictor demonstrates how machine learning can be applied to educational data to estimate student performance. The system provides a simple interface for entering student information and generates a prediction using a trained machine learning model. The project can be further improved by incorporating larger datasets, additional features, and personalized recommendations.

## Author

Name: Vaishnavi Kurikyala
Course: TY B.Sc Information Technology
Project: Smart Student Performance Predictor
