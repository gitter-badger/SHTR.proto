__author__ = 'tahmid'

import httplib2
import urllib
from googleapiclient import errors
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

class Authenticator:
    def __init__(self):
        self.path_to_client_secrect = 'client_secret.json'
        self.client_id = '1015702721813-davr8fgfgji5eih3ab52qnke423n53it.apps.googleusercontent.com'
        self.client_secrect = '1015702721813-davr8fgfgji5eih3ab52qnke423n53it.apps.googleusercontent.com'
        self.token_file_name = 'token.json'
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.storage = Storage(self.token_file_name)
        self.auth_scope = 'https://www.googleapis.com/auth/drive.file'
        self.flow = flow_from_clientsecrets(self.path_to_client_secrect, self.auth_scope, self.redirect_uri )
        self.creden = self.storage.get()

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