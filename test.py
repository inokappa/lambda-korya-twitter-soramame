# -*- coding: UTF-8 -*-

import base64
import gzip
from StringIO import StringIO
import json
import datetime
# import pytz

event = "H4sIAAAAAAAAAJ2RTY+CMBCG/wrpXgXb0lLgZrJqTPbjoDdjTJWJNlIgpega43/fAbMfpz3sqZN3Ju887/RGLLStPsDq2gDJyfNkNdm+TpfLyXxKRqS+VOBQ5pIxSdM4SShFuawPc1d3DXaKen8CF6Ly0JfegbbYaGunrbYQNqaB0lSw5ZTJkNGQKRxtu127d6bxpq5mpvTgWpKvyYu2u0I/TLb+AuDJZvCdnqHy/ciNmALtY865SngsOE0TJWjMleI8TZhgMhNKZkpKpSjPUFY8EzLFkUT09N5gZq8t4jMhJMNUTCSKj75ugfaLUbD+5k1XNMuFzGMaSUFxY/DEkk2weJu9B2EY5MHR+yYfjxvLZeTROzJVfdJOR/vajk/Xrr1245/00dHbEjngwzu991DMDJQFZruRQnvo8fqT/7m9v2DDcSwfKoZvGPY/cB7g+wqGEhnJ72D/Qb3fN/dPf1Js6SkCAAA="

decoded_data = event.decode("base64")
print gzip.GzipFile(fileobj=StringIO(decoded_data)).read()
#jst = pytz.timezone('Asia/Tokyo')
#print datetime.today(jst)
json_data = json.loads(gzip.GzipFile(fileobj=StringIO(decoded_data)).read())
d = datetime.date.today() - datetime.timedelta(1)
d = u"%s 年 %s 月 %s 日 PM2.5 の状況: " % (d.year, d.month, d.day)
for data in json_data['logEvents']:
	print d + data['extractedFields']['message']
