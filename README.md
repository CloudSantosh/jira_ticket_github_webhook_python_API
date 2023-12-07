# GitHub Jira Integration using Python Flask (DevOps Project)

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/project_concept.png" >

The project involves building and deploying Jira ticket application using python flask via webhook. Here are components involved:

### Developers:

When developers comment on the issue using keyword /jira in the text box.

### Github:

Github send complete information as payload to the Python API hosted on EC2 instance via webhook.

### EC2 instance hosting API python Application:

EC2 instances using flask to run the python script as an application.

### Jira:

Jira is a software application developed by the Australian software company Atlassian that allows teams to track issues, manage projects, and automate workflows. Jira is based on four key concepts: issue, project, board and workflow.

- Issue

An issue is a single work item you track from creation to completion. An issue could be a bug, a user story, an epic, a to-do item for an HR team, or an artifact that your documentation team needs to create.

- Projects

A project is a way to group your issues along with the common information and context that tie those issues together. You can configure issues associated with a project in a variety of ways, including visibility restrictions and applicable workflows.

- Boards

A board in Jira is a visual representation of your team’s workflow within a project. You can use multiple boards for flexible ways to view, manage, and report on work in progress on the same project. If you use an agile approach, you may find it helpful to use a Kanban Board view to track backlog items as they refine and a Sprint Board to show the Sprint Backlog for your current sprint.

- Workflows

A workflow represents the path that issues take as they progress through your project from creation to completion. Each label in a workflow, such as To Do, In Progress, and Done, represent a status that an issue can take. You can configure workflows to govern the transitions an issue can take between different statuses and trigger actions that occur when an issue moves into a status.

In this project we use issue tracking where python flask application makes API call to Jira to create Jira ticket on the board based on comments made by developers on github issues.

# 🚀 Part 1

## Developers Comment

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/issue_comment.png" >

<br/>
<br/>

# 🚀 PART-2

## Github Payload

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook_payload_request.png" >

## Github Response

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook_response.png" >

## Github Webhook Configure

- Click at repository
- Click at settings
- Click at Webhooks
- Click at "Add Webhook"
- Click Public IP address with 5000 ports as defined in Payload URL
- Choose Issue Comments
- Press Add Webhook

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook.png" >

<img src="https://github.com/CloudSantosh/jira_ticket_github_webhook_python_API/blob/main/image/webhook_issue_comments.png" >

# 🚀 PART-3

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
