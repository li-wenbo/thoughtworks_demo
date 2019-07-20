pipeline {
    agent none

    parameters {
        booleanParam defaultValue: true, description: 'is we are running the testing', name: 'Testing'
        string defaultValue: 'latest', description: 'the repo version we want to', name: 'tag', trim: false
        string defaultValue: '8080', description: 'the http_port web server will listen on', name: 'HTTP_PORT', trim: false
    }

    environment {
        RegistryURL = "https://registry.cn-hangzhou.aliyuncs.com"
        RegistryURLCID = "4f97170a-5618-4d63-a7a0-761b425b7970"
    }

    stages {
        stage('dev') {
            agent any

            when {
                branch 'dev'
            }

            steps {
                echo 'in dev'
            }
        }

        stage('test') {
            agent any
            environment {
                BUILD_ARGS = "--build-arg HTTP_PORT=${params.HTTP_PORT}"
            }

            when {
                branch 'testing'
            }

            steps {

                echo 'oops'
                script {
                    docker.withRegistry("$RegistryURL", "$RegistryURLCID") {
                        def customImage = docker.build("$env.JOB_NAME:latest", "$BUILD_ARGS .")
                        customImage.push 'latest'
                    }
                }
            }
        }

        stage('deploy') {
            agent any

            when {
                branch 'master'
            }

            steps {
                echo 'in deploy'
            }
        }
    }
}