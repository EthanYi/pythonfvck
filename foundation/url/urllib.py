import urllib

def parseUrl(url_path):
	google = urllib.urlopen("http://www.google.com")
	print "http header:\n", google.info()
	print "http status:", google.getcode()
	print "url:", google.geturl()
	for line in goolge:
		print line,
	google.close()
	
def cbc(a, b, c):
	"""a, 已经下载的数据块
	b,数据块的大小
	c,远程文件的大小"""
	per = 100.0 * a * b / c
	if per > 100:
		per = 100
	print '%.2f%%' % per

def DownLoadUrl(url_path):
	url = "http://www.google.com"
	local = "D:\\"
	urllib.urlretrieve(url, local, cbc)
	
def urlE&Decode():
	data = 'name = ~a+3'
	data1 = urllib.quote(data)
	print data1 # result: name%20%3D%20%7Ea%2B3
	print urllib.unquote(data1) # result: name = ~a+3

	data2 = urllib.quote_plus(data)
	print data2 # result: name+%3D+%7Ea%2B3
	print urllib.unquote_plus(data2)    # result: name = ~a+3

	data3 = urllib.urlencode({ 'name': 'dark-bull', 'age': 200 })
	print data3 # result: age=200&name=dark-bull

	data4 = urllib.pathname2url(r'd:\a\b\c\23.php')
	print data4 # result: ///D|/a/b/c/23.php
	print urllib.url2pathname(data4)    # result: D:\a\b\c\23.php
