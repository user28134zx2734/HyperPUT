/* ================================================================================================
 *
 *  FILE:
 *       hyperput.h
 *
 *  DESCRIPTION:
 *       List of transformations to produce PUTs.
 *
 * ================================================================================================
*/



// List of available Control Flow Graph transformations

#define INIT(N_ARGS,HOLE)					\
	int N = N_ARGS ; 				 	\
	if (argc > N) {						\
		HOLE						\
	}							\
	else {							\
		printf("Error: invalid number of arguments");	\
	}							\
	return 0;						
								

#define NONE(ARG,VALUE,VAR_N,HOLE) \
	HOLE			   \

#define IC(ARG,VALUE,VAR_N,HOLE)			\
	long long int i1##VAR_N=atoll(argv[ARG]);	\
	long long int i2##VAR_N=VALUE;			\
	if (i1##VAR_N==i2##VAR_N) {			\
		HOLE					\
	}					



#define IC2(ARG,VALUE,VAR_N,HOLE)			\
	long long int i1##VAR_N=atoll(argv[ARG]);	\
	long long int i2##VAR_N=VALUE;			\
	if (i1##VAR_N==i2##VAR_N) {			\
		HOLE					\
	}						\
	else {						\
		printf("%d\n", argc);			\
	}				


#define SC(ARG, VALUE, VAR_N, HOLE)			\
	const char *long_string##VAR_N=VALUE;		\
	if (strcmp(argv[ARG],long_string##VAR_N)==0) {	\
		HOLE					\
	}


#define SC2(ARG, VALUE, VAR_N, HOLE)			\
	const char *long_string##VAR_N=VALUE;		\
	if (strcmp(argv[ARG],long_string##VAR_N)==0) {	\
		HOLE					\
	} else {					\
		printf("%d\n", argc);			\
	}

#define WAC(ARG, VALUE, VAR_N, HOLE)			\
	long long int m##VAR_N=VALUE;			\
	long long int j##VAR_N=0;			\
	while (j##VAR_N<m##VAR_N) {			\
		printf("%lld\n", j##VAR_N);		\
		j##VAR_N++;				\
	} 						\
	HOLE						\


#define FAC(ARG, VALUE, VAR_N, HOLE)										\
	long long int m##VAR_N=VALUE;			\
	long long int j##VAR_N=0;			\
	for (; j##VAR_N<m##VAR_N; j##VAR_N++) {		\
		printf("%lld\n", j##VAR_N);		\
	} 						\
	HOLE						\
 								

// Verify if the input string argv[ARG] is palindrome (with length len=>VALUE) by comparing its characters
// If argv[ARG] is palindrome, execute the next transformation. Otherwise, terminate the program.
// VALUE must be greater than zero
#define CCC(ARG, VALUE, VAR_N, HOLE)					\
	const char *str##VAR_N=argv[ARG];				\
	size_t l##VAR_N=0;						\
	size_t h##VAR_N=strlen(str##VAR_N);				\
	if (h##VAR_N>=VALUE) {						\
		h##VAR_N=h##VAR_N-1;						\
		while(h##VAR_N>l##VAR_N) {					\
			if (str##VAR_N[l##VAR_N]!= str##VAR_N[h##VAR_N]) {	\
				printf("%d\n", argc);				\
				return 0;					\
			}							\
			l##VAR_N=l##VAR_N+1;					\
			h##VAR_N=h##VAR_N-1;					\
		}								\
		HOLE  								\
	}


// Verify if the input string argv[ARG] is palindrome (with length len=>VALUE) by comparing its characters
// If argv[ARG] is palindrome, execute the next transformation. Otherwise, terminate the program.
// VALUE must be greater than zero
#define CCC2(ARG, VALUE, VAR_N, HOLE)					\
	const char *str##VAR_N=argv[ARG];				\
	size_t l##VAR_N=0;						\
	size_t h##VAR_N=strlen(str##VAR_N);				\
	if (h##VAR_N<VALUE) {						\
		printf("%d\n", argc);					\
		return 0;						\
	}								\
	h##VAR_N=h##VAR_N-1;						\
	while(h##VAR_N>l##VAR_N) {					\
		if (str##VAR_N[l##VAR_N]!= str##VAR_N[h##VAR_N]) {	\
			printf("%d\n", argc);				\
			return 0;					\
		}							\
		l##VAR_N=l##VAR_N+1;					\
		h##VAR_N=h##VAR_N-1;					\
	}								\
	HOLE



#define FCC(ARG, VALUE, VAR_N, HOLE)						\
		size_t c##VAR_N=0;						\
		size_t count##VAR_N=0;						\
		const size_t occurrences##VAR_N=VALUE;				\
		const char valid_char##VAR_N='c';				\
		for (c##VAR_N=0; c##VAR_N<strlen(argv[ARG]); c##VAR_N++) {	\
			if (argv[ARG][c##VAR_N] == valid_char##VAR_N)		\
				count##VAR_N++;					\
		}								\
		if (count##VAR_N == occurrences##VAR_N) {			\
			HOLE							\
		}								\


#define FCC2(ARG, VALUE, VAR_N, HOLE)						\
		size_t c##VAR_N=0;						\
		size_t count##VAR_N=0;						\
		const size_t occurrences##VAR_N=VALUE;				\
		const char valid_char##VAR_N='c';				\
		for (c##VAR_N=0; c##VAR_N<strlen(argv[ARG]); c##VAR_N++) {	\
			if (argv[ARG][c##VAR_N] == valid_char##VAR_N)		\
				count##VAR_N++;					\
		}								\
		if (count##VAR_N != occurrences##VAR_N) {			\
			printf("%d\n", argc);					\
		} else {							\
			HOLE							\
		}								\


#define AC(ARG, VALUE, VAR_N, HOLE)						\
	int i1##VAR_N=atoi(argv[ARG]);						\
	int i2##VAR_N=VALUE;							\
	if (EQUATION(VAR_N)) {							\
		HOLE								\
	}									\


// Bug transformations 

#define ABORT_BUG 			\
	abort();			\	

#define ASSERT_BUG 			\
	assert(0==1);			\

#define BO_BUG(VAR_N) 			\
	int array##VAR_N[3];		\
	array##VAR_N[4];		\



// Obfuscation transformations

#define DELAY_OBF(SEC, HOLE) \
	sleep(SEC);    	     \
	HOLE


