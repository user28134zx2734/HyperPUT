#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 5 ; if (argc > N) { size_t c1=0; size_t count1=0; const size_t occurrences1=1; const char valid_char1='c'; for (c1=0; c1<strlen(argv[1]); c1++) { if (argv[1][c1] == valid_char1) count1++; } if (count1 == occurrences1) { size_t c2=0; size_t count2=0; const size_t occurrences2=2; const char valid_char2='c'; for (c2=0; c2<strlen(argv[2]); c2++) { if (argv[2][c2] == valid_char2) count2++; } if (count2 == occurrences2) { size_t c3=0; size_t count3=0; const size_t occurrences3=3; const char valid_char3='c'; for (c3=0; c3<strlen(argv[3]); c3++) { if (argv[3][c3] == valid_char3) count3++; } if (count3 == occurrences3) { size_t c4=0; size_t count4=0; const size_t occurrences4=4; const char valid_char4='c'; for (c4=0; c4<strlen(argv[4]); c4++) { if (argv[4][c4] == valid_char4) count4++; } if (count4 == occurrences4) { size_t c5=0; size_t count5=0; const size_t occurrences5=5; const char valid_char5='c'; for (c5=0; c5<strlen(argv[5]); c5++) { if (argv[5][c5] == valid_char5) count5++; } if (count5 == occurrences5) { assert(0==1); } } } } } } else { printf("Error: invalid number of arguments"); } return 0;}
