import jinja2
import os
import webapp2

import socket
import sys

jinja_environment = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

### STATIC PAGES ###

class HomePage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render())

app = webapp2.WSGIApplication([
		('/',HomePage),],
		debug=True)
