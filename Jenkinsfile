pipeline {
    agent {
        kubernetes {
            label 'slave'
            yamlFile 'build-pod.yaml'
            defaultContainer 'ez-docker-helm-build'
        }
    }

    environment {
        IMAGE_NAME = 'liyakeidar1/profileapp'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'feature_application']],
                        userRemoteConfigs: [[url: 'https://github.com/LiyaKeidar1/profile_app.git']]
                    ])
                    def customImage = docker.build("${IMAGE_NAME}:latest", ".")
                    echo 'Docker build completed.'
                }
            }
        }

//         stage('Testing') {
//             steps {
//                 script {
//                     sh 'docker run --rm liyakeidar1/profileapp pytest test_app.py'
//                 }
//             }
//         }

        stage('Push Docker Image') {
            steps {
                script {
                    echo 'Starting Docker push...'

                    // Log in to Docker Hub using credentials
                    withCredentials([usernamePassword(credentialsId: 'liya_dockerhub_cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push "${IMAGE_NAME}:latest"
                        '''
                    }

                    echo 'Docker push completed.'
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image pushed successfully.'
        }
    }
}
