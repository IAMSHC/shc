import re
for test_string in ['joyeta@gmail.com']:
	if re.match(r'\S{6}@\S{5}.\S{3}', test_string):
		print test_string,' is a valid email_id'
	else:
		print test_string, "rejected"