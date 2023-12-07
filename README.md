## GitHub Jira Integration using Python Flask (DevOps Project) 👋

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/project_concept.png" >

The project involves building and deploying Jira ticket application using python flask via webhook. Here are components involved:

### 💬 Developers:

When developers comment on the issue using keyword /jira in the text box.

### 💬 Github:

Github send complete information as payload to the Python API hosted on EC2 instance via webhook.

### 💬 EC2 instance hosting API python Application:

EC2 instances using flask to run the python script as an application.

### 💬 Jira:

Jira is a software application developed by the Australian software company Atlassian that allows teams to track issues, manage projects, and automate workflows. Jira is based on four key concepts: issue, project, board and workflow.

- Issue 👩‍💻

An issue is a single work item you track from creation to completion. An issue could be a bug, a user story, an epic, a to-do item for an HR team, or an artifact that your documentation team needs to create.

- Projects 👩‍💻

A project is a way to group your issues along with the common information and context that tie those issues together. You can configure issues associated with a project in a variety of ways, including visibility restrictions and applicable workflows.

- Boards 👩‍💻

A board in Jira is a visual representation of your team’s workflow within a project. You can use multiple boards for flexible ways to view, manage, and report on work in progress on the same project. If you use an agile approach, you may find it helpful to use a Kanban Board view to track backlog items as they refine and a Sprint Board to show the Sprint Backlog for your current sprint.

- Workflows 👩‍💻

A workflow represents the path that issues take as they progress through your project from creation to completion. Each label in a workflow, such as To Do, In Progress, and Done, represent a status that an issue can take. You can configure workflows to govern the transitions an issue can take between different statuses and trigger actions that occur when an issue moves into a status.

In this project we use issue tracking where python flask application makes API call to Jira to create Jira ticket on the board based on comments made by developers on github issues.

# 🚀 Part 1

## Developers Comment on Issue on Github

Here developers make comment on the issue with the keyword /Jira with detail information about the issue.

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/issue_comment.png" >

<br/>

# 🚀 PART-2

## Github Payload Send to Python Application Hosted in AWS EC2 Instance

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook_payload_request.png" >

- Payload with keyword /Jira

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/payload_Jira.png">

- Payload with keyword /abc

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/payload_abc.png">

## Github receives as Response from Flask Python Application

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook_response.png" >

## Github Webhook Configuration

    ⚡️ Click at repository

    ⚡️ Click at settings

    ⚡️ Click at Webhooks

    ⚡️ Click at "Add Webhook"

    ⚡️ Click Public IP address with 5000 ports as defined in Payload URL

    ⚡️ Choose Issue Comments

    ⚡️ Press Add Webhook

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook.png" >

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook_issue_comments.png" >

# 🚀 PART-3

This Python script is a Flask web application that serves as a GitHub webhook receiver. When a GitHub webhook event is received, specifically an issue comment event, the application checks for certain keywords in the comment. If any of the specified keywords ("/jira", "/Jira", or "/JIRA") are found, it triggers the creation of a corresponding issue in Jira.

Let's break down the code step by step:

1. **Importing Libraries:**

   ```python
   from flask import Flask, request, jsonify
   from requests.auth import HTTPBasicAuth
   import json
   from dotenv import load_dotenv
   import os
   import requests
   ```

   The script imports the necessary libraries: Flask for creating a web application, request for handling HTTP requests, jsonify for creating JSON responses, HTTPBasicAuth for HTTP basic authentication, json for working with JSON data, dotenv for loading environment variables, os for interacting with the operating system, and requests for making HTTP requests.

2. **Create Flask App:**

   ```python
   app = Flask(__name__)
   ```

   The Flask application is created with the name `app`.

3. **Load Environment Variables:**

   ```python
   load_dotenv()
   ```

   The `load_dotenv()` function is used to load environment variables from a file named `.env`.

4. **Set Jira Credentials:**

   ```python
   jira_email = os.environ.get('JIRA_EMAIL')
   jira_api_token = os.environ.get('JIRA_API_TOKEN')
   jira_base_url = "https://santoshtechguyjira.atlassian.net"
   ```

   The Jira credentials (email and API token) and base URL are loaded from environment variables.

5. **Set Jira Project and Issue Type:**

   ```python
   jira_project_key = "TP"
   jira_issue_type = "10006"
   ```

   The Jira project key and issue type are specified. Project_key is the First letter of each words. Issue type: Bug(10008), Epic(10009), Story(10006), Task(10007) and subtask(10010)

6. **Define a Route for GitHub Webhook:**

   ```python
   @app.route("/github_webhook", methods=['POST'])
   ```

   This line defines a route for the "/github_webhook" endpoint, and it specifies that the route should only respond to HTTP POST requests.

7. **GitHub Webhook Handling Function:**

   ```python
   def github_webhook():
   ```

   This function is executed when a POST request is made to the "/github_webhook" endpoint.

8. **Parse GitHub Webhook Payload:**

   ```python
   payload = request.json
   ```

   The incoming JSON payload from the GitHub webhook is parsed.

9. **Check for Issue Comment:**

   ```python
   if 'issue' in payload and 'comment' in payload:
   ```

   It checks if the payload contains information about an issue and a comment.

10. **Check for Jira Keywords in Comment:**

    ```python
    if any(keyword in issue_comment for keyword in jira_keywords):
    ```

    It checks if any of the specified keywords ("/jira", "/Jira", "/JIRA") are present in the issue comment.

11. **Call Function to Create Jira Issue:**

    ```python
    create_jira_issue(payload)
    ```

12. **Return Webhook Response:**

    ```python
    return jsonify({'message': 'Webhook received successfully'}), 200
    ```

    A JSON response is returned indicating that the webhook was received successfully.

