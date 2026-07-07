pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // This tells Jenkins to download your code from GitHub
                checkout scm
                echo 'Code successfully pulled from GitHub!'
            }
        }
        stage('Test Server Tools') {
            steps {
                // This proves Jenkins can use the tools we installed via PuTTY
                sh 'docker --version'
                sh 'terraform --version'
                sh 'aws --version'
            }
        }
    }
}