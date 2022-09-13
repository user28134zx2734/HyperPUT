#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 1 ; if (argc > N) { const char *long_string1="184"; if (strcmp(argv[1],long_string1)==0) { assert(0==1); } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
