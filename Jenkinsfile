pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
                echo 'Code successfully pulled from GitHub!'
            }
        }
        stage('Build Frontend Image') {
            steps {
                // We must tell Jenkins to go into the app-source folder where the Dockerfile lives
                dir('app-source') {
                    // This command builds the container and tags it with the name 'multishop-frontend'
                    sh 'docker build -t multishop-frontend:latest .'
                }
            }
        }
    }
}