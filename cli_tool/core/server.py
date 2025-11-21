from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request
import requests
import urllib.parse
import os
from dotenv import load_dotenv, set_key

app = Flask(__name__)
app.secret_key = 'abc123'

load_dotenv()

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = "http://127.0.0.1:5000/callback"   # Need to change this eventually


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

@app.route('/')
def index():
    
    return "Welcome to my Spotify App <a href='/login'>Login with Spotify</a>"

@app.route('/login')
def login():

    print(f'Calling login with client_id = {client_id}')
    
    params = {
        'client_id':client_id,
        'response_type':'code',
        'redirect_uri':REDIRECT_URI,
        'show_dialog':True,
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})

    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': client_id,
            'client_secret': client_secret,
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        access_token = token_info['access_token']
        refresh_token = token_info['refresh_token']
        expires_in = token_info['expires_in']

        # url = "https://api.spotify.com/v1/me/player/pause"
        # header = {
        #     'Authorization': f"Bearer {access_token}",
        # }

        # pause_resp = requests.put(url, headers=header)

        # Set environment variable to access_token

        # IMPORTANT. This line did not work as expected. Created new .env
        # file in core layer. Bad
        
        #set_key(".env", "ACCESS_TOKEN", access_token)
        
        
        return access_token
    
@app.route('/success')
def success():
    return "Logged in"

if __name__ == '__main__':

    # Set up flask server to get access token
    app.run(host='0.0.0.0', debug=True)


# Current code creates a new .env file in the /core layer, and then writes to it.
# Need to instead write to the global .env layer