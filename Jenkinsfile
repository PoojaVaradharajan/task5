
pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: '832db760-38e4-491b-96b0-62e9c6d7bc22', url: 'https://github.com/PoojaVaradharajan/task5.git'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarScanner with the necessary parameters
                    sh 'sonar-scanner.bat -D"sonar.projectKey=task5" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_cd95d7cf4434635a7f97b39d4d1595e016fd7e6e"'
                }
            }
        }
    }
}
