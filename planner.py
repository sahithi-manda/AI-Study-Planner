def generate_plan(subjects, hours, days):

    plan = []

    hours_per_subject = round(hours / len(subjects), 1)

    for day in range(1, days + 1):

        for subject in subjects:

            task = {
                "Day": day,
                "Subject": subject,
                "Hours": hours_per_subject,
                "Task": f"Study {subject}"
            }

            plan.append(task)

    return plan