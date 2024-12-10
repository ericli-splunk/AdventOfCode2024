# Youtube: https://youtu.be/4D0jV_rAU6g

import argparse, math, sys, re, functools, operator, itertools, heapq
from collections import defaultdict, Counter, deque
#sys.setrecursionlimit(100000000)
#A = list(map(int, input().split()))
#T = int(input())

def read_lines(f):
	while True:
		line = f.readline()
		if not line:
			break
		assert line[-1] == '\n'
		yield line[:-1]

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-1', '--one', action='store_true', help='Only part 1')
	parser.add_argument('-2', '--two', action='store_true', help='Only part 2')
	parser.add_argument('input_file', nargs='?')
	args = parser.parse_args()
	if args.input_file is not None:
		f = open(args.input_file)
	else:
		f = sys.stdin
	lines = list(read_lines(f))
	if not args.two:
		print(part_1(lines))
	if not args.one:
		print(part_2(lines))

def part_1(lines):
	s = 0
	for i in lines:
		for j, k in re.findall(r'mul\((\d+),(\d+)\)', i):
			s += int(j) * int(k)
	return s

def part_2(lines):
	s = 0
	en = True
	for i in lines:
		exp = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
		for j, k, l, m in re.findall(exp, i):
			if l:
				assert l == 'do()'
				assert not any([j, k, m])
				en = True
				#print(l)
			elif m:
				assert m == "don't()"
				assert not any([j, k, l])
				en = False
				#print(m)
			else:
				assert j and k
				#print(j, k)
				if en:
					s += int(j) * int(k)
	return s

if __name__ == '__main__':
	main()

