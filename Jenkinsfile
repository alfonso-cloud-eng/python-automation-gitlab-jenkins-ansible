pipeline {
    agent any
    environment {
        SLACK_WEBHOOK_URL = ${env.SLACK_WEBHOOK_URL}    }
    stages {
        stage('Prepare Directory') {
            steps {
                sh '''
                    mkdir -p ~/myapp
                    chmod 777 ~/myapp
                '''
            }
        }
        stage('Download Application') {
            steps {
                sh '''
                    cd ~/myapp
                    rm -f stocks-slack.py
                    wget https://raw.githubusercontent.com/alfonso-cloud-eng/python-automation-gitlab-jenkins-ansible/main/stocks-slack.py -O stocks-slack.py
                    chmod +x stocks-slack.py
                '''
            }
        }
        stage('Install Python & Dependencies') {
            steps {
                sh '''
                    sudo apt update && sudo apt install -y python3 python3-pip
                    pip3 install yfinance slack_sdk apscheduler
                '''
            }
        }
        stage('Run stocks-slack.py') {
            steps {
                // Run the Python script. If it’s long-running, consider running it in the background.
                sh 'python3 -u ~/myapp/stocks-slack.py'
            }
        }
    }
}
