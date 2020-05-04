pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'pip3 install mock --user'
                sh 'pip3 install --upgrade pip --user'
                sh 'pip3 install networkx --user'
                sh 'pip3 install numpy --user'
                sh 'python -m py_compile sources/Node.py sources/NodeFailure.py sources/Path.py sources/sim.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml sources/PathTest.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}