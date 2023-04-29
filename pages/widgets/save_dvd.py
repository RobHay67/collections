
import streamlit as st


from dvds.save import save_dvd_file



def dvd_save_button(scope):
    
	st.button(
		label='Save Changes to DVDs File', 
		use_container_width=True,
		on_click=dvd_save_file,
		args=(scope, ),
		
		)


def dvd_save_file(scope):
	save_dvd_file(scope)