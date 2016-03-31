######################################################################################
#
#                       Command Line Interface Web Client Tool 
#
# Added : Custom Page Simulation - DNS Resolving
######################################################################################
f = open('/proc/self/ns_id', 'w')
f.write('2\n')
f.close()
import urllib2, base64
import urllib, time
import ctypes
libc = ctypes.cdll.LoadLibrary('libc.so.6')
res_init = libc.__res_init
res_init()
request1 = urllib2.Request("http://network-access.com")
request3 = urllib2.Request("http://network-access.com/login")
request = urllib2.Request("http://network-access.com/hello")
request2 = urllib2.Request("http://network-access.com/goodbye")
values = {'extremenetloginuser' : 'admin3',
          'extremenetloginpassword' : 'admin2',
          }

data = urllib.urlencode(values)
#req = urllib2.Request(url, data)
basestr = base64.encodestring('%s:%s' % ("admin2", "admin2")).replace('\n',' ')
#request.add_header("Authorization", "Basic %s" % basestr)
request2.add_header("Authorization", "Basic %s" % basestr)
try:
    print "\nThe Start page is as follows:--------------------\n"
    result1 = urllib2.urlopen(request1)
    print(result1.read())
except urllib2.HTTPError, e:
    print e
except urllib2.URLError, e:
    print e.args
try:
    print "\nThe Login page is as follows:--------------------\n"
    result3 = urllib2.urlopen(request3)
    print(result3.read())
#    urllib2.HTTPRedirectHandler.redirect_request("www.extremenetworks.com")
except urllib2.HTTPError, e:
    print e
except urllib2.URLError, e:
    print e.args
	
try:
    print "\nThe Login Success Page is as follows---------------\n"
    result = urllib2.urlopen(request, data)
    print(result.read())
except urllib2.HTTPError, e:
    print e
except urllib2.URLError, e:
    print e.args

try:
    print "\nThe Logout Success Page is as follows---------------\n"
    time.sleep(10)
    result2 = urllib2.urlopen(request2)
    print(result2.read())
except urllib2.HTTPError, e:
    print e
except urllib2.URLError, e:
    print e.args

