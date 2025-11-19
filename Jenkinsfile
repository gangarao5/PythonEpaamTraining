// // pipeline {
// //     agent any
// //     stages {
// //         stage('Checkout') {
// //             steps {
// //                 git branch: 'main', url: 'https://github.com/gangarao5/PythonEpaamTraining.git'
// //             }
// //         }
// //         stage('Build') {
// //             steps {
// //                 echo 'Building...'
// //             }
// //         }
// //     }
// // }
//
//
// pipeline {
//     agent any
//
//     environment {
//         PYTHON_VERSION = "3.10"
//     }
//
//     stages {
//         stage('Checkout') {
//             steps {
//                 // Pull code from Git repository
//                 git branch: 'R_main', url: 'https://github.com/gangarao5/PythonEpaamTraining.git'
//                 credentialsId: 'abde241b-f18a-469f-85cf-1f0ce67df100'
//             }
//         }
//
//         stage('Setup Python') {
//             steps {
//                 sh '''
//                 python3 --version
//                 python3 -m pip install --upgrade pip
//                 pip install -r requirements.txt
//                 pip install pytest
//                 '''
//             }
//         }
//
//         stage('Run Script') {
//             steps {
//                 sh '''
//                 echo "Running Python script..."
//                 pytest C:\\Users\\VeeraGangarao\PycharmProjects\\PythonEpaamTraining\\sample_pytest.py
//                 '''
//             }
//         }
//
//         stage('Post Actions') {
//             steps {
//                 echo 'Pipeline completed successfully!'
//             }
//         }
//     }
//
//     post {
//         always {
//             echo 'Cleaning up workspace...'
//             cleanWs()
//         }
//     }









pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'R_main',
                    url: 'https://github.com/gangarao5/PythonEpaamTraining.git',
                    credentialsId: 'abde241b-f18a-469f-85cf-1f0ce67df100'
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python --version
                python -m pip install --upgrade pip
                pip install -r requirements.txt;

                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                echo "Running pytest..."
                pytest sample_pytest.py
                '''
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Pipeline completed successfully!'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}