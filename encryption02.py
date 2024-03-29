# DATA ENCRYPTION WITH FERNET
# VERSION: 0.2

# THOSE MODULES THAT ARE COMMENTED AND WILL BE USED IN FUTURE DEV.
#import base64
#import time
from cryptography.fernet import Fernet
import os
import colorama
import random

def research(amount):
	global path_key
	global path_file
	current_progress = amount

	for i in command[amount:]:
		if i == '%':
			path_file = command[amount:current_progress]
			amount = 1 + current_progress

			path_key = command[amount:]
		else:
			current_progress+=1


# COMMANDS LIST HERE:
def commands_execution(cmd):
	try:
		if cmd == "help":
			print(colorama.Fore.YELLOW + "\nENCRYPTION PART:"
			      "\n   encrypt <path-to-file>%<key> // encrypts the file."
			      "\n   decrypt <path-to-file>%<key> // decrypts the file."
			      "\n   gkey                         // generates new key.\n")

		elif cmd[:8] == "encrypt ":
			research(8)
			open_key()
			encrypt_data()

		elif cmd[:8] == "decrypt ":
			research(8)
			open_key()
			decrypt_data()

		elif cmd[:4] == "gkey":
			generate_key()

		else:
			cmd_execution(cmd)

	except:
		print(colorama.Fore.RED + "InvalidEncryptionToken or Syntax!")

# SCRIPT INITIALIZE METHOD:
def initialize():
	colorama.init()
	print(colorama.Fore.YELLOW + "[+] PROGRAM INITIALIZING...")
	print(colorama.Fore.WHITE + "[!] use 'help' to display available commands.")

	try:
		ScDconsole()

	except KeyboardInterrupt:
	    	print(colorama.Fore.RED + "\n[!] EXITING...")

# COMMAND LINE EXECUTION:
def ScDconsole():
	while True:
		try:
			global command

			command = str(input(colorama.Fore.WHITE + ">_"))
			commands_execution(command)

		except ValueError:
			print("ValueError!")
		except KeyboardInterrupt:
			print(colorama.Fore.RED + "\n[!] EXITING...")
			break


# ENCRYPTION KEYS:
def random_value():
	return random.randrange(0,9)

def generate_key():
	print(colorama.Fore.YELLOW + "[+] GENERATING KEY...")

	try:
		KEY = Fernet.generate_key()
		fernet = Fernet(KEY)
		print(fernet)
		save_key = open('key{val1}{val2}.key'.format(val1=random_value(),val2=random_value()), 'wb')
		save_key.write(KEY)
		save_key.close()
	except:
		os.close()

def open_key():
	global fernet
	try:
		with open(path_key, 'rb') as save_key:
			KEY = save_key.readline()
			fernet = Fernet(KEY)
			print(colorama.Fore.MAGENTA + f"[+] KEY '{save_key}' FOUND!")
	except ValueError:
		print(colorama.Fore.RED + f"[-] KEY '{path_key}' WAS NOT FOUND!")
		sys.exit()


# ENCRYPTION && DECRYPTION PART:
def encrypt_data():
	with open(path_file, 'rb') as read_file:
		var = read_file.read()
		encrypted_data = fernet.encrypt(b"%s"%(var))
	with open(path_file, 'wb') as write_file:
		write_file.write(encrypted_data)
		print("File was encrypted successfully!")

def decrypt_data():
	with open(path_file, 'rb') as read_file:
		var = read_file.read()
		decrypted_data = fernet.decrypt(var)
	with open(path_file, 'wb') as write_file:
		write_file.write(decrypted_data)
		print("File was decrypted successfully!")

def cmd_execution(cmd):
		print(os.system(f'{cmd}'))

# CODE EXECUTION BASE
if __name__ == "__main__":
	initialize()
