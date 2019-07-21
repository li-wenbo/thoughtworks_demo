pipeline {
    agent none

    parameters {
        string defaultValue: 'latest', description: 'the repo version we want to', name: 'tag', trim: false
        string defaultValue: '3333', description: 'the publish port for proxy container', name: 'HTTP_PUBLISH_PORT', trim: false
    }

    environment {
        RegistryEndpoint = 'registry.cn-hangzhou.aliyuncs.com'
        RegistryURL = "https://${RegistryEndpoint}"
        RegistryURLCID = '4f97170a-5618-4d63-a7a0-761b425b7970'

        AppImageName = "${env.JOB_NAME}-app:${params.tag}"
        ProxyImageName = "${env.JOB_NAME}-proxy:${params.tag}"
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

        stage('build the app image') {
            agent any
            steps {

                script {
                    docker.withRegistry("$RegistryURL", "$RegistryURLCID") {
                        def customImage = docker.build("${AppImageName}")

                        def imageid = customImage.id
                        def rv = sh returnStatus: true, script: "docker run --rm $imageid python test_flask.py"
                        if (rv == 0) {
                            customImage.push "${params.tag}"
                        }
                    }
                }
            }
        }


        stage('build the proxy image') {
            agent any
            environment {
                BUILD_ARGS = "-f Dockerfile.nginx"
            }

            steps {

                script {
                    docker.withRegistry("$RegistryURL", "$RegistryURLCID") {
                        def customImage = docker.build("${ProxyImageName}", "$BUILD_ARGS .")
                        customImage.push "${params.tag}"
                    }
                }
            }
        }


        stage('pre deploy') {
            agent any
            steps {
                // pre
                sh 'docker network rm oops || true'
                sh 'docker container stop proxy || true'
                sh 'docker container rm proxy || true'
                sh 'docker container stop app || true'
                sh 'docker container rm app || true'
            }
        }

        stage('deploy') {
            agent any

            steps {

                // create docker brige network
                sh 'docker network create oops'

                // create app container
                sh "docker run -d --rm -e 'ENVIRON=${env.BRANCH_NAME}' --network=oops --name app ${RegistryEndpoint}/${AppImageName}"

                // create proxy container
                sh "docker run -d --rm -p ${params.HTTP_PUBLISH_PORT}:80 --network=oops --name proxy ${RegistryEndpoint}/${ProxyImageName}"
            }
        }
    }
}