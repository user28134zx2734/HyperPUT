#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 3 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=1; if (i11==i21) { long long int i12=atoll(argv[2]); long long int i22=2; if (i12==i22) { long long int i13=atoll(argv[3]); long long int i23=3; if (i13==i23) { assert(0==1); } } } } else { printf("Error: invalid number of arguments"); } return 0;}
