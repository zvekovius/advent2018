#!/usr/bin/env python


with open('input.txt', 'r') as input:
	answer = 0
	for line in input:
		answer += int(line)
	print(answer)
