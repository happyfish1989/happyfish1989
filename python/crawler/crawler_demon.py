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