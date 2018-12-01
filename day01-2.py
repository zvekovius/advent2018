#!/usr/bin/env python

with open('input.txt', 'r') as input:
	input_list = []
	for line in input:
		input_list.append(int(line))

repeat = None
freq_seen = []
answer = 0
iteration = 0
while not repeat:
	iteration += 1
	for item in input_list:
		answer += item
		if answer not in freq_seen:
			freq_seen.append(answer)
		else:
			repeat = answer
			break
print(repeat)
