#!/usr/bin/env python

import time
import os

def time_test():
	time.localtime() #time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=14, tm_sec=50, tm_wday=3, tm_yday=125, tm_isdst=0)
	time.localtime(1304575584.1361799) #time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=6, tm_sec=24, tm_wday=3, tm_yday=125, tm_isdst=0)
	time.gmtime() #time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=6, tm_min=19, tm_sec=48, tm_wday=3, tm_yday=125, tm_isdst=0)
	time.time() #1304575584.1361799
	time.sleep(4)
	time.clock()
	time.asctime() #'Thu May 5 14:55:43 2011'
	time.ctime() #'Thu May 5 14:58:09 2011'
	time.strftime()
	time.strptime()