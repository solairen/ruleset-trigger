import os
import requests

github_token = os.environ.get("INPUT_TOKEN")
repository = (
  os.environ.get("INPUT_REPOSITORY")
  or os.environ.get("GITHUB_REPOSITORY")
)
ruleset_id = os.environ.get("INPUT_RULESET_ID")
enforcement = (
  os.environ.get("INPUT_ENFORCEMENT")
  or "active"
)

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

data = {
    "enforcement": enforcement
}

url = f"https://api.github.com/repos/{repository}/rulesets/{ruleset_id}"

response = requests.patch(url, headers=headers, json=data)

if response.status_code == 200:
  print(f"Status code: {response.status_code}")
else:
  print(f"Error: {response.status_code}")
  print(response.text)
  exit(1)
