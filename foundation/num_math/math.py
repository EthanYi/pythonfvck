#!/usr/bin/env python
#coding:utf-8

import math
import cmath

def printMath():
	print """
	print math.sqrt"""
	print "num 9 with sqrt is" + str(math.sqrt(9))
	print "num 10 with sqrt is " + str(math.sqrt(10))
	print "num 987654321 sqrt is" + str(math.sqrt(987654321))
	
def printCmath():
	print """
	print cmath.sqrt"""
	print "num 9 with sqrt is" + str(cmath.sqrt(9))
	print "num 10 with sqrt is " + str(cmath.sqrt(10))
	print "num 987654321 sqrt is" + str(cmath.sqrt(987654321))
	
if __name__ == "__main__":
	printMath();
	printCmath();