#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 7 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=73; if (i11==i21) { size_t c2=0; size_t count2=0; const size_t occurrences2=2; const char valid_char2='c'; for (c2=0; c2<strlen(argv[2]); c2++) { if (argv[2][c2] == valid_char2) count2++; } if (count2 == occurrences2) { size_t c4=0; size_t count4=0; const size_t occurrences4=9; const char valid_char4='c'; for (c4=0; c4<strlen(argv[4]); c4++) { if (argv[4][c4] == valid_char4) count4++; } if (count4 != occurrences4) { printf("%d\n", argc); } else { size_t c5=0; size_t count5=0; const size_t occurrences5=7; const char valid_char5='c'; for (c5=0; c5<strlen(argv[5]); c5++) { if (argv[5][c5] == valid_char5) count5++; } if (count5 == occurrences5) { long long int i16=atoll(argv[6]); long long int i26=18; if (i16==i26) { size_t c7=0; size_t count7=0; const size_t occurrences7=5; const char valid_char7='c'; for (c7=0; c7<strlen(argv[7]); c7++) { if (argv[7][c7] == valid_char7) count7++; } if (count7 == occurrences7) { assert(0==1); } } } } } } } else { printf("Error: invalid number of arguments"); } return 0;}
