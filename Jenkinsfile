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
                sh 'docker exec Olympic-Container /bin/bash -c "source myenv/bin/activate && cd /var/www/html/Final_year_Project/ && pwd  && git pull origin master --force && service apache2 restart"'
            }
        }
    }       
