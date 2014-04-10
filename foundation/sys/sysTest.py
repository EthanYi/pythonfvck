#!/usr/bin/env python
#coding:UTF-8

import sys

def SysGetArgv():
	print """
	test sys.argv"""
	print sys.argv[0]
	print sys.argv[1]
	
def SysGetPlatForm():
	print """
	test sys.platform"""
	print sys.platform
	
def SysGetPath():
	print """
	test sys.path"""
	print sys.path
	
def SysExit():
	print """
	test sys.exit"""
	print sys.exit(0)
	
def SysVersion():
	print """
	test sys.version"""
	print sys.version

def SysGetWindowsVersion():
	print """
	test sys.getwindowsversion"""
	print sys.getwindowsversion()
	
	
if __name__ == "__main__":
	SysGetArgv()
	SysVersion()
	SysGetWindowsVersion()
	SysGetPlatForm()
	SysGetPath()
	raw_input("press any key to continue")
	SysExit()
	
	