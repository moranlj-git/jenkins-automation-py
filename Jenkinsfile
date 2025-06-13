pipeline {
    agent any  
    environment {
        PYTHON_HOME = '/usr/bin/python3' 
    }
	
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt' // Assumes pip is available in the PATH
            }
        }

        stage('Run Scraper') {
            steps {
                sh 'python3 scraper.py'
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
