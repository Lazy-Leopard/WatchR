from __future__ import unicode_literals

from plugins.censys import censys_ip
from plugins.shodan_io import shodan_host

def repl():
	print(menu())
        user_input = input("Enter your choice:")
        if len(user_input)==0:
        	print("You have entered no input\n")
        else
        	choice = int(user_input)
        
        if choice == 1:
        	""" Left for Email or Username, 
        		testing only IP for the moment """
        
        elif choice == 2:
        	ip = input("Enter the IP,you want to locate")
        	if len(ip)==0:
        		print("No IP Address entered")
        	else:
        		shodan_host(ip)
        		censys_ip(ip)
        
        elif choice == 3:
        	""" Left for some other , 
        		most probably phone number"""
        
        elif choice == 0:
        	exit("You chose not to search anything")
        
        else:
        	pass
        		
        	
        	
        


