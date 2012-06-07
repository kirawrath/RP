import sys
from k_means import *
from utilities import parse_file, use_ibl

def main():
	filename='iris2d.data'
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		print 'Assuming filename as \'iris2d.data\''
	interval=[0]*2

	print 'Do you want to choose a \'k\' or an interval of \'k\'s?'
	choice = raw_input('type \'k\' or \'i\': ')
	if choice == 'k':
		k = int(raw_input('Type a value of k: '))
		interval[0]=interval[1]=k
	elif choice == 'i':
		interval = raw_input('Type the two numbers of the interval: ')
		interval = map(lambda a: int(a), interval.split())
		assert len(interval) == 2
	else:
		print 'Assuming k=3'
		interval[0]=interval[1]=3
		
	
	print 'f0,f,d1,d2'
	dots=None
	for k in range(interval[0], interval[1]+1):
		dots = parse_file(filename)
		print 'k =',k
		result = k_means(k, dots)
		print result
		if result[0] > result[1]:
			print 'f0 is greater than the f from the table,',
			print 'so we can reject the hypothesis that there is no group (it\'s all OK).'
		else:
			print 'f0 is smaller than the f from the table, your K is likely to be inappropriated.'

	if len(dots[0].pos) == 2:
		choice = raw_input('Display last result with IBL1? [y/N] ')
		if choice == 'y':
			use_ibl(dots)

				

if __name__ == '__main__':
	main()
