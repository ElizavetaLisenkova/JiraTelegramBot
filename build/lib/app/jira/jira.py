import requests
from requests.auth import HTTPBasicAuth
import json

testUrl = "https://arstar.atlassian.net/rest/api/3/serverInfo"
email = "lisenkovaelizavetas@gmail.com"
telegram_token = '6133746261:AAHpNiQ6uFQZlDJlWNsHmVKkL_US8tMYsfY'
testToken = "ATATT3xFfGF0fEy1NhafG98zA1D4PN_H_zoKznQOTIYQ1JmjneY6pdYm28IRAX4Ucb44HKx5PaKQCqahObX7j4zpmUJQ_MwydJ9ulZhxnhi9XYu1_Sdtx0mnbbq1neJx20iCjxi3q47b-wHOowXYlzYNeMJWXsd7tjg9HHPX5xsRhsnWB-drMzg=0CCD7757"




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