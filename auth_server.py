import cherrypy
from shoot import receive_verification_code

class AuthVerificationServer(object):

    verification_code = ''
    def stop_server(self):
        cherrypy.engine.exit()

    @cherrypy.expose()
    def index(self, code=''):
        verification_code = code
	receive_verification_code(code)
        return "<h1>You have successfully setup Google Drive.</h1>"

