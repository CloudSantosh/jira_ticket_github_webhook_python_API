from flask import Flask, request, jsonify
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os
import requests
import hmac
import hashlib

app = Flask(__name__)

# Load environment variables
load_dotenv()

# GitHub secret for webhook validation
# github_secret = os.environ.get('GITHUB_WEBHOOK_SECRET')

# Jira credentials
jira_email = os.environ.get("JIRA_EMAIL")
jira_api_token = os.environ.get("JIRA_API_TOKEN")
jira_base_url = "https://santoshtechguyjira.atlassian.net"

# Jira project key
jira_project_key = "TP"

# Jira issue type
jira_issue_type = "10006"


@app.route("/github_webhook", methods=["POST"])
def github_webhook():
    # Validate GitHub webhook signature
    # if not validate_github_signature(request):
    # return jsonify({'message': 'Invalid GitHub signature'}), 403

    # Parse the incoming JSON payload
    payload = request.json

    # Check if the payload is an issue comment event
    if "issue" in payload and "comment" in payload:
        issue_comment = payload["comment"]["body"]

        # Specify the keywords to trigger Jira creation
        jira_keywords = ["/jira", "/Jira", "/JIRA"]

        # Check if any of the keywords is present in the issue comment
        if any(keyword in issue_comment for keyword in jira_keywords):
            create_jira_issue(payload)

    return jsonify({"message": "Webhook received successfully"}), 200


# def validate_github_signature(request):
#    if github_secret is None:
#       return False

#    signature_header = request.headers.get('X-Hub-Signature')
#    if signature_header is None:
#        return False

#    payload = request.data
#    expected_signature = 'sha1=' + hmac.new(github_secret.encode(), payload, hashlib.sha1).hexdigest()

#    return hmac.compare_digest(expected_signature, signature_header)


def create_jira_issue(payload):
    url = f"{jira_base_url}/rest/api/3/issue"

    # Jira API token authentication
    auth = HTTPBasicAuth(jira_email, jira_api_token)

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    # Extract relevant information from GitHub payload
    issue_title = payload["issue"]["title"]
    issue_body = payload["comment"]["body"]

    # Create payload for Jira issue creation
    jira_payload = {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [{"type": "text", "text": issue_body}],
                        "type": "paragraph",
                    }
                ],
                "type": "doc",
                "version": 1,
            },
            "issuetype": {"id": jira_issue_type},
            "project": {"key": jira_project_key},
            "summary": issue_title,
        },
        "update": {},
    }

    # Make a POST request to create the Jira issue
    response = requests.request(
        "POST", url, json=jira_payload, headers=headers, auth=auth
    )

    return jsonify(json.loads(response.text)), 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
