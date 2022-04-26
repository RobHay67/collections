import streamlit as st


# from config.model.page import set_page
def set_page(scope:dict, page:str):
	scope.pages['display_page'] = page



def render_sidebar (scope):
	st.sidebar.button('Home', on_click=set_page, args=(scope, 'home_page', ))
	st.sidebar.write('---')
	st.sidebar.button('Star Wars - Comics', on_click=set_page, args=(scope, 'sw_comics', ))
	st.sidebar.button('Star Wars - Trading Cards', on_click=set_page, args=(scope, 'sw_cards', ))
	st.sidebar.button('Doctor Who - DVD Collections', on_click=set_page, args=(scope, 'dr_who', ))





