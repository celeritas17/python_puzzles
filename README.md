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

Compare is_permutation.py with a similar function in C:
	
	int is_permutation(char *s, char *t){
                int i;
                char *c, s_chars[256]; // ascii assumption.
                
                for (i = 0; i < 256; i++)
                        s_chars[i] = 0;
                
                for (c = s; *c; c++)
                        s_chars[*c]++;
                for (c = t; *c; c++){
                        if (--s_chars[*c] < 0)
                                return 0;
                }
                return 1;        
        }

compress.py: program to perform rudimentary string compression using character counts, e.g., aaaabbcc -> a4b2c2. Usage:

        python compress.py "stringToCompress"


