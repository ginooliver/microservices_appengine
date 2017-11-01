import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Microservice1')

app = webapp2.WSGIApplication([
    ('/ms1', MainPage),
], debug=True)