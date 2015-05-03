#!/usr/bin/env python
import json
import urllib

api_url = "https://api.coursera.org/api/catalog.v1/courses"
base_course_url = "https://www.coursera.org/course/"

response = urllib.urlopen(api_url)
json_response = json.loads(response.read())
for course in json_response['elements']:
    course['homepage'] = base_course_url + course['shortName']
    print "- [{} | *Coursera*]({}) **Future**".format(course['name'].encode('utf-8'), course['homepage'])
