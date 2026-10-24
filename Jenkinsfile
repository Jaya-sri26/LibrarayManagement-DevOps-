pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo "Building Docker Image"
                bat "docker build -t libraryapp ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"

                bat "docker login -u jaya02sri26 -p Jaya@sri26"
            }
        }

        stage('Push Image') {
            steps {
                echo "Tagging Docker Image"

                bat "docker tag libraryapp jaya02sri26/library:latest"

                echo "Pushing Docker Image"

                bat "docker push jaya02sri26/library:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"

                bat "kubectl apply -f k8s/deployment.yaml"

                bat "kubectl apply -f k8s/service.yaml"
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}