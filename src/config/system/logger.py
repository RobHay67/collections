import logging


# logging Colours
white 		= "\033[0m"
grey 		= '\033[90m'
yellow 		= '\033[93m'
green		= "\033[92m"
purple		= "\033[95m"
red			= '\033[91m'
blue        = "\033[94m"
reset 		= white
cyan		= "\033[96m"
blink		= "\033[5m"


def set_logging_config(to_terminal=True):

	logging.basicConfig(
						level		= int(25),
						# format	= "%(levelname)-4s > %(message)s",
						# format	= "%(asctime)s [%(threadName)-12.12s] [%(levelname)-7.7s]  %(message)s",
						format		="%(levelname)s > %(message)s",
						handlers	= [
										logging.FileHandler("zz_log_file.log"),
										logging.StreamHandler(),
										]
						)
	# Custom Logging Levels
	logging.addLevelName(5, grey 	+ "TRACE   " 	+ reset) # 5 Python Code
	logging.trace = trace						
	logging.Logger.trace = trace
	logging.addLevelName(10, cyan 	+ "DEBUG   " 	+ reset)
	logging.addLevelName(20, yellow + "INFO    " 	+ reset)
	logging.addLevelName(25, green 	+ "SUCCESS " 	+ reset) # 21 Streamlit Main Pagers (Controllers / Routers)
	logging.success = success					
	logging.Logger.render = success
	logging.addLevelName(30, purple + "WARNING "	+ reset)
	logging.addLevelName(40, red	+ "ERROR   "	+ reset)
	# logging.addLevelName(50, blue 	+ "CRITICAL"	+ reset)
	logging.addLevelName(50, blink 	+ "CRITICAL"	+ reset)


	logging.success("set_logging_config instantiated")

	logging.trace("TRACE")
	logging.debug("debug")
	logging.info("info")
	logging.success("success")
	logging.warning("warning")
	logging.error("error")
	logging.critical("critical")


# Custom Logging Level Functions (called above during initialisation)

def trace(msg, *args, **kwargs):
	if logging.getLogger().isEnabledFor(5):
		logging.log(5, msg)

def success(msg, *args, **kwargs):
	if logging.getLogger().isEnabledFor(21):
		logging.log(25, msg)





