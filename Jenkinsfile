pipeline {
    agent none

    parameters {
        string defaultValue: 'latest', description: 'the repo version we want to', name: 'tag', trim: false
        string defaultValue: '8080', description: 'the http_port web server will listen on', name: 'HTTP_PORT', trim: false
        string defaultValue: '8080', description: 'the publish port http_port', name: 'HTTP_PUBLISH_PORT', trim: false
        string defaultValue: 'test', description: 'should be one of "production, dev, test", or the test default', name: 'ENVIRON', trim: false
    }

    environment {
        RegistryEndpoint = 'registry.cn-hangzhou.aliyuncs.com'
        RegistryURL = "https://$RegistryEndpoint"
        RegistryURLCID = '4f97170a-5618-4d63-a7a0-761b425b7970'
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

            when {
                branch 'testing'
            }

            steps {
                echo 'in testing'
            }
        }

        stage('build the image') {
            agent any
            environment {
                BUILD_ARGS = "--build-arg HTTP_PORT=${params.HTTP_PORT} --build-arg ENVIRON=${params.ENVIRON}"
            }

            steps {

                script {
                    docker.withRegistry("$RegistryURL", "$RegistryURLCID") {
                        def customImage = docker.build("${env.JOB_NAME}:${params.tag}", "$BUILD_ARGS .")

                        def imageid = customImage.id
                        def rv = sh returnStatus: true, script: "docker run --rm $imageid python test_flask.py"
                        if (rv == 0) {
                            customImage.push "${params.tag}"
                        }
                    }
                }
            }
        }

        stage('deploy') {
            agent any

            steps {
                sh "docker run -d --rm -p ${params.HTTP_PUBLISH_PORT}:${params.HTTP_PORT} ${RegistryEndpoint}/${env.JOB_NAME}:${params.tag}"
            }
        }


    }
}