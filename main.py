import logging

from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World!')


class IncomingEmailHandler(webapp.RequestHandler):
  def post(self):
    message = mail.InboundEmailMessage(self.request.body)
    logging.info('Got e-mail: %s', message)


application = webapp.WSGIApplication(
    [('/', MainPage),
     ('/_ah/mail/.+', IncomingEmailHandler)
     ],
    debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
