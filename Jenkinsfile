pipeline {
    agent any  
    environment {
        PYTHON_HOME = '/usr/bin/python3' 
    }
	
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:moranlj-git/jenkins-pipeline-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt' // Assumes pip is available in the PATH
            }
        }

        stage('Run Scraper') {
            steps {
                sh 'python scraper.py'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'data.csv', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
