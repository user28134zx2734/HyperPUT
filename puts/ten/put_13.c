#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 10 ; if (argc > N) { const char *long_string1="18"; if (strcmp(argv[1],long_string1)==0) { const char *long_string2="199"; if (strcmp(argv[2],long_string2)==0) { long long int i13=atoll(argv[3]); long long int i23=155; if (i13==i23) { const char *long_string4="167"; if (strcmp(argv[4],long_string4)==0) { const char *str5=argv[5]; size_t l5=0; size_t h5=strlen(str5); if (h5>=5) { h5=h5-1; while(h5>l5) { if (str5[l5]!= str5[h5]) { printf("%d\n", argc); return 0; } l5=l5+1; h5=h5-1; } size_t c6=0; size_t count6=0; const size_t occurrences6=8; const char valid_char6='c'; for (c6=0; c6<strlen(argv[6]); c6++) { if (argv[6][c6] == valid_char6) count6++; } if (count6 != occurrences6) { printf("%d\n", argc); } else { long long int i17=atoll(argv[7]); long long int i27=69; if (i17==i27) { size_t c9=0; size_t count9=0; const size_t occurrences9=10; const char valid_char9='c'; for (c9=0; c9<strlen(argv[9]); c9++) { if (argv[9][c9] == valid_char9) count9++; } if (count9 != occurrences9) { printf("%d\n", argc); } else { size_t c10=0; size_t count10=0; const size_t occurrences10=6; const char valid_char10='c'; for (c10=0; c10<strlen(argv[10]); c10++) { if (argv[10][c10] == valid_char10) count10++; } if (count10 == occurrences10) { assert(0==1); } } } else { printf("%d\n", argc); } } } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } else { printf("Error: invalid number of arguments"); } return 0;}
