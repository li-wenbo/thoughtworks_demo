pipeline {
    agent none

    stages {
        stage('dev') {
            agent any
            steps {
                echo 'in dev'
            }
        }

        stage('test') {
            agent any
            steps {
                echo 'in test'
            }
        }

        stage('deploy') {
            agent any
            steps {
                echo 'in deploy'
            }
        }
    }
}