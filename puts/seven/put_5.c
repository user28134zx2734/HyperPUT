#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=193; if (i11==i21) { const char *str2=argv[2]; size_t l2=0; size_t h2=strlen(str2); if (h2>=6) { h2=h2-1; while(h2>l2) { if (str2[l2]!= str2[h2]) { printf("%d\n", argc); return 0; } l2=l2+1; h2=h2-1; } const char *str3=argv[3]; size_t l3=0; size_t h3=strlen(str3); if (h3>=2) { h3=h3-1; while(h3>l3) { if (str3[l3]!= str3[h3]) { printf("%d\n", argc); return 0; } l3=l3+1; h3=h3-1; } const char *str4=argv[4]; size_t l4=0; size_t h4=strlen(str4); if (h4>=2) { h4=h4-1; while(h4>l4) { if (str4[l4]!= str4[h4]) { printf("%d\n", argc); return 0; } l4=l4+1; h4=h4-1; } const char *long_string6="222"; if (strcmp(argv[6],long_string6)==0) { long long int m7=175; long long int j7=0; while (j7<m7) { printf("%lld\n", j7); j7++; } assert(0==1); } } } } } } else { printf("Error: invalid number of arguments"); } return 0;}
