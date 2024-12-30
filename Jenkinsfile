pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git credentialsId: '832db760-38e4-491b-96b0-62e9c6d7bc22', url: 'https://github.com/PoojaVaradharajan/task5.git'
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
