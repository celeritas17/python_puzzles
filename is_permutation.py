from sys import exit, argv

# is_permutation: returns True if t is a permutation (anagram) of s,
# False otherwise.
def is_permutation(s, t):
	t_chars = {}
	s_chars = {}

	# Record characters in s and t
	for i in s:
		s_chars[i] = 0
	for i in t:
		t_chars[i] = 0
	
	# Count occurrences of each char
	for i in s:
		s_chars[i] += 1
	for i in t:
		t_chars[i] += 1
	
	if set(s_chars.keys()) == set(t_chars.keys()):
		for i in s_chars.keys():
			if not s_chars[i] == t_chars[i]:
				return False
	else:
		return False
	return True

if len(argv) < 3:
	print "Usage: %s <string> <string>\n" % argv[0]
	exit(1)

print "%s is%s a permutation of %s\n" % (argv[1], "" if is_permutation(argv[1], argv[2]) else " not", argv[2])
