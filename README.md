GCLOUD_SERVICE_ACCOUNT_KEY_B64
GCP_PROJECT_ID
GCP_ZONE
JENKINS_USERNAME
JENKINS_PASSWORD

Compute Engine API 
Infrastructure Manager API 

roles/config.agent
roles/compute.admin
roles/iam.serviceAccountUser
os config
  
sudo -i
sudo nano /var/lib/jenkins/config.xml
<useSecurity>false</useSecurity>
sudo systemctl restart jenkins
sudo visudo
jenkins ALL=(ALL) NOPASSWD:ALL
sudo -u jenkins sudo ls /root