import os
import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class BlogHandler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

    def render_str(self,template,**params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))

class Main_Handler(BlogHandler):
    def render_front(self, subject="", content="", error=""):
        posts =db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 5")
        self.render('front.html' , subject= subject , content= content , error= error , posts= posts)

    def get(self):
        self.render_front()

















app = webapp2.WSGIApplication([
    ('/blog', Main_Handler),
    ], debug=True)
