import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

### BASE HANDLER

class _BaseHandler(webapp2.RequestHandler):
	def initialize(self, request, response):
		super(_BaseHandler, self).initialize(request, response)

### STATIC PAGES ###

class HomePage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render())

app = webapp2.WSGIApplication([
		('',HomePage),
		('/',HomePage),],
		debug=True)
