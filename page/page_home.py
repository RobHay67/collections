import logging
import streamlit as st

# Page Configuration
scope = st.session_state
page = 'home'
scope.display_page = page
logging.render(f"NAVIGATE {page=}")


st.title('Home Page')






