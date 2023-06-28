pipeline {
    agent any
    
    stages {
        stage("Checkout from repo and build docker image") {
            steps {
                // Source repo url
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub', url: 'https://github.com/Biswajit1693/CI-CD-deployment']])
                // Build docker image
                sh 'sudo docker build -t helloapp:latest .'
                sh 'sudo docker run -d helloapp:latest'
            }
        }
        
        stage("Push to dockerhub") {
            steps {
                // Login to Dockerhub
                withCredentials([string(credentialsId: 'docker-passwd', variable: 'dockerpssd')]) {
                sh 'sudo docker login -u jeetlinux -p ${dockerpssd}'
                    
                }
                
                // push the image to dockerhub
                sh 'sudo docker tag helloapp:latest jeetlinux/demo-docker:v10'
                sh 'sudo docker push jeetlinux/demo-docker:v10'
                
            }
        }
        
        stage("Deploy") {
            steps {
                withCredentials([file(credentialsId: 'kubemini', variable: 'KUBECONFIG')]) {
                sh 'export KUBECONFIG=$KUBECONFIG'
                
                //deployment
                
                sh 'kubectl apply -f deployment.yaml --force'
                
                }
            }
        }
        
    }

}
