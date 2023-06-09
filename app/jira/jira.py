import requests
from requests.auth import HTTPBasicAuth
import json
from app.secret import testToken, testUrl, email


url = testUrl
email = email
testToken = testToken

auth = HTTPBasicAuth(email, testToken)

headers = {
  "Accept": "application/json"
}
def get_request():
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    return response

print(json.dumps(json.loads(get_request().text), sort_keys=True, indent=4, separators=(",", ": ")))