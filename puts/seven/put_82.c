#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=245; if (i11==i21) { const char *str3=argv[3]; size_t l3=0; size_t h3=strlen(str3); if (h3>=3) { h3=h3-1; while(h3>l3) { if (str3[l3]!= str3[h3]) { printf("%d\n", argc); return 0; } l3=l3+1; h3=h3-1; } const char *long_string5="153"; if (strcmp(argv[5],long_string5)==0) { const char *str6=argv[6]; size_t l6=0; size_t h6=strlen(str6); if (h6<8) { printf("%d\n", argc); return 0; } h6=h6-1; while(h6>l6) { if (str6[l6]!= str6[h6]) { printf("%d\n", argc); return 0; } l6=l6+1; h6=h6-1; } const char *long_string7="205"; if (strcmp(argv[7],long_string7)==0) { assert(0==1); } } } } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
