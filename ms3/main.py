import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Microservice3')

app = webapp2.WSGIApplication([
    ('/ms3', MainPage),
], debug=True)