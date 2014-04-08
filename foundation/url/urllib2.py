#!/usr/bin/env python

import urllib2

def ParseUrl(url_path):
	req = urllib2.Request("http://www.qiushibaike.com")
	response = urllib2.urlopen(req)
	the_page = response.read()
	
def Proxy(url_path):
	enable_proxy = True
	proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
	null_proxy_handler = urllib2.ProxyHandler({})
	 
	if enable_proxy:
		opener = urllib2.build_opener(proxy_handler)
	else:
		opener = urllib2.build_opener(null_proxy_handler)
 #urllib2.install_opener(opener)
 
#for qiushibaike
#httpHandler = urllib2.HTTPHandler(debuglevel=1)
#httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#proxy_handler = urllib2.ProxyHandler({"http" : '127.0.0.1:8089'})
#opener = urllib2.build_opener(httpHandler, httpsHandler)
#urllib2.install_opener(opener)
header ={'User-Agent':'mozilla/5.0 (windows; U; windows NT 5.1; zh-cn)'}
qiushi = urllib2.Request("http://www.qiushibaike.com/week",None,header)
response = urllib2.urlopen(qiushi)
#the_page = response.read().decode("utf-8")
#for line in the_page:
#    print line,

soup = BeautifulSoup.BeautifulSoup(''.join(response))
buycount = soup.findAll(attrs={'class':'content'})
for item in buycount:
    print item
	
import urllib
import urllib2
import re
import BeautifulSoup
import time

header ={'User-Agent':'mozilla/5.0 (windows; U; windows NT 5.1; zh-cn)'}

for i in range(4, 30):
    url = "http://www.qiushibaike.com/week/page/%d?s=4652172" % i
    qiushi = urllib2.Request(url,None,header)
    response = urllib2.urlopen(qiushi)

    soup = BeautifulSoup.BeautifulSoup(''.join(response))
    buycount = soup.findAll(attrs={'class':'content'})
    for item in buycount:
        print item
        print "press enter to continue"
        inName = raw_input();

