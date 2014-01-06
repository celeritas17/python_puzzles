from sys import argv, exit

# insert: returns a list of strings formed by inserting the
# character c at each index of string s (including after s)
# (e.g., insert('s', 'cat') returns ['scat', 'csat', 'cast', 'cats'])
def insert(c, s):
	inserts = []
	for i in range(0, len(s) + 1):
		inserts.append(s[:i] + c + s[i:])
	return inserts

# Returns a list of all permutations of string s
def permutations(s):
	if len(s) == 1:
		return [s]
	elif len(s) == 2:
		return [s, s[::-1]]
	else:
		perms = []
		for t in permutations(s[1:]):
			perms += insert(s[0], t)
		return perms

if len(argv) < 2:
	print "Usage: python %s <string>\n" % argv[0]
	exit(1)

print permutations(argv[1])
