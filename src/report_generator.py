from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(summary, health_score, quality_score, filename):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>CleanIQ - Data Quality Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"Rows : {summary['Rows']}", styles["BodyText"]))
    story.append(Paragraph(f"Columns : {summary['Columns']}", styles["BodyText"]))
    story.append(Paragraph(f"Missing Values : {summary['Missing Values']}", styles["BodyText"]))
    story.append(Paragraph(f"Duplicate Rows : {summary['Duplicate Rows']}", styles["BodyText"]))
    story.append(Paragraph(f"Health Score : {health_score}/100", styles["BodyText"]))
    story.append(Paragraph(f"Quality Score : {quality_score}%", styles["BodyText"]))

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated automatically by CleanIQ.",
            styles["Italic"]
        )
    )

    doc.build(story)