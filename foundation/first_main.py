#!/usr/bin/env python
#coding:utf-8
import sys

if __name__ == "__main__":
	sys.path.append("importModule")
	exec(open(sys.argv[1]).read())