# import logging


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


def log_instructions():
	# logging.trace("log_instructions")
	print ( "\033[96m")
	print("="*100)
	print ( "Logging Levels")
	print("-"*100)
	print(  grey 	+ "trace" 		+ grey + "    <05> minor function to facilitate code tracking")
	print(  cyan 	+ "debug" 		+ grey + "    <10> additional output for the developer")
	print(  yellow 	+ "info" 		+ grey + "     <20> A primary function has been initiated")
	print(  green 	+ "success" 	+ grey + "  <25> A core function has completed successfully")
	print(  purple 	+ "warning" 	+ grey + "  <30> Data has been changed by this function")
	print(  red 	+ "errors" 		+ grey + "   <40> Actual Errors or unexpected results (look into these)")
	print(  blue 	+ "critical"	+ grey + " <50> TODOs or placeholders notes that are currently being worked upon")
	print ( "\33[96m")
	print("="*100)
	print ( "\33[0m")
