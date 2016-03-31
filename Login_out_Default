###############################################################################
#
#  Login and Logout with Default Web Pages
#
###############################################################################
f = open('/proc/self/ns_id', 'w')
f.write('2\n')
f.close()
import urllib2, base64
import time
request1 = urllib2.Request("http://10.1.1.1/login")
request = urllib2.Request("http://10.1.1.1/hello")
request2 = urllib2.Request("http://20.1.1.1/goodbye")
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
