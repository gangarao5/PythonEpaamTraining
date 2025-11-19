pipeline{
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/gangarao5/PythonEpaamTraining.git'
            }
        }
        stage('Install Dependencies')
        {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}






// pipeline {
//     agent any
//
//     environment {
//         PYTHON = 'python'
//     }
//
//     stages {
//         stage('Checkout') {
//             steps {
//                 echo 'Checking out source code...'
//                 git branch: 'R_main', url: 'https://github.com/gangarao5/PythonEpaamTraining.git'
//             }
//         }
//
//         stage('Setup Python') {
//             steps {
//                 echo 'Setting up Python environment...'
//                 bat "${PYTHON} --version"
//                 bat "${PYTHON} -m pip install --upgrade pip"
//                 bat "pip install -r requirements.txt"
//                 bat "pip install pytest pytest-html"
//             }
//         }
//
//         stage('Run Tests') {
//             steps {
//                 echo 'Running Pytest with HTML report...'
//                 bat "pytest --maxfail=50 --disable-warnings --junitxml=reports/results.xml --html=reports/results.html --self-contained-html"
//             }
//         }
//
//         stage('Publish Reports') {
//             steps {
//                 echo 'Publishing test results...'
//                 junit 'reports/results.xml'
//                 archiveArtifacts artifacts: 'reports/results.html', fingerprint: true
//             }
//         }
//
//         stage('Post Actions') {
//             steps {
//                 echo 'Cleaning up workspace...'
//                 cleanWs()
//             }
//         }
//     }
//
//     post {
//         success {
//             echo '✅ Pipeline completed successfully!'
//         }
//         failure {
//             echo '❌ Pipeline failed. Check logs for details.'
//         }
//     }
// } // ✅ Make sure this closing brace exists