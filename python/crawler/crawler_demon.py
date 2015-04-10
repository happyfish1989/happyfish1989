import sys;
import os;
import re;
import urllib2;


def downURL( url, filename):
	try:
		fp = urllib2.urlopen(url);
	except Exception, e:
		print 'download exception';
		return 0;
	pass

	op = open(filename,'rb');
	while 1:
		s = fp.read();
		if not s:
			break;
			pass
		op.write(s);
		pass
	fp.close();
	op.close();
	return 1;

def getURL(url):
	try:
		fp = urllib2.urlopen(url)
	except:
		print 'get url exception'
		return []
	pass

	pattern = re.compile("http://sports.sina.com.cn/[^\>]+.shtml")
	while 1:
		s = fp.read();
		if not s:
			break;
			pass
		urls = pattern.findall(s);
		pass
	fp.close();
	return urls;

def spider(startURL, times):
	urls = []
	urls.append(startURL);
	i = 0;
	while 1:
		if i > times:
			break;
			pass
		if len(urls) > 0:
			url = urls.pop(0);
			print url, len(urls);
			downURL(url, str(i)+".htm");
			i = i+1;
			if len(urls) < times:
				urllist = getURL(url)
				for url in urllist:
					if urls.count(url)==0:
						urls.append(url);
						pass
				 	pass 
				pass
			pass
		else:
			break;
			pass;
		pass
	pass
	return 1;


def main():
	print 'hello, crawler world!'
	pass

if __name__ == '__main__':
	main()