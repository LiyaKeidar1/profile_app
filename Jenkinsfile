pipeline {
    agent {
        kubernetes {
            label 'slave'
            yamlFile 'build-pod.yaml'
            defaultContainer 'ez-docker-helm-build'
        }
    }
    environment {
        // Set environment variables if needed
        DOCKER_HUB_CREDENTIALS = credentials('9d695493-685a-4593-9ce1-834966410c90') // Use the ID of your Docker Hub credentials
        IMAGE_NAME = 'liyakeidar1/profileapp'
    }

    stages {
        stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }
        stage('Unit Testing') { // Perform unit testing
      steps {
        script {
          sh """
          pytest test_app.py
          """
        }
      }
    }

        stage('Build') {
            steps {
                script {
                    echo "Building the application..."
                    git branch: 'feature_application', url= "https://github.com/LiyaKeidar1/profile_app.git"
                    def customImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}", ".")
                    echo 'Docker build completed.'


            }
        }

        stage('Push Docker Image')
        {
    steps
    {
        script
        {
            echo 'Starting Docker push...'

            // Log in to Docker Hub using credentials
            withCredentials([usernamePassword(credentialsId: 'liya_dockerhub_cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh '''
                echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                docker push "${IMAGE_NAME}:${env.BUILD_NUMBER}"
                '''
            }

            echo 'Docker push completed.'
        }
    }
}

    post {
        success {
            echo 'Docker image pushed successfully.'
        }
    }
}





