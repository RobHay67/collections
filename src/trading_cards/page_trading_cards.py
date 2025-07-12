import logging
import streamlit as st





# Page Configuration
scope = st.session_state
page = 'trading_cards'
scope.display_page = page
logging.success(f"NAVIGATE {page=}")


st.title('Trading Cards')




