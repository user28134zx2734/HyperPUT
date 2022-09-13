#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 2 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=173; if (i11==i21) { long long int i12=atoll(argv[2]); long long int i22=213; if (i12==i22) { assert(0==1); } else { printf("%d\n", argc); } } } else { printf("Error: invalid number of arguments"); } return 0;}
