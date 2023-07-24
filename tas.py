import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://bharat-kumar.atlassian.net/rest/api/3/myself"

auth = HTTPBasicAuth("19311a04m3@sreenidhi.edu.in", "ATATT3xFfGF0S3w3liRfbCduC-YnN1k7HG9vuZ-2JXM8yadDgpZItkIwtAZ7DyLwgpNKEvZvNrCENSSGuJpdLDiXlnnD0mQ-JNFFS46LhY7uDRoAKXciLs8F9UvsL45ARuvden0hO5CKZ4P0JsgjsSnKw4Y5a6UDJbi5GW1mxxCy4Gy6qKJmf-Q=7D8299C6")

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
