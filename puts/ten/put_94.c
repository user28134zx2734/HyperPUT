#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 10 ; if (argc > N) { long long int i12=atoll(argv[2]); long long int i22=46; if (i12==i22) { const char *long_string3="149"; if (strcmp(argv[3],long_string3)==0) { long long int i16=atoll(argv[6]); long long int i26=123; if (i16==i26) { const char *long_string7="134"; if (strcmp(argv[7],long_string7)==0) { long long int i18=atoll(argv[8]); long long int i28=99; if (i18==i28) { size_t c9=0; size_t count9=0; const size_t occurrences9=1; const char valid_char9='c'; for (c9=0; c9<strlen(argv[9]); c9++) { if (argv[9][c9] == valid_char9) count9++; } if (count9 == occurrences9) { assert(0==1); } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } } else { printf("Error: invalid number of arguments"); } return 0;}
