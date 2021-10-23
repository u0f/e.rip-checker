import requests
import os
import platform
import threading
import sys
from simple_chalk import chalk
import os.path
mystring = '''

		BY u0f		
		  ______       _____  _____ _____               
		 |  ____|     |  __ \|_   _|  __ \              
		 | |__        | |__) | | | | |__) |             
		 |  __|       |  _  /  | | |  ___/              
		 | |____   _  | | \ \ _| |_| |                  
		 |______|_(_) |_|__\_\_____|_|  ________ _____  
		  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
		 | |    | |__| | |__ | |    | ' /| |__  | |__) |
		 | |    |  __  |  __|| |    |  < |  __| |  _  / 
		 | |____| |  | | |___| |____| . \| |____| | \ \ 
		  \_____|_|  |_|______\_____|_|\_\______|_|  \_\
                                                



			  [1] Start Check
			  [2] View List
		
'''

if platform.system() == "Windows":
	os.system("cls")
elif platform.system() == "Linux":
	os.system("clear")
print(chalk.yellow(mystring)) 


def program():
	
	file_exits = os.path.exists("list.txt")
	if file_exits == False:
		list = open("list.txt", "w")
		print(chalk.red("Reboot the program and add your URL's to check into list.txt file"))
	elif file_exits == True:
		list = open("list.txt", "r")
	disponibles = open("available.txt", "w")

	selection = input(chalk.yellow("\nSelect a option: "))

	if selection == "1":
		print(chalk.blackBright("Starting checking...\n\n"))
		def check():
			for i in list:
				i = i.strip()
				response = requests.get("https://e.rip/" + i )
				if response.status_code == 404:
					print(chalk.green(i + " available"))
					disponibles.write(i+"\n")
				elif response.status_code == 200:
					print(chalk.red(i + " no available"))
			
		for i in range(5):
			thread = threading.Thread(target=check)
			thread.start()		

	elif selection == "2":
		for i in list:
			i = i.strip()
			print(i)
		program()

	input("")	


program()