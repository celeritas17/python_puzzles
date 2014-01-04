from sys import argv, exit

def compress(s):
	char_count = 0
	compressed = ''
	char = ''
	i = 0
	s_len = len(s)
	
	while i < s_len:
		char = s[i]
		while i < s_len and s[i] == char:
			char_count += 1
			i += 1
		compressed += (char + str(char_count))
		char_count = 0

	if len(compressed) < s_len:
		return compressed

	return s

if len(argv) < 2:
	print "Usage %s <string to compress>\n" % argv[0]
	exit(1)

print "%r compressed is %r" % (argv[1], compress(argv[1]))


