pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git credentialsId: 'GitHub_Credentials_ID', url: 'https://github.com/PoojaVaradharajan/task5.git'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('SonarQube') {
                    bat 'sonar-scanner.bat'  // Using 'bat' instead of 'sh' for Windows
                }
            }
        }
    }
}
