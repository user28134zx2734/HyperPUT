#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
int main(int argc, char* argv[]) {
int N = 10 ; if (argc > N) { long long int i11=atoll(argv[1]); long long int i21=243; if (i11==i21) { long long int i12=atoll(argv[2]); long long int i22=110; if (i12==i22) { const char *str3=argv[3]; size_t l3=0; size_t h3=strlen(str3); if (h3<5) { printf("%d\n", argc); return 0; } h3=h3-1; while(h3>l3) { if (str3[l3]!= str3[h3]) { printf("%d\n", argc); return 0; } l3=l3+1; h3=h3-1; } size_t c4=0; size_t count4=0; const size_t occurrences4=2; const char valid_char4='c'; for (c4=0; c4<strlen(argv[4]); c4++) { if (argv[4][c4] == valid_char4) count4++; } if (count4 != occurrences4) { printf("%d\n", argc); } else { const char *str6=argv[6]; size_t l6=0; size_t h6=strlen(str6); if (h6<1) { printf("%d\n", argc); return 0; } h6=h6-1; while(h6>l6) { if (str6[l6]!= str6[h6]) { printf("%d\n", argc); return 0; } l6=l6+1; h6=h6-1; } long long int i17=atoll(argv[7]); long long int i27=162; if (i17==i27) { long long int i19=atoll(argv[9]); long long int i29=54; if (i19==i29) { long long int i110=atoll(argv[10]); long long int i210=146; if (i110==i210) { assert(0==1); } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } } } else { printf("%d\n", argc); } } else { printf("%d\n", argc); } } else { printf("Error: invalid number of arguments"); } return 0;}
