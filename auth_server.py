import cherrypy
from pydispatch import dispatcher

class AuthVerification(object):

    verification_code = ''



    @cherrypy.expose()
    def index(self, code=''):
        verification_code = code
        dispatcher.send(sender=code)
        return "<h1>You have successfully setup Google Drive.</h1>"

