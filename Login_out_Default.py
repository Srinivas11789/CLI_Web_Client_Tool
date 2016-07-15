###############################################################################
#
#  Login and Logout with Default Web Pages
#
###############################################################################
###
import urllib2, base64
import time
request1 = urllib2.Request("<url>")
request = urllib2.Request("<url>")
request2 = urllib2.Request("<url>")
basestr = base64.encodestring('%s:%s' % ("admin2", "admin2")).replace('\n',' ')
request.add_header("Authorization", "Basic %s" % basestr)
request1.add_header("Authorization", "Basic %s" % basestr)
request2.add_header("Authorization", "Basic %s" % basestr)
try:
    result1 = urllib2.urlopen(request1)
    result = urllib2.urlopen(request)
    time.sleep(10)
    result2 = urllib2.urlopen(request2)
    print(result1.read())
    print(result.read())
    print(result2.read())
except urllib2.HTTPError, e:
    print e
except urllib2.URLError, e:
    print e.args
