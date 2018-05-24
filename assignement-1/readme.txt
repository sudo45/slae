Assignement 1 (SLAE ID - 1245):
- Create a bind TCP shellcode
  1) binds to a port
  2) execs shell on incoming connection
  
- Port number should be easily configurable

to build the shellcode:
$ ./compile.sh mybindtcp

to get the shellcode:
$ ./getShellcode mybindtcp
copy and paste the output from the command above to shellcode.c

compile shellcode.c:
$ gcc -m32 -fno-stack-protector -z execstack -o shellcode shellcode.c -g

run shellcode:
$ ./shellcode

to change the shellcode listen port (default is 5555):
$ ./getShellcode mybindtcp
copy and paste the output from the command above to change_port.py
$ python change_port.py 4444
copy and paste the output from the command above to shellcode.c

