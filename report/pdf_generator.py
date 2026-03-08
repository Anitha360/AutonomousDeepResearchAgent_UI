from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(title, content, citations, filename):

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph(title, styles["Title"]))

    story.append(Paragraph(content, styles["BodyText"]))

    story.append(Paragraph("<b>References</b>", styles["Heading2"]))

    for cite in citations:

        story.append(Paragraph(cite, styles["BodyText"]))

    doc = SimpleDocTemplate(filename)

    doc.build(story)