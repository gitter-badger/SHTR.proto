__author__ = 'tahmid'

import urllib
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

import httplib2
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage


CODE = ''

class customHandler(BaseHTTPRequestHandler):
    #handler for GET requests

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<center><h2>You have successfully logged in<h2><center>")
        s =  urlparse.urlparse(self.requestline).query
        code =  s.split('=', 1)[1].split(' ')[0]
        CODE = code
        return


class Authenticator:
    def __init__(self):
        self.verification_code = CODE
        self.path_to_client_secrect = 'client_secret.json'
        self.client_id = '1015702721813-davr8fgfgji5eih3ab52qnke423n53it.apps.googleusercontent.com'
        self.client_secrect = '1015702721813-davr8fgfgji5eih3ab52qnke423n53it.apps.googleusercontent.com'
        self.token_file_name = 'token.json'
        self.redirect_uri = 'http://localhost:8080'
        self.storage = Storage(self.token_file_name)
        self.auth_scope = 'https://www.googleapis.com/auth/drive.file'
        self.flow = flow_from_clientsecrets(self.path_to_client_secrect, self.auth_scope, self.redirect_uri )
        self.creden = self.storage.get()
        self.port = 7575

    def _isAlreadyLoggedIn(self):
        if(self.creden != None):
            return True
        return False

    def _get_permission_url(self):
        return urllib.unquote(self.flow.step1_get_authorize_url())

    def _get_drive_service(self):
        http = httplib2.Http()
        http = self.creden.authorize(http)
        drive_service = build('drive', 'v2', http = http)

    def collect_code(self):
        self.verification_code =CODE

    def start_auth_server(self):
        server = HTTPServer(("", self.port), customHandler)
        server._handle_request_noblock()
        self.collect_code()

