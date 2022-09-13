#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 2 ; if (argc > N) { const char *str1=argv[1]; size_t l1=0; size_t h1=strlen(str1); if (h1>=7) { h1=h1-1; while(h1>l1) { if (str1[l1]!= str1[h1]) { printf("%d\n", argc); return 0; } l1=l1+1; h1=h1-1; } const char *str2=argv[2]; size_t l2=0; size_t h2=strlen(str2); if (h2<8) { printf("%d\n", argc); return 0; } h2=h2-1; while(h2>l2) { if (str2[l2]!= str2[h2]) { printf("%d\n", argc); return 0; } l2=l2+1; h2=h2-1; } assert(0==1); } } else { printf("Error: invalid number of arguments"); } return 0;}
