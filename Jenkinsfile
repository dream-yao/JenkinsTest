Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 test.py'
            }
        }
        stage('test') {
            steps {
                sh 'python3 api_test.py'
            }
        }
    }
}
