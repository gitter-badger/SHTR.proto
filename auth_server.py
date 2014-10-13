import cherrypy
from pydispatch import dispatcher

class AuthVerificationServer(object):

    verification_code = ''
    def stop_server(self):
        cherrypy.engine.exit()

    @cherrypy.expose()
    def index(self, code=''):
        verification_code = code
        dispatcher.send(sender=code)
        return "<h1>You have successfully setup Google Drive.</h1>"

