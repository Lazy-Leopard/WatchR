def banner():
	return("""
	SWE PROJECT - 51
	""")

def menu():
	return("""
	1. Email Address
	2. IP 
	3. Phone Number
	0. Exit
	""")
	
if __name__ == '__main__':
	if sys.version_info[0] > 2:
		try:
			print(banner())
			from core import repl_prompt
		except ModuleNotFoundError:
			print('\nSeems like you haven\'t installed Requirements, Please install using: python setup.py install')
			quit()
	else:
		try:
			from core import repl_prompt
		except ImportError:
			print('\nSeems like you haven\'t installed Requirements, Please install using: python setup.py install')
			quit()
