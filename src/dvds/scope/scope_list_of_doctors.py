import logging


def scope_list_of_doctors(scope):
	logging.warning(f"scope_list_of_doctors")
	dvds_list_of_doctors_for_who = []
	
	# filter dvds to the selected series
	dvd_df = scope.dvds_file[scope.dvds_file['series'] == 'Doctor Who']
	
	# add back our default doctor
	dvds_list_of_doctors_for_who = list(dvd_df['doctor'].unique())
	dvds_list_of_doctors_for_who.insert(0, 'All Doctors')

	return dvds_list_of_doctors_for_who