import streamlit as st

from pages.dvds.header import render_dvd_header
from pages.dvds.render_dvd import render_dvd


scope = st.session_state

st.title('DVD Collection')

render_dvd_header(scope)

no_of_dvds = len(scope.dvd_story_list)

for i in range(0, no_of_dvds, 8):
	col1,col2,col3,col4,col5,col6,col7,col8=st.columns([2,2,2,2,2,2,2,2])
	st.divider()
	with col1: render_dvd(scope, no_of_dvds, i+0)
	with col2: render_dvd(scope, no_of_dvds, i+1)
	with col3: render_dvd(scope, no_of_dvds, i+2)
	with col4: render_dvd(scope, no_of_dvds, i+3)
	with col5: render_dvd(scope, no_of_dvds, i+4)
	with col6: render_dvd(scope, no_of_dvds, i+5)
	with col7: render_dvd(scope, no_of_dvds, i+6)
	with col8: render_dvd(scope, no_of_dvds, i+7)



