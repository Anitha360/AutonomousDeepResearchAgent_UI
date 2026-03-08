import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from pipeline.autonomous_research_pipeline import run_autonomous_research
from report.pdf_generator import generate_pdf
from tools.citation_manager import generate_citations

st.title("Autonomous Deep Research AI Agent")

query = st.text_input("Enter Research Topic")

if st.button("Run Autonomous Research"):

    docs, urls = run_autonomous_research(query)

    report_text = " ".join(docs)

    citations = generate_citations(urls)

    generate_pdf(
        query,
        report_text,
        citations,
        "report/research_report.pdf"
    )

    st.success("Research completed")

    for doc in docs:

        st.write(doc[:1000])
        
        # Download button for the generated PDF
    with open("report/research_report.pdf", "rb") as f:
        st.download_button(
            label="Download Research Paper",
            data=f.read(),
            file_name="research_report.pdf",
            mime="application/pdf"
        )