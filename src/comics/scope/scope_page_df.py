import logging


def scope_comic_df_for_page(scope):
	series = scope.comics_selected_series
	missing_only = scope.comics_selected_missing_only
	logging.warning(f"create_comic_df {series=} {missing_only=}")
	
	# Filter for Series
	comic_df = scope.comics_file.copy()
	comics_page_df = comic_df[comic_df['series'] == series]

	# Filter to missing eps only if requested
	if missing_only == True:
		# Show only DVDs that HAVE NOT been collected (missing episodes)
		comics_page_df = comics_page_df[comics_page_df['collected'] == False]

	return comics_page_df