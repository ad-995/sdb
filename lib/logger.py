from lib import arguments
import os
from time import gmtime, strftime

colour_red = "\033[1;31m"
colour_blue = "\033[1;34m"
colour_yellow = "\033[1;33m"
colour_green = "\033[1;32m"
colour_magenta = "\033[1;35m"
colour_remove= "\033[0m"

args = arguments.get_args()

if args.silent == True:
	silent = True
else:
	silent = False

log_directory = 'logs/'
log_file = "sdb.log"
log_path = log_directory+log_file

def strip(string):
	# This is annoying, but because the other logging functions are using ansi - they have to be stripped to log to file because it also writes out the ansi codes
	# This just kills them
	import re
	ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
	result = ansi_escape.sub('', string)
	return result

def log_to_file(string):
	log_time=strftime("%d/%m/%y_%H:%M:%S", gmtime())
	if not os.path.exists(log_directory):
	    os.makedirs(log_directory)
	with open(log_path,'a') as f:
		string = strip(string)
		f.write('[%s] %s\n\r' % (log_time,string))

def RED(string):
	string=str(string)
	return (colour_red + string + colour_remove)

def BLUE(string):
	string=str(string)
	return (colour_blue + string + colour_remove)

def YELLOW(string):
	string=str(string)
	return (colour_yellow + string + colour_remove)

def GREEN(string):
	string=str(string)
	return (colour_green + string + colour_remove)

def blue(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	if args.silent == False:
		print('['+log_time+']'+BLUE(' >> ' )+string)
	log_to_file(string)

def green(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	if args.silent == False:
		print('['+log_time+']'+GREEN(' >> ' )+string)
	log_to_file(string)

def red(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	if args.silent == False:
		print('['+log_time+']'+RED(' >> ' )+string)
	log_to_file(string)

def yellow(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	if args.silent == False:
		print('['+log_time+']'+YELLOW(' >> ' )+string)
	log_to_file(string)

def timer(string):
	string = str(string)
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	if args.silent == False:
		print('['+log_time+']'+BLUE(' >> ' )+string,end='\r')