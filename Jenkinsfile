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
                sh 'docker exec Olympic-Container /bin/bash -c "source myenv/bin/activate && cd Final_year_Project && git pull origin master && service apache2 restart" '
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
