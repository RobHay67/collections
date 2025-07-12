import logging
import streamlit as st

# Page Configuration
scope = st.session_state
page = 'home'
scope.display_page = page
logging.success(f"NAVIGATE {page=}")


st.title('Home Page')






