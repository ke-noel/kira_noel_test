'''
Question B

Given two version strings, determine whether the first is greater than, 
equal to or less than the second.
'''

import re

def get_relationship(s1,s2):
	tokens = []
	for s in (s1,s2):
		# remove alphabet chars and whitespace. Split on ., -, _
		s = re.sub(r'[a-zA-Z\s]', '', s)
		tokens.append(re.split('\.|-|_', s))

		if len(tokens[-1]) == 0:
			print('Error. No numbers detected in input %s' %s)
			exit(1)

		for i in range(len(tokens[-1])):
			tokens[-1][i] = int(tokens[-1][i])

	for t1,t2 in zip(tokens[0],tokens[1]):
		if t1 > t2:
			return 'greater than'
		elif t1 < t2:
			return'less than'
	return 'equals'


TESTS = (('5', '1', 'greater than'),	
	 ('1', '1', 'equals'),	
	 ('1', '2', 'less than'),	
	 ('1.1', '2.0', 'less than'),
	 ('1.12.3', '1.2.5', 'greater than'),
	 ('20200116-8845', '20200117-1', 'less than'),
	 ('v1.1', 'version3', 'less than'),
	 ('v1.1 ', 'v0.3', 'greater than'),
	 ('1_1-856', '1_1-900', 'less than'),
	 ('v1.35', '1_035', 'equals'),
	 ('0.0.0.0.1', '0.1', 'less than'))

def run_tests():
	for a,b,expected in TESTS:
		result = get_relationship(a,b)
		if result != expected:
			print('TEST FAILED - (%s,%s), got %s but expected %s' %(a,b,result,expected))
			break
	else:
		print('All tests pass.')
		

if __name__ == '__main__':
	run_tests()
