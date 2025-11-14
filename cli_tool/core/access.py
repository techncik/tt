import base64
from dotenv import load_dotenv
import os
import json
import requests
import urllib.parse
from flask import jsonify, redirect, request

# Set up quick Flask server
from flask import Flask
app = Flask(__name__)
app.secret_key = 'abc123'

load_dotenv()

AUTH_URL = "https://accounts.spotify.com/authorize?"
TOKEN_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = "http://127.0.0.1:5000/callback"   # Need to change this eventually
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_auth(
        access_token
):

    # Definitely want to add Scope and State to this eventually. This will do
    # for dev though. 
    # https://developer.spotify.com/documentation/web-api/tutorials/code-flow  
    
    # Some issue with this not returning the correct code.
    # Possibly an issue with not actually running a server??

    auth_header = base64.urlsafe_b64encode((client_id + ':' + client_secret).encode())
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % auth_header.decode(),
    }

    payload = {
        'code': access_token,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }

    # Make a request to the /token endpoint to get an access token
    access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)

    # convert the response to JSON
    access_token_response_data = access_token_request.json()

    print("GOT AUTH")

    print(access_token_response_data)

    # save the access token
    # access_token = access_token_response_data['access_token']

    # print(access_token)

    
    return 0