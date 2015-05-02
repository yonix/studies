#!/usr/bin/env python
import json
import urllib
# from urlparse import urlparse
response = urllib.urlopen('https://udacity.com/public-api/v0/courses')
json_response = json.loads(response.read())
for course in json_response['courses']:
    course['homepage'] = course['homepage'][:course['homepage'].find('?')]
    print "[{} | *Udacity*]({}) **Future**".format(course['title'], course['homepage'])
