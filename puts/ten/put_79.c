#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 10 ; if (argc > N) { const char *str1=argv[1]; size_t l1=0; size_t h1=strlen(str1); if (h1>=3) { h1=h1-1; while(h1>l1) { if (str1[l1]!= str1[h1]) { printf("%d\n", argc); return 0; } l1=l1+1; h1=h1-1; } long long int i12=atoll(argv[2]); long long int i22=72; if (i12==i22) { long long int i13=atoll(argv[3]); long long int i23=178; if (i13==i23) { long long int i14=atoll(argv[4]); long long int i24=255; if (i14==i24) { long long int m5=177; long long int j5=0; for (; j5<m5; j5++) { printf("%lld\n", j5); } const char *long_string6="36"; if (strcmp(argv[6],long_string6)==0) { long long int i17=atoll(argv[7]); long long int i27=169; if (i17==i27) { const char *long_string8="160"; if (strcmp(argv[8],long_string8)==0) { long long int i19=atoll(argv[9]); long long int i29=16; if (i19==i29) { const char *str10=argv[10]; size_t l10=0; size_t h10=strlen(str10); if (h10<4) { printf("%d\n", argc); return 0; } h10=h10-1; while(h10>l10) { if (str10[l10]!= str10[h10]) { printf("%d\n", argc); return 0; } l10=l10+1; h10=h10-1; } assert(0==1); } } } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } } } else { printf("Error: invalid number of arguments"); } return 0;}
