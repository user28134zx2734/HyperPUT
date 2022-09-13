#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { long long int i12=atoll(argv[2]); long long int i22=176; if (i12==i22) { const char *str5=argv[5]; size_t l5=0; size_t h5=strlen(str5); if (h5<8) { printf("%d\n", argc); return 0; } h5=h5-1; while(h5>l5) { if (str5[l5]!= str5[h5]) { printf("%d\n", argc); return 0; } l5=l5+1; h5=h5-1; } assert(0==1); } } else { printf("Error: invalid number of arguments"); } return 0;}
