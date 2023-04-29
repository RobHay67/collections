
import streamlit as st

from pages.widgets.comic_collected import collected_comic_checkbox

def render_comic_details(scope, i):
	
	issue_no = str(scope.comic_issue_list[i])
	title = str(scope.comic_title_list[i])
	note = str(scope.comic_notes_list[i])

	if title == 'nan': title = 'Missing Title for this Issue'

	comic_cover = scope.comic_covers[issue_no]

	st.header(issue_no)

	collected_comic_checkbox(scope, i)

	st.image(comic_cover, caption=title)
	if note != 'nan':
		st.caption(note)



# series
# volume
# issue_no
# title
# cover_date
# collected
# condition
# value 
# notes


# series,		volume,	issue_no,	title,	cover_date,	collected,	condition,	value,	notes
# Star Wars,	1,		1,			,		,			1,			,50			,
# Star Wars,	1,		1.1,		,		,			,			,400		,35cent edition with UPC code
# Star Wars,	1,		2,			,		,			1,			,			30,
