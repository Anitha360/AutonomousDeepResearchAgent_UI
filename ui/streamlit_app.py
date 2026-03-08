# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import streamlit as st

# from pipeline.autonomous_research_pipeline import run_autonomous_research
# from report.pdf_generator import generate_pdf
# from tools.citation_manager import generate_citations

# st.title("Autonomous Deep Research AI Agent")

# query = st.text_input("Enter Research Topic")

# if st.button("Run Autonomous Research"):

#     docs, urls = run_autonomous_research(query)

#     report_text = " ".join(docs)

#     citations = generate_citations(urls)

#     generate_pdf(
#         query,
#         report_text,
#         citations,
#         "report/research_report.pdf"
#     )

#     st.success("Research completed")

#     for doc in docs:

#         st.write(doc[:1000])
        
#         # Download button for the generated PDF
#     with open("report/research_report.pdf", "rb") as f:
#         st.download_button(
#             label="Download Research Paper",
#             data=f.read(),
#             file_name="research_report.pdf",
#             mime="application/pdf"
#         )

# ui/app.py
import streamlit as st
import anyio
from config.logger import get_logger
from pipeline.research_orchestrator import run_research

logger = get_logger("StreamlitUI")

st.title("Autonomous Research Agent")

topic = st.text_input("Enter Research Topic")

if st.button("Run Research") and topic.strip():
    logger.info(f"User started research for topic: {topic}")
    with st.spinner("Running multi-agent research system..."):

        # Run async research safely in Streamlit
        result = anyio.run(run_research, topic)

        st.subheader("Research Plan")
        st.write(result["plan"])

        st.subheader("Analysis")
        st.write(result["analysis"])

        st.subheader("Critique")
        st.write(result["critique"])

        st.subheader("Defense")
        st.write(result["defense"])

        st.subheader("Final Report")
        st.write(result["report"])

        st.subheader("Citations")
        st.write(result["citations"])

        # PDF Download button
        with open(result["pdf_path"], "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f,
                file_name="research_report.pdf",
                mime="application/pdf"
            )

        st.success("Research report generated successfully!")
        logger.info(f"Research completed for topic: {topic}")