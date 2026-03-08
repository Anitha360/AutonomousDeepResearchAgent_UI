from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from config.logger import get_logger

logger = get_logger("PDFGenerator")

def generate_pdf(title, content, citations, filename):
    logger.info("Starting PDF generation")

    try:
        logger.info("Preparing document styles")

        styles = getSampleStyleSheet()

        story = []
        logger.info("Adding title to PDF: %s", title)

        story.append(Paragraph(title, styles["Title"]))
        logger.info("Adding research content to PDF")

        story.append(Paragraph(content, styles["BodyText"]))
        logger.info("Adding references section")

        story.append(Paragraph("<b>References</b>", styles["Heading2"]))
        logger.info("Total citations to add: %d", len(citations))

        for cite in citations:
            logger.info("Adding citation: %s", cite)
            story.append(Paragraph(cite, styles["BodyText"]))
        
        logger.info("Creating PDF document: %s", filename)

        doc = SimpleDocTemplate(filename)

        doc.build(story)
        logger.info("PDF successfully generated and saved")
        
    except Exception as e:

        logger.error("PDF generation failed: %s", str(e))