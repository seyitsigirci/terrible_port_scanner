#/bin/python3

import sys
import socket


if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments")
	print("Syntax : python3 scanner.py <ip> ")
	sys.exit()

print("-" *50)
print("Scanning target"+target)
print("-" *50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result= s.connect_ex((target,port))
		print("Checking port {}".format(port))
		if result ==0:
			print("Port {} is open.".format(port))
		s.close()
except KeyboardInterrupt:
	print("Exiting program")
	sys.exit()
except socket.gaierror:
	print("Couldn't find hostname")
	sys.exit()
except socket.error:
	print("Couldn't connect to the server")
	sys.exit()
