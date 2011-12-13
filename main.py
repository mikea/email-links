import logging
import os

from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app



class BaseHandler(webapp.RequestHandler):

  def render_template(self, relative_template_path, variables):
    full_path = os.path.join(os.path.dirname(__file__), relative_template_path)
    self.response.out.write(template.render(full_path, variables))


class MainHandler(BaseHandler):
  def get(self):
    self.render_template('t/index.html', {})


class IncomingEmailHandler(webapp.RequestHandler):
  def post(self):
    message = mail.InboundEmailMessage(self.request.body)
    logging.info('Got e-mail: %s', message)


application = webapp.WSGIApplication(
    [('/', MainHandler),
     ('/_ah/mail/.+', IncomingEmailHandler)
     ],
    debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
