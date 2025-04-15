import logging
import streamlit as st
from dvds.views.header import page_header_dvds
from dvds.views.render_dvd import render_dvd


# page allows for the selection of either
# a) a season
# b) a doctor



# Page Configuration
scope = st.session_state
page = 'dvds'
scope.display_page = page
logging.render(f"NAVIGATE {page=}")


st.title('DVD Collection')

page_header_dvds(scope)

dvds_story_list = list(scope.dvds_page_df['story'])
no_of_dvds = len(dvds_story_list)
dvd_index_list = list(scope.dvds_page_df.index.values)

for count in range(0, no_of_dvds, 8):
	col1,col2,col3,col4,col5,col6,col7,col8=st.columns([2,2,2,2,2,2,2,2])
	st.divider()
	with col1: render_dvd(scope, dvd_index_list, count+0)
	with col2: render_dvd(scope, dvd_index_list, count+1)
	with col3: render_dvd(scope, dvd_index_list, count+2)
	with col4: render_dvd(scope, dvd_index_list, count+3)
	with col5: render_dvd(scope, dvd_index_list, count+4)
	with col6: render_dvd(scope, dvd_index_list, count+5)
	with col7: render_dvd(scope, dvd_index_list, count+6)
	with col8: render_dvd(scope, dvd_index_list, count+7)
