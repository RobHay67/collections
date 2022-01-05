import streamlit as st


# from set_page import set_page
from config.model.page import set_page


# st.sidebar.button('Single', on_click=set_page, args=('single', ))

def render_sidebar ():
	st.sidebar.button('Star Wars - Comics', on_click=set_page, args=('sw_comics', ))
	st.sidebar.button('Star Wars - Trading Cards', on_click=set_page, args=('sw_cards', ))
	st.sidebar.button('Doctor Who - DVD Collections', on_click=set_page, args=('dr_who', ))
