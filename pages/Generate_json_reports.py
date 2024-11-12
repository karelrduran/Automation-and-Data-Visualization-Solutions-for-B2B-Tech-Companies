import tempfile
import time
from pathlib import Path
import streamlit as st

from page_parts.page_configuration import page_configuration
from src.file_utils import FileUtils
from src.json_utils import JsonUtils
from src.openai_utils import get_json_from_company_reports

# Page Configuration

page_configuration()

# End - Page Configuration

# Banner

# End - Banner

# Body Section

# Get OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai_api_key"]

# Define two columns for UI layout
col1, col2 = st.columns(2)

# Left container for uploading company report
contL = col1.container(border=True)
# Right container for uploading competitors' reports
contR = col2.container(border=True)

with contL:
    # File uploader for company report
    company = st.file_uploader(label="Upload company report:",
                               type=['txt'],
                               accept_multiple_files=False)

with contR:
    # File uploader for competitors' reports
    competitors = st.file_uploader(label="Select reports from competing companies:",
                                   type=['txt'],
                                   accept_multiple_files=True)

company_report_path = []
if company:
    original_file = company.name
    original_extension = Path(original_file).suffix

    # Create a temporary file for the uploaded company report
    with tempfile.NamedTemporaryFile(delete=False, suffix=original_extension) as tmp_company_file:
        tmp_company_file.write(company.read())

        company_report_path.append(tmp_company_file.name)

else:
    contL.error("Please upload company report")

competitors_report_paths = []
if competitors:
    # Create temporary files for each uploaded competitor report
    for upload_file in competitors:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_competitor_file:
            tmp_competitor_file.write(upload_file.read())
            competitors_report_paths.append(tmp_competitor_file.name)
else:
    contR.error("Please upload the competitors' reports")

report_paths = []
company_reports = ""
if company_report_path and competitors_report_paths:
    # Combine paths of company and competitors' reports
    report_paths = company_report_path + competitors_report_paths
    # Read content from all uploaded reports
    company_reports = FileUtils.read_multiple_files(report_paths)

cont = st.container(border=False, )
with cont:
    # Button to trigger report generation
    generate_btn = st.button("Generate", disabled=not (company_report_path and competitors_report_paths))

# Instruction for OpenAI assistant
instruction = """I will provide you with reports from different companies. For the first company, I am running a marketing campaign, and the others are direct competitors of this company. I want you to review the data mentioned for each company and generate a detailed analysis including key metrics such as ROI and success rate in JSON format. If a value is missing, mark it as null:
"""

# Example JSON output for reference
example_output = JsonUtils.to_str('data/json/example_output.json')

location = {True: "", False: ""}

if generate_btn:
    # Call OpenAI function to generate JSON report
    generated, json_result = get_json_from_company_reports(openai_api_key=openai_api_key, instruction=instruction,
                                                           company_reports=company_reports,
                                                           example_output=example_output)
    if generated:
        # Display generated JSON result
        st.json(json_result)
    else:
        # Display error message if JSON generation fails
        st.error("The json file could not be generated correctly, please try again.")


# End Section

# Footer section

# Styling for footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 10px 0;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer content
st.markdown(
    """
    <div class="footer">
        <p>© 2024 krduran@ - All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# End - Footer section
