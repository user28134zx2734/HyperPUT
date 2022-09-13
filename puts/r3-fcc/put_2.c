#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 2 ; if (argc > N) { size_t c1=0; size_t count1=0; const size_t occurrences1=1; const char valid_char1='c'; for (c1=0; c1<strlen(argv[1]); c1++) { if (argv[1][c1] == valid_char1) count1++; } if (count1 == occurrences1) { size_t c2=0; size_t count2=0; const size_t occurrences2=2; const char valid_char2='c'; for (c2=0; c2<strlen(argv[2]); c2++) { if (argv[2][c2] == valid_char2) count2++; } if (count2 == occurrences2) { assert(0==1); } } } else { printf("Error: invalid number of arguments"); } return 0;}
