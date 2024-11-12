import streamlit as st

from page_parts.page_configuration import page_configuration
from page_parts.dash_board import charts_generator

# Page Configuration

# Perform page configuration
page_configuration()

# End - Page Configuration

# Banner

# End - Banner

# Body Section

# Generate charts from company data
charts_generator()

# End - Body Section


# Footer section

# Add custom CSS for the footer
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

# Insert footer content
st.markdown(
    """
    <div class="footer">
        <p>© 2024 Higrowth. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# End - Footer section
