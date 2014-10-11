#!/usr/bin/python

import httplib2
import pprint
import unicodedata
from PySide.QtCore import QUrl
import webbrowser
import urllib

from apiclient import errors
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

PATH_TO_SECRET = 'client_secrets.json'

def get_permission_url():
    # Copy your credentials from the APIs Console
    CLIENT_ID = '82388069862-7m3uqv8ff4p2hc5korrs66n7lata3dbr.apps.googleusercontent.com'
    CLIENT_SECRET = 'IuZt1FYe69121OpJ4rjQAXPl'

    # Check https://developers.google.com/drive/scopes for all available scopes
    AUTH_SCOPE = 'https://www.googleapis.com/auth/drive.file'

    # Run through the OAuth flow and retrieve credentials
    flow = flow_from_clientsecrets(PATH_TO_SECRET, AUTH_SCOPE, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
    authorize_url = flow.step1_get_authorize_url()
    return urllib.unquote(authorize_url)

def get_drive_service(verification_code):
    """returns a google drive service"""
    credentials = flow.step2_exchange(verification_code)

    #Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    http = credentials.authorize(http)

    drive_service = build('drive', 'v2', http=http)
    return drive_service

def insert_file(service, title, description, parent_id, mime_type, filename):
    """Insert new file.

    Args:
      service: Drive API service instance.
      title: Title of the file to insert, including the extension.
      description: Description of the file to insert.
      parent_id: Parent folder's ID.
      mime_type: MIME type of the file to insert.
      filename: Filename of the file to insert.
    Returns:
      Inserted file metadata if successful, None otherwise.
    """
    media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
    body = {
        'title': title,
        'description': description,
        'mimeType': mime_type
    }
    # Set the parent folder.
    if parent_id:
        body['parents'] = [{'id': parent_id}]

    try:
        file = service.files().insert(
            body=body,
            media_body=media_body).execute()

        # Uncomment the following line to print the File ID
        # print 'File ID: %s' % file['id']

        return file
    except errors.HttpError, error:
        print 'An error occured: %s' % error
        return None


if __name__ == '__main__':
    svc = build_service()
    f = insert_file(svc, "Garbage", "Just a throwaway file", None, "text/plain", "gbg.gbg" )
    print "File uploaded"
