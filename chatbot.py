# -----------------------------------
# AI Recommendations
# -----------------------------------
def get_ai_recommendations(subjects, hours, days):

    recommendations = []

    subject_count = len(subjects.split(","))

    if hours < 3:
        recommendations.append(
            "⚠ Increase study hours for better preparation."
        )
    else:
        recommendations.append(
            "✅ Your study hours are balanced."
        )

    if days < 7:
        recommendations.append(
            "🔥 Focus more on revision and mock tests."
        )
    elif days < 15:
        recommendations.append(
            "📘 Prioritize important and difficult topics."
        )
    else:
        recommendations.append(
            "🚀 You have enough time for deep learning."
        )

    if subject_count > 5:
        recommendations.append(
            "📚 Split difficult subjects across multiple days."
        )

    recommendations.append(
        "⏳ Use Pomodoro: 50 mins study + 10 mins break."
    )

    recommendations.append(
        "💤 Maintain proper sleep for better memory."
    )

    return recommendations


# -----------------------------------
# AI Chatbot Responses
# -----------------------------------
def chatbot_response(user_input):

    user_input = user_input.lower()

    if "dsa" in user_input:
        return "📘 Practice arrays, linked lists, trees, and solve coding problems daily."

    elif "java" in user_input:
        return "☕ Focus on OOP concepts, collections, and exception handling."

    elif "aiml" in user_input:
        return "🤖 Revise ML algorithms, Python libraries, and model training."

    elif "dbms" in user_input:
        return "🗄 Focus on normalization, SQL queries, and indexing."

    elif "motivation" in user_input:
        return "🔥 Small daily consistency beats random motivation."

    elif "procrastination" in user_input:
        return "⏳ Start with just 10 minutes. Action reduces procrastination."

    else:
        return "📚 Stay consistent and focus on one task at a time."