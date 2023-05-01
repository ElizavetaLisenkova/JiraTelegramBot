import requests
from requests.auth import HTTPBasicAuth
import json
import secret

url = secret.testUrl
email = secret.email
testToken = secret.testToken

auth = HTTPBasicAuth(email, testToken)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))