13. **Function to Create Jira Issue:**

    ```python
    def create_jira_issue(payload):
    ```

    This function is responsible for creating a new issue in Jira.

14. **Jira API URL and Authentication:**

    ```python
    url = f"{jira_base_url}/rest/api/3/issue"
    auth = HTTPBasicAuth(jira_email, jira_api_token)
    ```

    The Jira API URL and authentication details are set up.

15. **Headers and Payload for Jira Issue:**

    ```python
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    jira_payload = {
        # ... (JSON data for creating a new Jira issue)
    }
    ```

16. **Make a POST Request to Jira API:**

    ```python
    response = requests.request(
        "POST",
        url,
        json=jira_payload,
        headers=headers,
        auth=auth
    )
    ```

    A POST request is made to the Jira API using the `requests` library, with the specified URL, payload, headers, and authentication.

17. **Return JSON Response:**

    ```python
    return jsonify(json.loads(response.text)), 200
    ```

    The JSON response from the Jira API is returned.

18. **Run the Flask App:**
    ```python
    if __name__ == "__main__":
        app.run('0.0.0.0', port=5000)
    ```
    The script checks whether it is being run directly (`__name__ == '__main__'`) and, if so, starts the Flask web application on the specified host and port (0.0.0.0:5000). This makes the web service accessible externally.

In summary, this script creates a Flask web service that acts as a GitHub webhook receiver. When it receives a webhook event related to an issue comment and detects specific keywords, it triggers the creation of a corresponding issue in Jira.

#### Configuration of Flask Application

    ⚡️ Updating the system
    	- sudo apt update

    ⚡️ pip installation to interacts with PyPI(Python Package Index)
    	- sudo apt install python3-pip

    ⚡️ Installing flask
    	- sudo apt install python3-flask

    ⚡️ Installation of dotenv to a Python library that helps with loading environment variables
    	- sudo pip3 install python-dotenv

#### Running of Application on EC2 AWS Instances

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/python_application.png" >

# 🚀 PART-4

Login Jenkins > New Item > project-1 > Pipeline > OK

    	               Pipeline:
    	                    Definition: Pipeline script from SCM

    	               SCM: Git

    	                 Repositories:
    	                      Repository URL: https://github.com/CloudSantosh/jenkins-automate-pipeline-project2-application.git

    	                 Script Path: Jenkinsfile

```

<br/>

### Jenkins integration with Sonarqube server.

<br/>

### Login Sonarqube server

```

Sonarqube > My Account > Security > Generate Tokens
Name : porject-1
Type : Global Analysis Token
Expires : 30 Days
Generate

After that copy token & save it.

```

### Go to Jenkins and create credential for Sonar token

```

Dashboard > Manage Jenkins > Credentials > System Global credentials (unrestricted) > Add credentials >
kind: Secret text
Scope: Global
Secret: **\*\***
ID: SONAR_TOKEN
Des: SONAR_TOKEN
Create

```

<br/>

### Configure inventry file & Password less authentication with Kubernetes server.

```

+++++++++++++++ KUBERNETES SERVER ++++++++++++++++++++++
(Allowing password authentication)
$ passwd root
$ cp -r /etc/ssh/sshd_config /etc/ssh/sshd_config_orig
$ sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin yes/g" /etc/ssh/sshd_config
$ sed -i "s/PasswordAuthentication no/PasswordAuthentication yes/g" /etc/ssh/sshd_config
$ systemctl restart sshd.service

+++++++++++++++ ANSIBLE SERVER ++++++++++++++++++++++

$ cat /etc/ansible/hosts
s
$ > /etc/ansible/hosts

$ cat /etc/ansible/hosts

$ vim /etc/ansible/hosts

    [kubernetes] //Here name of the host should only include alphanumeric, hyphens or underscore.
    <kubernetes_ip>

$ cat /etc/ansible/hosts

$ su - jenkins // switching to jenkins user as pipeline is executed as jenkins user

$ ansible -m ping kubernetes -u root

$ ssh root@<kubernetes_ip>

$ ssh-keygen //create ssh keypair for jenkins user

$ ssh-copy-id root@<kubernetes_ip> // Copying public keypair to the kubnernets server

$ ssh root@<kubernetes_ip> //Allow ssh login

$ ansible -m ping kubernetes -u root

```

<br/>

### Create credential for Dockerhub server login.

```

Dashboard > Manage Jenkins > Credentials > System Global credentials (unrestricted) > Add credentials >
kind: Secret text
Scope: Global
Secret: **\*\***
ID: DOCKERHUB_USER
Des: DOCKERHUB_USER
Create

##################################

Dashboard > Manage Jenkins > Credentials > System Global credentials (unrestricted) > Add credentials >
kind: Secret text
Scope: Global
Secret: **\*\***
ID: DOCKERHUB_PASS
Des: DOCKERHUB_PASS
Create

```

<br/>

### Github integrate with Jenkins.

```

+++++++++++++++ GITHUB ACCOUNT ++++++++++++++++++++++
Github > Repository > Settings > Webhooks > Add Webhooks >
Payload UR : http://<jenkins_ip>:8080/github-webhook/
Content type : application/json

Just the push event.

+++++++++++++++ JENKINS SERVER ++++++++++++++++++++++

Jenkins > project-1 > Configure > Build Triggers >
GitHub hook trigger for GITScm polling

```

<br/>

# Part-3

The result of the project looks likes below
<img src="https://github.com/CloudSantosh/jenkins-automate-pipeline-project2-application/blob/main/images/pipeline.png" width="700" height="400">

<img src="https://github.com/CloudSantosh/jenkins-automate-pipeline-project2-application/blob/main/images/console.png" width="700" height="400">

# Accessing application

http://dockerserver_ip_address:30000/application_name

[def]: ttps://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/project_concept.pn
```
