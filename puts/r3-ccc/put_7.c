#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { const char *str1=argv[1]; size_t l1=0; size_t h1=strlen(str1); if (h1>=1) { h1=h1-1; while(h1>l1) { if (str1[l1]!= str1[h1]) { printf("%d\n", argc); return 0; } l1=l1+1; h1=h1-1; } const char *str2=argv[2]; size_t l2=0; size_t h2=strlen(str2); if (h2>=2) { h2=h2-1; while(h2>l2) { if (str2[l2]!= str2[h2]) { printf("%d\n", argc); return 0; } l2=l2+1; h2=h2-1; } const char *str3=argv[3]; size_t l3=0; size_t h3=strlen(str3); if (h3>=3) { h3=h3-1; while(h3>l3) { if (str3[l3]!= str3[h3]) { printf("%d\n", argc); return 0; } l3=l3+1; h3=h3-1; } const char *str4=argv[4]; size_t l4=0; size_t h4=strlen(str4); if (h4>=4) { h4=h4-1; while(h4>l4) { if (str4[l4]!= str4[h4]) { printf("%d\n", argc); return 0; } l4=l4+1; h4=h4-1; } const char *str5=argv[5]; size_t l5=0; size_t h5=strlen(str5); if (h5>=5) { h5=h5-1; while(h5>l5) { if (str5[l5]!= str5[h5]) { printf("%d\n", argc); return 0; } l5=l5+1; h5=h5-1; } const char *str6=argv[6]; size_t l6=0; size_t h6=strlen(str6); if (h6>=6) { h6=h6-1; while(h6>l6) { if (str6[l6]!= str6[h6]) { printf("%d\n", argc); return 0; } l6=l6+1; h6=h6-1; } const char *str7=argv[7]; size_t l7=0; size_t h7=strlen(str7); if (h7>=7) { h7=h7-1; while(h7>l7) { if (str7[l7]!= str7[h7]) { printf("%d\n", argc); return 0; } l7=l7+1; h7=h7-1; } assert(0==1); } } } } } } } } else { printf("Error: invalid number of arguments"); } return 0;}
