from numpy import issubsctype
import streamlit as st

# from comics.view.comics import render_comics_star_wars
from comics.model.series import series_selector
from pages.comics.details import render_comic_details


# Page Configuration
scope = st.session_state
# page = 'screener'
# page_title = 'Ticker Screener'
# page_icon = '🧪'
# # -----------------------------
# scope.pages['display'] = page

st.title('Comic Collection')

col1,col2=st.columns([4,8])

with col1: series_selector(scope)

# sort the comics_df by issue_no
scope.comic_df.sort_values(by='issue_no')
no_of_comics = len(scope.comic_df)
scope.comic_issue_list = list(scope.comic_df['issue_no'])
scope.comic_title_list = list(scope.comic_df['title'])
scope.comic_notes_list = list(scope.comic_df['notes'])


for i in range(0, no_of_comics, 4):
	col1,col2,col3,col4=st.columns([2,2,2,2])
	with col1: render_comic_details(scope, i, )
	with col2: render_comic_details(scope, i+1)
	with col3: render_comic_details(scope, i+2)
	with col4: render_comic_details(scope, i+3)

st.write(scope.comic_df)










# series
# volume
# issue_no
# title
# cover_date
# collected
# condition
# value 
# notes



	


# def render_comics_page(scope):








