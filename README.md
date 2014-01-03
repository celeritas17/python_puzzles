##Solutions to programming puzzles in python for fun and practice

permutations.py: program to print all permutations of a string. 
Usage:

	python permutations.py "example"

unique_chars.py: Program to determine if a string has all unique characters.
Usage:
G
	python unique_chars.py "test_string"

is_permutation.py: program to determine if one string is a permutation of another string. Usage:

	python is_permutation.py "string1" "string2"

Compare is_permutation.py with a similar program in C:
	
	#include <stdio.h>
	#include <stdlib.h>


	int main(int argc, char *argv[]){
        	if (argc < 3){
                	printf("Usage: %s <string> <string>\n", argv[0]);
                	exit(1);
        	}
        	printf("\'%s\' is%s a permutation of \'%s\'\n", argv[1], (is_permutation(argv[1], argv[2])) ? "" : " not", argv[2]);
        	return 0;
	}

	int is_permutation(char *s, char *t){
        	int i, s_chars[127], t_chars[127];
        	char *c;
        
        	for (i = 0; i < 127; i++)
                	s_chars[i] = t_chars[i] = 0;
        
        	for (c = s; *c; c++)
                	s_chars[*c]++;
        	for (c = t; *c; c++)
                	t_chars[*c]++;

        	for (i = 0; i < 127; i++){
                	if (s_chars[i] != t_chars[i])
                        	return 0;
        	}
        	return 1;        
	}



