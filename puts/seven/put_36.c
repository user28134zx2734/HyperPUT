#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=75; if (i11==i21) { const char *str2=argv[2]; size_t l2=0; size_t h2=strlen(str2); if (h2<3) { printf("%d\n", argc); return 0; } h2=h2-1; while(h2>l2) { if (str2[l2]!= str2[h2]) { printf("%d\n", argc); return 0; } l2=l2+1; h2=h2-1; } const char *long_string3="59"; if (strcmp(argv[3],long_string3)==0) { const char *long_string5="185"; if (strcmp(argv[5],long_string5)==0) { size_t c6=0; size_t count6=0; const size_t occurrences6=4; const char valid_char6='c'; for (c6=0; c6<strlen(argv[6]); c6++) { if (argv[6][c6] == valid_char6) count6++; } if (count6 != occurrences6) { printf("%d\n", argc); } else { long long int i17=atoll(argv[7]); long long int i27=160; if (i17==i27) { assert(0==1); } } } else { printf("%d\n", argc); } } } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
