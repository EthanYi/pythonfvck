#!/usr/bin/env python
import os
import stat
import fnmatch
import re

def DirTraversal(path):
	for fileName in os.listdir(path):
		subFilePath = path.join(fileName)
		print subFilePath
		if os.path.isdir(subFilePath):
			DirTraversal(subFilePath)
		
		
def Dirmake(path):
	os.makedirs(path)

def DirDel(path):
	os.removesdirs(path)
	
def fnmatch(path):
	for fileName in os.listdir(path):
		if fnmatch.fnmath(fileName,"*.txt"):
			print open(fileName).read()
		elif fnmatch.fnmath(fileName,"*.exe"):
			print fileName
	
def Transfnmatch(path):
	filePattern = fnmatch.translate("*.txt")
	for fileName in os.listdir(path)
		if re.match(filePattern, fileName):
			print "text file"
