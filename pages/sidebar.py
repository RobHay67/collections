import streamlit as st


# from config.model.page import set_page
def set_page(scope:dict, page:str):
	scope.pages['display_page'] = page



def render_sidebar (scope):
	st.sidebar.button('Home', on_click=set_page, args=(scope, 'home_page', ))
	st.sidebar.write('---')
	st.sidebar.button('Comic Collection', on_click=set_page, args=(scope, 'comics', ))
	st.sidebar.button('Trading Cards', on_click=set_page, args=(scope, 'cards', ))
	st.sidebar.button('DVD Collection', on_click=set_page, args=(scope, 'dvds', ))





