Create slack webhook
In the form:
https://hooks.slack.com/services/xxxxxxxxxxxx/xxxxxxxxxxxxx/xxxxxxxxxx

Create service account with
Cloud OS Config Service Agent
Compute Admin
Compute OS Admin Login
Service Account User
Service Usage Admin

Encode key
echo -n "your-string" | base64

GCLOUD_SERVICE_ACCOUNT_KEY_B64
GCP_PROJECT_ID
GCP_ZONE

View output logs, access the link, enter admin and password

Admin jenkins left menu
Plugins
Available plugins
Install "pipeline" plugin
Wait
Go to home
create job
select pipeline
paste jenkinsfile in script
substitute webhook in the file (with "")
Save
Build now in the left
Give it a couple of minutes.
