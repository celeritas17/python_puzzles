from sys import argv, exit

def is_rotation(s, t):
	if len(s) != len(t):
		return False
	if not s[0] in t:
		return False

	count_length = i = 0
	t_len = len(t)

	while t[i] != s[0]:
		i += 1
	while count_length < t_len and s[count_length] == t[i%t_len]:
		count_length += 1
		i += 1
	if count_length == t_len:
		return True
	return False

if len(argv) < 3:
	print "Usage: %s <string> <string>\n" % argv[0]
	exit(1)

print "%r is%s a rotation of %r\n" % (argv[2], "" if is_rotation(argv[1], argv[2]) else " not", argv[1])


