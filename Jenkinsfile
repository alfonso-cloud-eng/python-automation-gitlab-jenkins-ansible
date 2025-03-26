pipeline {
    agent any
    stages {
        stage('Set Slack Webhook') {
            steps {
                sh '''
                  export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/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"
                  echo $SLACK_WEBHOOK_URL
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                  # Si no está instalado python3-pip, ya fue instalado por Ansible.
                  # De todas formas, revisamos que tengamos pip3
                  pip3 install --upgrade pip
                  pip3 install yfinance slack_sdk apscheduler
                '''
            }
        }
        stage('Run main.py') {
            steps {
                sh '''
                  cd /home/tu_usuario_linux/myapp
                  python3 main.py
                '''
            }
        }
    }
}
