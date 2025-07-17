import logging
import streamlit as st
from dvds.model import Dvd
from dvds.views.widgets.available import checkbox_available
from dvds.views.widgets.collected import checkbox_collected
from dvds.views.widgets.watched import checkbox_watched



def render_dvd(scope, list_pos):
	logging.trace(f"render_dvd {list_pos=}")

	if list_pos < Dvd.page_qty:
		dvd			= Dvd.page_dvds[list_pos]
		dvd_cover 	= Dvd.page_covers[list_pos]
		index_no	= dvd.index

		st.caption('Season ' + str(dvd.season))
		st.caption('Story ' + str(dvd.story) + ' - index ' + str(index_no))
		checkbox_available(dvd, index_no)
		checkbox_collected(dvd, index_no)
		checkbox_watched(dvd, index_no)
		st.image(dvd_cover, caption=dvd.title, use_container_width=True)
		st.write(dvd.url)




	

