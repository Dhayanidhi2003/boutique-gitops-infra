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
                dir('app-source') {
                    // We tag the image with YOUR Docker Hub username
                    sh 'docker build -t dhayag/multishop-frontend:latest .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // This securely opens the Jenkins vault to grab your token
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    // 1. Log in to Docker Hub using the hidden credentials
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    // 2. Push the image to your public repository
                    sh 'docker push dhayag/multishop-frontend:latest'
                }
            }
        }
    }
}