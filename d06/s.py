# Youtube: https://youtu.be/5olAYPViH4g

import argparse, math, sys, re, functools, operator, itertools, bisect
from collections import defaultdict, Counter
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

def solve1(t, d):
	ans = 0
	for i in range(t + 1):
		assert t - i >= 0
		if i * (t - i) > d:
			ans += 1
	return ans

def part_1(lines):
	s = 1
	for t, d in zip(map(int, lines[0].split()[1:]),
					map(int, lines[1].split()[1:])):
		s *= solve1(t, d)
	return s

def solve2(t, d):
	# f > 0 is win
	f = lambda x: (x * (t - x) - d)
	assert f(0) <= 0
	assert f(t) <= 0
	# maxima:
	# solve(diff((x * (t - x) - d), x) = 0, x);
	# Gives x = t / 2 is the maximum of this parabola
	assert f(t // 2) > 0
	l0 = 0
	l1 = t // 2
	while l0 < l1 - 1:
		# Assume f(l0) <= 0 and f(l1) > 0
		m = (l0 + l1) // 2
		if f(m) <= 0:
			l0 = m
		else:
			l1 = m
	r0 = t // 2
	r1 = t
	while r0 < r1 - 1:
		# Assume f(r0) > 0 and f(r1) <= 0
		m = (r0 + r1) // 2
		if f(m) > 0:
			r0 = m
		else:
			r1 = m
	return r0 - l0

def solve2O1(t, d):
	# We want x s.t. x * (t - x) > d
	# Let maxima solve (x * (t - x) - d = 0)
	# (%i4) solve(x * (t - x) - d = 0, x);
	# (%o4) [x = -(sqrt(t^2-4*d)-t)/2,x = (sqrt(t^2-4*d)+t)/2]
	from math import sqrt
	x0 = -(sqrt(t**2-4*d)-t)/2
	x1 = (sqrt(t**2-4*d)+t)/2
	l0 = int(x0)
	l1 = l0 + 1
	r0 = int(x1)
	r1 = r0 + 1
	# May not work well if x0 or x1 happens to be integer.
	f = lambda x: (x * (t - x) - d)
	assert f(l0) <= 0
	assert f(l1) > 0
	assert f(r0) > 0
	assert f(r1) <= 0
	return r0 - l0

def part_2(lines):
	s = 0
	t = int(''.join(lines[0].split()[1:]))
	d = int(''.join(lines[1].split()[1:]))
	# I submitted using solve1, didn't take too long to finish.
	s = solve1(t, d)
	# Then I wrote solve2 using bisection, thinking it is the optimal solution.
	assert s == solve2(t, d)
	# After posting the Youtube video, I realize there is an O(1) solution.
	assert s == solve2O1(t, d)
	return s

if __name__ == '__main__':
	main()

