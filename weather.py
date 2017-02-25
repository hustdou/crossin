# coding: utf-8
import urllib2
import json
from StringIO import StringIO
import gzip
city = raw_input('你想查哪个城市的天气？\n')
url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s'% city
request = urllib2.Request(url)
response = urllib2.urlopen(request)
if response.info().get('Content-Encoding') == 'gzip':
    print 'gzip enabled'
    buf = StringIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
else:
    data = response.read()
dic = json.loads(data)
print 'city: %s' %city
print '温度: %s' %str(dic['data']['wendu'])
print dic['data']['forecast'][0]['high']
print dic['data']['forecast'][0]['low']
