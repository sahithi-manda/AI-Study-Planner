import streamlit as st
import pandas as pd
import plotly.express as px

from planner import generate_plan

from chatbot import (
    get_ai_recommendations,
    chatbot_response
)

from pdf_generator import create_pdf

from database import (
    save_task,
    get_completed_tasks,
    create_user,
    login_user,
    get_subject_analysis
)

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------
st.title("📚 AI Study Planner")

# -----------------------------------
# Theme Toggle
# -----------------------------------
theme = st.sidebar.radio(
    "Choose Theme",
    ["Dark", "Light"]
)

# -----------------------------------
# Theme Styling
# -----------------------------------
if theme == "Dark":

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }

        .css-1d391kg {
            background-color: #161A23;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# Authentication
# -----------------------------------
menu = ["Login", "Signup"]

choice = st.sidebar.selectbox(
    "Menu",
    menu
)

# -----------------------------------
# Signup Section
# -----------------------------------
if choice == "Signup":

    st.subheader("📝 Create New Account")

    new_user = st.text_input("Username")

    new_password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Signup"):

        create_user(
            new_user,
            new_password
        )

        st.success(
            "✅ Account Created Successfully!"
        )

# -----------------------------------
# Login Section
# -----------------------------------
elif choice == "Login":

    st.subheader("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        result = login_user(
            username,
            password
        )

        if result:

            st.success(
                f"Welcome {username} 🎉"
            )

            st.write(
                "Generate a smart study timetable based on your subjects and available study hours."
            )

            # -----------------------------------
            # Sidebar Inputs
            # -----------------------------------
            st.sidebar.header(
                "⚙ Planner Settings"
            )

            subjects = st.sidebar.text_area(
                "Enter Subjects",
                "DSA, Java, DBMS, AIML"
            )

            hours = st.sidebar.slider(
                "Study Hours Per Day",
                1,
                12,
                4
            )

            days = st.sidebar.slider(
                "Days Left For Exams",
                1,
                60,
                15
            )

            # -----------------------------------
            # Generate Study Plan
            # -----------------------------------
            if st.sidebar.button(
                "Generate Study Plan"
            ):

                subject_list = [
                    s.strip()
                    for s in subjects.split(",")
                ]

                # Generate Plan
                plan = generate_plan(
                    subject_list,
                    hours,
                    days
                )

                # Create PDF
                create_pdf(plan)

                # Convert to DataFrame
                df = pd.DataFrame(plan)

                # -----------------------------------
                # Metrics
                # -----------------------------------
                total_hours = df["Hours"].sum()

                total_subjects = len(
                    subject_list
                )

                total_tasks = len(df)

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "📘 Subjects",
                    total_subjects
                )

                col2.metric(
                    "⏳ Total Study Hours",
                    total_hours
                )

                col3.metric(
                    "✅ Total Tasks",
                    total_tasks
                )

                st.divider()

                # -----------------------------------
                # Study Plan Table
                # -----------------------------------
                st.subheader(
                    "📅 Study Plan"
                )

                st.dataframe(
                    df,
                    use_container_width=True
                )

                # -----------------------------------
                # Download PDF Button
                # -----------------------------------
                with open(
                    "study_plan.pdf",
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="📥 Download Study Plan PDF",
                        data=pdf_file,
                        file_name="study_plan.pdf",
                        mime="application/pdf"
                    )

                st.divider()

                # -----------------------------------
                # Subject-wise Chart
                # -----------------------------------
                st.subheader(
                    "📊 Subject-wise Study Hours"
                )

                subject_hours = (
                    df.groupby("Subject")["Hours"]
                    .sum()
                    .reset_index()
                )

                fig = px.bar(
                    subject_hours,
                    x="Subject",
                    y="Hours",
                    title="Study Hours Distribution"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                # -----------------------------------
                # AI Recommendations
                # -----------------------------------
                st.divider()

                st.subheader(
                    "🤖 AI Study Recommendations"
                )

                recommendations = (
                    get_ai_recommendations(
                        subjects,
                        hours,
                        days
                    )
                )

                for tip in recommendations:

                    st.success(tip)

                st.divider()

                # -----------------------------------
                # Daily Schedule
                # -----------------------------------
                st.subheader(
                    "📖 Daily Schedule"
                )

                selected_day = st.selectbox(
                    "Select Day",
                    df["Day"].unique()
                )

                daily_tasks = df[
                    df["Day"] == selected_day
                ]

                completed_tasks = 0

                for index, row in daily_tasks.iterrows():

                    task_completed = st.checkbox(
                        f"{row['Task']} ({row['Hours']} hrs)",
                        key=f"{row['Day']}_{row['Subject']}"
                    )

                    if task_completed:

                        completed_tasks += 1

                        save_task(
                            row["Day"],
                            row["Subject"],
                            row["Task"],
                            1
                        )

                # -----------------------------------
                # Progress Tracking
                # -----------------------------------
                progress = (
                    completed_tasks /
                    len(daily_tasks)
                )

                st.divider()

                st.subheader(
                    "🚀 Daily Progress"
                )

                st.progress(progress)

                st.write(
                    f"Completed {completed_tasks} out of {len(daily_tasks)} tasks"
                )

                # -----------------------------------
                # Overall Productivity Metric
                # -----------------------------------
                overall_completed = (
                    get_completed_tasks()
                )

                st.metric(
                    "🔥 Overall Completed Tasks",
                    overall_completed
                )

                # -----------------------------------
                # AI Chatbot Assistant
                # -----------------------------------
                st.divider()

                st.subheader(
                    "🤖 AI Study Assistant"
                )

                user_question = st.text_input(
                    "Ask your study question"
                )

                if st.button("Ask AI"):

                    response = chatbot_response(
                        user_question
                    )

                    st.info(response)

                # -----------------------------------
                # Weak Area Prediction
                # -----------------------------------
                st.divider()

                st.subheader(
                    "📉 Weak Area Prediction"
                )

                analysis = get_subject_analysis()

                if analysis:

                    analysis_df = pd.DataFrame(
                        analysis,
                        columns=[
                            "Subject",
                            "Completed Tasks"
                        ]
                    )

                    st.dataframe(
                        analysis_df,
                        use_container_width=True
                    )

                    weak_subject = (
                        analysis_df.sort_values(
                            by="Completed Tasks"
                        ).iloc[0]["Subject"]
                    )

                    st.warning(
                        f"⚠ You should focus more on: {weak_subject}"
                    )

                else:

                    st.info(
                        "No study progress data available yet."
                    )

                # -----------------------------------
                # Pomodoro Focus Timer
                # -----------------------------------
                st.divider()

                st.subheader(
                    "⏳ Pomodoro Focus Timer"
                )

                focus_minutes = st.slider(
                    "Select Focus Time (Minutes)",
                    1,
                    60,
                    25
                )

                if st.button(
                    "Start Focus Session"
                ):

                    st.success(
                        f"🔥 Focus for {focus_minutes} minutes without distractions!"
                    )

                    st.info(
                        "📵 Avoid social media and stay focused on your task."
                    )

        else:

            st.error(
                "❌ Invalid Username or Password"
            )