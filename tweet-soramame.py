# -*- coding: utf-8 -*-

import sys, json
import datetime
import ConfigParser
import twitter
import base64
import gzip
from StringIO import StringIO

def extract_url(record):
    # cw_log_json= json.loads(event)
    # record = cw_log_json['awslogs']['data']
    decoded_data = record.decode("base64")
    json_data = json.loads(gzip.GzipFile(fileobj=StringIO(decoded_data)).read())
    for data in json_data['logEvents']:
    	return data['extractedFields']['message']

def lambda_handler(event, context): 
    # print event['awslogs']['data']
    # config.ini から Twitter API の Credential 情報を取得
    c = ConfigParser.SafeConfigParser()
    c.read("./config.ini")
    # Twitter API を初期化
    api = twitter.Api(
        consumer_key        = c.get('tw','consumer_key'),
        consumer_secret     = c.get('tw','consumer_secret'),
        access_token_key    = c.get('tw','access_token_key'),
        access_token_secret = c.get('tw','access_token_secret'),
        )
    url = extract_url(event['awslogs']['data'])
    d = datetime.date.today() - datetime.timedelta(1)
    # d = u"%s 年 %s 月 %s 日 PM2.5 の状況(九州地方のみ): " % (d.year, d.month, d.day)
    d = u"昨日の PM2.5 状況(九州地方のみ): " % (d.year, d.month, d.day)
    print d + url
    print api.PostUpdate(d + url)

#event = "H4sIAAAAAAAAAJ2RTY+CMBCG/wrpXgXb0lLgZrJqTPbjoDdjTJWJNlIgpega43/fAbMfpz3sqZN3Ju887/RGLLStPsDq2gDJyfNkNdm+TpfLyXxKRqS+VOBQ5pIxSdM4SShFuawPc1d3DXaKen8CF6Ly0JfegbbYaGunrbYQNqaB0lSw5ZTJkNGQKRxtu127d6bxpq5mpvTgWpKvyYu2u0I/TLb+AuDJZvCdnqHy/ciNmALtY865SngsOE0TJWjMleI8TZhgMhNKZkpKpSjPUFY8EzLFkUT09N5gZq8t4jMhJMNUTCSKj75ugfaLUbD+5k1XNMuFzGMaSUFxY/DEkk2weJu9B2EY5MHR+yYfjxvLZeTROzJVfdJOR/vajk/Xrr1245/00dHbEjngwzu991DMDJQFZruRQnvo8fqT/7m9v2DDcSwfKoZvGPY/cB7g+wqGEhnJ72D/Qb3fN/dPf1Js6SkCAAA="

#lambda_handler(event)
