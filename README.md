Compute Engine API 
Infrastructure Manager API 

roles/config.agent
roles/compute.admin
roles/iam.serviceAccountUser
  
  sudo -i
  sudo nano /var/lib/jenkins/config.xml
  <useSecurity>false</useSecurity>
sudo systemctl restart jenkins
sudo visudo
jenkins ALL=(ALL) NOPASSWD:ALL
sudo -u jenkins sudo ls /root