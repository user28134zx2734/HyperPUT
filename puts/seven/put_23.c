#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { const char *long_string1="255"; if (strcmp(argv[1],long_string1)==0) { const char *long_string2="148"; if (strcmp(argv[2],long_string2)==0) { const char *long_string3="2"; if (strcmp(argv[3],long_string3)==0) { long long int i14=atoll(argv[4]); long long int i24=200; if (i14==i24) { const char *long_string5="240"; if (strcmp(argv[5],long_string5)==0) { long long int i16=atoll(argv[6]); long long int i26=234; if (i16==i26) { const char *long_string7="165"; if (strcmp(argv[7],long_string7)==0) { assert(0==1); } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } else { printf("Error: invalid number of arguments"); } return 0;}
