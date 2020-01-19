'''
Question A

Given two lines (x1,x2), (x3,x4), determine if they overlap.
'''

class Line():
	def __init__(self,x1,x2):
		'''
		Make sure it's a valid line:
		    * x1, x2 are valid numbers
		    * x1 <= x2
		'''
		try:
			self.x1 = float(x1)
			self.x2 = float(x2)
			if self.x1 > self.x2: raise ValueError
		except ValueError:
			print('Error. Invalid inputs (%s,%s)' %(x1,x2))
			exit(1)

	def is_overlapping(self, l):
		if l.x1 < self.x1:
			return l.is_overlapping(self)
		else:
			# For (x1,x2),(x3,x4), x1<=x3<=x2
			return l.x1 <= self.x2 and l.x1 >= self.x1
	

def main():
	l1 = Line(input('x1: '), input('x2: '))
	l2 = Line(input('x3: '), input('x4: '))

	if l1.is_overlapping(l2):
		print('overlap')
	else:
		print('no overlap')
	

if __name__ == '__main__':
	main()
