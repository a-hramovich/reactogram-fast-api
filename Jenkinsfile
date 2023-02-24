pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'uvicorn main:app --reload --port 8001'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh """curl -X 'GET' \
  'http://127.0.0.1:8001/post/all' \
  -H 'accept: application/json'"""
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
