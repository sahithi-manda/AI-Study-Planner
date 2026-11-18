# 📚 AI Study Planner

A study planning app built with **Streamlit** and **Python**. It generates a daily study schedule from your subjects, available hours and days until exams, tracks progress, highlights weak areas, and gives study recommendations from a set of rules.

## ✨ Features

- **🔐 User Authentication:** Signup and login, with passwords stored as salted PBKDF2-SHA256 hashes.
- **📅 Smart Study Planner:** Automatically generate a detailed daily study schedule based on your subjects, available daily study hours, and days left until exams.
- **📥 PDF Export:** Download your generated study plan as a nicely formatted PDF.
- **📊 Interactive Analytics:** Visualize your study hours distribution across subjects with Plotly charts.
- **🤖 Study Assistant & Recommendations:** Rule-based tips that adapt to your study hours, days left and number of subjects, plus a keyword-based assistant that answers common study questions.
- **✅ Daily Progress Tracking:** Check off completed tasks and monitor your daily productivity with progress bars.
- **📉 Weak Area Prediction:** Analyzes your task completion rates to identify and warn you about subjects that need more attention.
- **⏳ Pomodoro Focus Timer:** A built-in timer to help you stay focused during study sessions without distractions.
- **🌗 Dark/Light Mode:** Customizable UI themes for comfortable viewing day or night.

## 🛠️ Technology Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
- **Data Visualization:** [Plotly Express](https://plotly.com/python/plotly-express/)
- **PDF Generation:** [ReportLab](https://pypi.org/project/reportlab/)
- **Backend/Database:** Python, SQLite (for task and user tracking)

## 🚀 Installation & Setup

Follow these steps to run the AI Study Planner locally on your machine.

### Prerequisites

- Python 3.8+ installed
- pip (Python package installer)

### 1. Clone the Repository (or navigate to the project directory)

```bash
cd "AI Study Planner"
```

### 2. Install Dependencies

You can install the required packages using the provided requirements file:

```bash
pip install -r requirements.txt.txt
```

*(Note: The requirements file is named `requirements.txt.txt` in this repository.)*

### 3. Run the Application

Launch the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will start a local server, and the app will open in your default web browser (usually at `http://localhost:8501`).

## 📖 How to Use

1. **Create an Account / Login:** Start by creating a new account from the sidebar menu, then log in.
2. **Configure Settings:** In the sidebar, enter the subjects you need to study (comma-separated), your daily study hours, and the number of days left until your exams.
3. **Generate Plan:** Click "Generate Study Plan" to see your personalized schedule, task list, and AI recommendations.
4. **Track Progress:** Use the "Daily Schedule" section to check off tasks as you complete them. Your overall progress and weak areas will update automatically.
5. **Focus Mode:** Use the Pomodoro Timer at the bottom to set focus sessions.

## 📁 Project Structure

```
AI Study Planner/
├── app.py                   # Main Streamlit application file
├── chatbot.py               # Rule-based recommendations and keyword-based study assistant
├── database.py              # SQLite database operations (auth, tasks, analytics)
├── planner.py               # Logic for generating the study schedule
├── pdf_generator.py         # Code to generate the PDF version of the study plan
├── requirements.txt.txt     # List of Python dependencies
├── study_planner.db         # SQLite database file
└── README.md                # Project documentation
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to modify the code and enhance the features for your personal use or to contribute to the repository.

---
*Built with ❤️ to make studying smarter, not harder.*
