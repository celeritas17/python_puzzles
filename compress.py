from sys import argv, exit

# compress: returns a compressed version of string s
# (e.g., aaabbcc -> a3b2c2)
def compress(s):
	
	char_count = 0
	compressed = []
	i = 0
	s_len = len(s)
	
	while i < s_len:
		char = s[i]
		while i < s_len and s[i] == char:
			char_count += 1
			i += 1
		chars = [char]
		chars.append(str(char_count))
		compressed.append(''.join(chars))
		char_count = 0

	if len(compressed) < s_len:
		return ''.join(compressed)

	return s

if len(argv) < 2:
	print "Usage %s <string to compress>\n" % argv[0]
	exit(1)

print "%r compressed is %r" % (argv[1], compress(argv[1]))


