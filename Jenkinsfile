// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                //sh 'source /var/lib/jenkins/workspace/venv/bin/activate && python test.py'
                sh 'source /var/lib/jenkins/workspace/venv/bin/activate && pip list'
                echo 'api has lanched'
            }
        }
        stage('test') {
            steps {
                sh 'source /var/lib/jenkins/workspace/venv/bin/activate && python -m unittest api_test.py'
                echo 'test has finished'
                /* publishHTML (target : [allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'myreport.html',
                reportName: 'My Reports',
                reportTitles: 'The Report']) */
            }
        }
    }
}