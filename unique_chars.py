from sys import argv, exit

# unique_chars: Returns True if input string s has all unique chars.
def unique_chars(s):
	chars = {}
	for i in s:
		chars[i] = 1
	if len(chars.keys()) < len (s):
		return False
	return True
if len(argv) < 2:
	print "Usage: %s <string>\n" % argv[0]
	exit(1)

print "%r does%s have all unique chars.\n" % (argv[1], "" if unique_chars(argv[1]) else " not")
