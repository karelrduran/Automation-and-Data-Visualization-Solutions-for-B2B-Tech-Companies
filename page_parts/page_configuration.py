import streamlit as st


def page_configuration():
    st.set_page_config(
        page_title="Higrowth",
        page_icon="https://www.sortlist.com/_next/image?url=https%3A%2F%2Fsortlist.gumlet.io%2Fsortlist-core-api%2Fgr1tbmr4wslrq8wbqs4opqlwreh1%3Fw%3D150%26q%3D95%26format%3Dgif&w=128&q=75",
        layout="wide",
        initial_sidebar_state='expanded'
    )

    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

