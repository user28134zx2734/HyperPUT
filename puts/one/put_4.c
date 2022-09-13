#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 1 ; if (argc > N) { const char *str1=argv[1]; size_t l1=0; size_t h1=strlen(str1); if (h1<8) { printf("%d\n", argc); return 0; } h1=h1-1; while(h1>l1) { if (str1[l1]!= str1[h1]) { printf("%d\n", argc); return 0; } l1=l1+1; h1=h1-1; } assert(0==1); } else { printf("Error: invalid number of arguments"); } return 0;}
