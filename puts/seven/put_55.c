#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=228; if (i11==i21) { const char *long_string3="207"; if (strcmp(argv[3],long_string3)==0) { const char *str4=argv[4]; size_t l4=0; size_t h4=strlen(str4); if (h4<10) { printf("%d\n", argc); return 0; } h4=h4-1; while(h4>l4) { if (str4[l4]!= str4[h4]) { printf("%d\n", argc); return 0; } l4=l4+1; h4=h4-1; } size_t c5=0; size_t count5=0; const size_t occurrences5=4; const char valid_char5='c'; for (c5=0; c5<strlen(argv[5]); c5++) { if (argv[5][c5] == valid_char5) count5++; } if (count5 != occurrences5) { printf("%d\n", argc); } else { long long int i16=atoll(argv[6]); long long int i26=80; if (i16==i26) { long long int i17=atoll(argv[7]); long long int i27=74; if (i17==i27) { assert(0==1); } } } } } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
