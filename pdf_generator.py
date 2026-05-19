from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(plan):

    doc = SimpleDocTemplate("study_plan.pdf")

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AI Study Planner Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 12))

    for task in plan:

        text = (
            f"Day {task['Day']} - "
            f"{task['Subject']} - "
            f"{task['Hours']} hrs"
        )

        para = Paragraph(
            text,
            styles['BodyText']
        )

        elements.append(para)

    doc.build(elements)