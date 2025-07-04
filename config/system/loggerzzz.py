import logging



def set_logging_config(to_terminal=True):

	logging.basicConfig(
		level=int(35),
		# format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-7.7s]  %(message)s",
		format="%(levelname)-4s > %(message)s",
		handlers=[
			logging.FileHandler('zz_log_file.log'),
			logging.StreamHandler()
			]
	)
	# Custom Logging Levels
	logging.addLevelName(5, 'PARTIAL')
	logging.partial = partial					# 5 Streamlit repetitive tasks
	logging.Logger.partial = partial
	logging.addLevelName(15, 'COMMON')			# 15 python commonly run key code
	logging.common = common					
	logging.Logger.common = common
	logging.addLevelName(25, 'RENDER')
	logging.render = render					# 21 Streamlit Main Pagers (Controllers / Routers)
	logging.Logger.render = render
	logging.addLevelName(35, 'CORE')
	logging.core = core						# 31 python core functions (Controllers)
	logging.Logger.core = core

	# Initial Log and important messages
	
	logging.core("set_logging_config")


# Custom Logging Level Functions (called above during initialisation)

def partial(msg, *args, **kwargs):
	if logging.getLogger().isEnabledFor(5):
		logging.log(5, msg)

def common(msg, *args, **kwargs):
	if logging.getLogger().isEnabledFor(5):
		logging.log(15, msg)


def render(msg, *args, **kwargs):
	if logging.getLogger().isEnabledFor(21):
		logging.log(25, msg)

def core(msg, *args, **kwargs):
	if logging.getLogger().isEnabledFor(31):
		logging.log(35, msg)



