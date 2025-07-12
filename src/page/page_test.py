import logging
import streamlit as st


# Page Configuration
scope = st.session_state
page = 'testing'
scope.display_page = page
logging.success(f"NAVIGATE {page=}")











