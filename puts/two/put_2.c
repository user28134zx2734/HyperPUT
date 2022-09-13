#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 2 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=173; if (i11==i21) { const char *str2=argv[2]; size_t l2=0; size_t h2=strlen(str2); if (h2>=7) { h2=h2-1; while(h2>l2) { if (str2[l2]!= str2[h2]) { printf("%d\n", argc); return 0; } l2=l2+1; h2=h2-1; } assert(0==1); } } } else { printf("Error: invalid number of arguments"); } return 0;}
