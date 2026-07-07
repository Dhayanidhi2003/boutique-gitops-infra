pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Frontend Image') {
            steps {
                dir('app-source') {
                    sh 'docker build -t dhayag/multishop-frontend:latest .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push dhayag/multishop-frontend:latest'
                }
            }
        }
        // 👇 ADD THIS NEW DEPLOY STAGE 👇
        stage('Deploy to AWS Server') {
            steps {
                // 1. Stop and remove any old versions of the website if they exist
                sh 'docker stop multishop-live || true'
                sh 'docker rm multishop-live || true'
                
                // 2. Download the latest image from Docker Hub and run it on port 80
                sh 'docker run -d --name multishop-live -p 80:80 dhayag/multishop-frontend:latest'
            }
        }
    }
}