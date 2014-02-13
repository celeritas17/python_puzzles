from sys import argv, exit

def decompress(s):
	char_count = 0
	decompressed = ''
	char = ''
	i = 0
	s_len = len(s)

	while i < s_len:
		char = s[i]
		if (i + 1) < s_len and s[i] == s[i + 1]:
			for j in range(0, int(s[i + 2]) + 2):
				decompressed += char
			i += 3
		else:
			decompressed += char
			i += 1

	return decompressed 

if len(argv) < 2:
	print "Usage %s <string to decompress>\n" % argv[0]
	exit(1)

print "%r decompressed is %r" % (argv[1], decompress(argv[1]))