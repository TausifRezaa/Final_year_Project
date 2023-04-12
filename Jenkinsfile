pipeline {
    agent {
        label 'My_Agent'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh ' docker start Olympic-Container'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'docker exec Olympic-Container /bin/bash'
                sh 'docker exec Olympic-Container /bin/bash -c "service apache2 restart" '
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker exec Olympic-Container /bin/bash -c "git pull origin master" '
                sh 'docker exec Olympic-Container /bin/bash -c "service apache2 restart" '
            }
        }
    }
}
