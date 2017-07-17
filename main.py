#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2
import json
import urllib2

from apiclient.discovery import build
from optparse import OptionParser



JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))



MAIN_API = "https://content.googleapis.com/youtube/v3/playlistItems?maxResults=5&part=snippet&playlistId=UUvS6-K6Ydmb4gH-kim3AmjA&key=AIzaSyC5rwPxv0NlkAJLzKFFkZts2Wz3GEMH9-Y"

class JsonHandler(webapp2.RequestHandler):
    def get(self):
    	if self.request.get('fmt') == 'json':
    		url = MAIN_API
    		json_data = {}
    		#url = "http://localhost/ws_cap/web/cliente/json"
    		response = urllib2.urlopen(url)
    		data = response.read()
    		json_data = json.loads(data)
    		self.response.out.headers['Content-Type'] = 'text/json'
    		self.response.out.write(json.dumps(json_data))
    		return
    	
    	title = "JSON"
    	template_vars = {
    		'title':title,
    	}
    	template = JINJA_ENVIRONMENT.get_template('about.html')
    	self.response.out.write(template.render(template_vars))

class VideoHandler(webapp2.RequestHandler):
    def get(self):
    	
		url = MAIN_API
		response = urllib2.urlopen(url)
		data = response.read()
		json_data = json.loads(data)
        
		self.response.out.headers['Content-Type'] = 'text/json'
		self.response.out.write(json.dumps(json_data))
		
    	
    	#title = "JSON"
    	#template_vars = {
    	#	'title':title,
    	#}
    	#template = JINJA_ENVIRONMENT.get_template('about.html')
    	#self.response.out.write(template.render(template_vars))




app = webapp2.WSGIApplication([    
    ('/',VideoHandler),
    ('/json',JsonHandler)

], debug=True)