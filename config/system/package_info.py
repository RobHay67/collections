import logging
import sys
import streamlit
import pandas
# import numpy
# import pytz
# import watchdog



def terminal_out_package_info():
	logging.warning("terminal_out_package_info")
	print ( '\033[91m')
	print('='*100)
	print ( 'EXPECTED Python Verion  = 3.13.0')
	print ( 'ACTUAL Version      	=', sys.version )
	print ( 'Python Executable     	=', sys.executable )  
	print ( 'Environment Version   	=', sys.prefix )
	print('-'*100)
	print ( 'Package			Installed Version	Expected Version')
	print ( 'Streamlit		', streamlit.__version__, '		1.44.1')
	print ( 'Pandas			', pandas.__version__, '			2.2.3')
	# print ( 'Numpy			', numpy.__version__, '			2.2.3')
	# print ( 'pytz			', pytz.__version__, '		2025.1')
	print ( 'watchdog		','cant check', '		6.0.0')
	print('='*100)
	print ( '\33[0m')
	for i in range(5):print('')

