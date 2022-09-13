// A simple initial PUT to analyze the properties of testing frameworks.

#include "stdio.h"
#include "stdlib.h"
#include "assert.h"
#include "string.h"
#include "PUT_generator_v0.407/initial_progr/argv-fuzz-inl.h"

int main(int argc, char** argv) { 
	AFL_INIT_SET0("a.out");
	long int N=2;
	if (argc > N) {
		assert(0==1);
		cocci_ref();
	}
	else {
		printf("Error: invalid number of arguments(%d, instead of %ld).\n",argc-1,N);
	}
	return 0;
}
