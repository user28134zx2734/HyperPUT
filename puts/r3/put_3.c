#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 3 ; if (argc > N) { const char *long_string1="1"; if (strcmp(argv[1],long_string1)==0) { const char *long_string2="2"; if (strcmp(argv[2],long_string2)==0) { const char *long_string3="3"; if (strcmp(argv[3],long_string3)==0) { assert(0==1); } } } } else { printf("Error: invalid number of arguments"); } return 0;}
