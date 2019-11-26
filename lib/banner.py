from lib import logger

def header(string):
	print(logger.RED('  ██████ ▓█████▄  ▄▄▄▄   '))
	print(logger.RED('▒██    ▒ ▒██▀ ██▌▓█████▄ '))
	print(logger.RED('░ ▓██▄   ░██   █▌▒██▒ ▄██ %s') % logger.YELLOW(string))
	print(logger.RED('  ▒   ██▒░▓█▄   ▌▒██░█▀  '))
	print(logger.RED('▒██████▒▒░▒████▓ ░▓█  ▀█▓'))
	print(logger.RED('▒ ▒▓▒ ▒ ░ ▒▒▓  ▒ ░▒▓███▀▒'))
	print(logger.RED('░ ░▒  ░ ░ ░ ▒  ▒ ▒░▒   ░ '))
	print(logger.RED('░  ░  ░   ░ ░  ░  ░    ░ '))
	print(logger.RED('      ░     ░     ░      '))

