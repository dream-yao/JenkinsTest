// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'source /home/sun/venv/bin/activate && python test.py'
                echo 'api has lanched'
            }
        }
        stage('test') {
            steps {
                sh 'source /home/sun/venv/bin/activate && python -m unittest api_test.py'
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