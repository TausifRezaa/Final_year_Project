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
                sh 'docker exec Olympic-Container /bin/bash -c "source myenv/bin/activate"'
                sh 'docker exec Olympic-Container /bin/bash -c "cd Final_year_Project" '
                sh 'docker exec Olympic-Container /bin/bash -c "pwd"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker exec Olympic-Container /bin/bash -c "git remote -v" '
                sh 'docker exec Olympic-Container /bin/bash -c "git pull origin master --force" '
                sh 'docker exec Olympic-Container /bin/bash -c "service apache2 restart" '
            }
        }
    }
}
