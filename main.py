import json
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests


#path to your service account key file adminsdk
SERVICE_ACCOUNT_FILE = '/content/firebase-adminsdk.json'

# define the required scopes
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

#load the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

#generate access token 
request = google.auth.transport.requests.Request()
credentials.refresh(request)
access_token = credentials.token

#show the firebase access token
print(f'Access Token: {access_token}')