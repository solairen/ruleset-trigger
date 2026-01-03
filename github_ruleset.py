import os

import requests

github_token = os.environ.get("INPUT_TOKEN")
repository = os.environ.get("INPUT_REPOSITORY") or os.environ.get("GITHUB_REPOSITORY")
ruleset_id = os.environ.get("INPUT_RULESET_ID")
enforcement = os.environ.get("INPUT_ENFORCEMENT") or "active"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28",
    "Content-Type": "application/json",
}

data = {"enforcement": enforcement}

url = f"https://api.github.com/repos/{repository}/rulesets/{ruleset_id}"

response = requests.put(url, headers=headers, json=data)

if response.status_code == 200:
    print(f"Successfully updated ruleset {ruleset_id} in {repository}")
    print(f"Enforcement set to: {enforcement}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)
