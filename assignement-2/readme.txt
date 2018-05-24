Assignement 2 (SLAE ID - 1245):
- Create a reverse TCP shellcode
  1) reverse connects to configured ip and port
  2) execs shell on successfull connection
  
- Port number and ip address should be easily configurable

to build the shellcode:
$ ./compile.sh myreverse_tcp

to get the shellcode:
$ ./getShellcode myreverse_tcp
copy and paste the output from the command above to shellcode.c

compile shellcode.c:
$ gcc -m32 -fno-stack-protector -z execstack -o shellcode shellcode.c -g

run shellcode:
$ ./shellcode

to change the shellcode listen port:
$ ./getShellcode myreverse_tcp
copy and paste the output from the command above to change_port.py
$ python change_port.py -p 4444 -a 127.0.0.1
copy and paste the output from the command above to shellcode.c
