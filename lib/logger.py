from time import gmtime, strftime

colour_red = "\033[1;31m"
colour_blue = "\033[1;34m"
colour_yellow = "\033[1;33m"
colour_green = "\033[1;32m"
colour_magenta = "\033[1;35m"
colour_remove= "\033[0m"

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
	print('['+log_time+']'+BLUE(' >> ' )+string)

def green(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	print('['+log_time+']'+GREEN(' >> ' )+string)

def red(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	print('['+log_time+']'+RED(' >> ' )+string)

def yellow(string):
	log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
	print('['+log_time+']'+YELLOW(' >> ' )+string)