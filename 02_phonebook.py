import sys
import re
import collections

if len(sys.argv) <2:
	print('usage: python3 {}'.format(sys.argv[1]))
	exit()
try:
	f = open(sys.argv[1])
except:
	print('cannot open file {}'.format(sys.argv[1]))

firstnames = [];
lastnames = [];
while True:
	line = f.readline()
	if (len(line) == 0):
		break;
	line = line.rstrip('\n')
	pair = re.split('[ \t]*', line)
	print('pair:{} {}'.format(pair, len(pair)))
	


for item, count in collections.Counter(firstnames).items():
	if count > 1:
		print(item)

print(firstnames)
