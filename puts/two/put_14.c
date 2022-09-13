#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 2 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=213; if (i11==i21) { const char *long_string2="137"; if (strcmp(argv[2],long_string2)==0) { assert(0==1); } } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
