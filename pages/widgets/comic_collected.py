
import streamlit as st




def collected_comic_checkbox(scope, i):

	issue_no = str(scope.comic_issue_list[i])

	widget_key = 'widget_comic_collected_' + issue_no

	st.checkbox(
				label='Collected',
				key=widget_key,
				on_change=update_collected,
				args=(scope, i, widget_key)
				)


def update_collected(scope, i, widget_key):
	print('updated collected - ', i)

	changed_value = scope[widget_key]

	# store the selection
	# scope.user_df.at[user_name, df_col_name] = changed_value

	print('we want to update the comic_df')
	print('but we dont have a key for the df. So how do we update')



