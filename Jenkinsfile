pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('install deps') {
            steps {
                sh '''
                    cd app_python
                    pip install -r requirements.txt -r requirements-dev.txt
                '''
            }
        }
        stage('lint and test') {
            steps {
                sh '''
                    black --check .
                    python run_tests.py
                '''
            }
        }
    }
}
