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

        net_name = "${env.BRANCH_NAME}-net"
        app_name = "${env.BRANCH_NAME}-app"
        proxy_name = "${env.BRANCH_NAME}-proxy"
    }

    stages {
        stage('production') {
            agent any

            when {
                branch 'master'
            }

            steps {
                echo 'in production'
            }
        }

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
                BUILD_ARGS = "--build-arg APP_NAME=${app_name} -f Dockerfile.nginx"
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
                sh "docker container stop ${proxy_name} || true"
                sh "docker container rm ${proxy_name} || true"
                sh "docker container stop ${app_name} || true"
                sh "docker container rm ${app_name} || true"
                sh "docker network rm ${net_name}"
            }
        }

        stage('deploy') {
            agent any

            steps {

                // create docker brige network
                sh "docker network create ${net_name}"

                // create app container
                sh "docker run -d --rm -e 'ENVIRON=${env.BRANCH_NAME}' --network=${net_name} --name ${app_name} ${RegistryEndpoint}/${AppImageName}"


                sleep 1
                // create proxy container
                sh "docker run -d --rm -p ${params.HTTP_PUBLISH_PORT}:80 --network=${net_name} --name ${proxy_name} ${RegistryEndpoint}/${ProxyImageName}"
            }
        }
    }
}
