#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 10 ; if (argc > N) { const char *long_string1="2"; if (strcmp(argv[1],long_string1)==0) { const char *long_string3="85"; if (strcmp(argv[3],long_string3)==0) { const char *long_string4="203"; if (strcmp(argv[4],long_string4)==0) { const char *long_string5="177"; if (strcmp(argv[5],long_string5)==0) { long long int i16=atoll(argv[6]); long long int i26=101; if (i16==i26) { const char *long_string7="68"; if (strcmp(argv[7],long_string7)==0) { long long int i18=atoll(argv[8]); long long int i28=19; if (i18==i28) { const char *long_string9="147"; if (strcmp(argv[9],long_string9)==0) { assert(0==1); } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
