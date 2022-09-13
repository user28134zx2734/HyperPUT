#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 10 ; if (argc > N) { const char *long_string2="152"; if (strcmp(argv[2],long_string2)==0) { long long int i13=atoll(argv[3]); long long int i23=72; if (i13==i23) { long long int i14=atoll(argv[4]); long long int i24=247; if (i14==i24) { const char *long_string5="28"; if (strcmp(argv[5],long_string5)==0) { const char *long_string6="193"; if (strcmp(argv[6],long_string6)==0) { long long int i17=atoll(argv[7]); long long int i27=240; if (i17==i27) { const char *str8=argv[8]; size_t l8=0; size_t h8=strlen(str8); if (h8<6) { printf("%d\n", argc); return 0; } h8=h8-1; while(h8>l8) { if (str8[l8]!= str8[h8]) { printf("%d\n", argc); return 0; } l8=l8+1; h8=h8-1; } size_t c9=0; size_t count9=0; const size_t occurrences9=8; const char valid_char9='c'; for (c9=0; c9<strlen(argv[9]); c9++) { if (argv[9][c9] == valid_char9) count9++; } if (count9 != occurrences9) { printf("%d\n", argc); } else { const char *long_string10="146"; if (strcmp(argv[10],long_string10)==0) { assert(0==1); } } } } } } else { printf("%d\n", argc); } } } } else { printf("Error: invalid number of arguments"); } return 0;}
