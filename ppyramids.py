#!/usr/bin/env python

import sys

text = input("What do you want to print?")
space = " "

#width in characters
width = 181
r = int(width/len(text))
repetition = int(input("How many repetitions?"))

for i in range(repetition):
	for i in range(r+1):
		print(text*i)

	for i in range(r-1):
		print(text*(r-i-1), end=" ")
		print(space*i)

#if __name__ == "__main__":
    #main()
