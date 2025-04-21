pipeline {
    agent any

    environment {
        IMAGE_NAME = "bookstore"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Pragati-K26/Bookstore.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
