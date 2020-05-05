pipeline {
    agent none
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8-slim-buster' 
                }
            }
            steps {
                sh 'python -m py_compile sources/Node.py sources/NodeFailure.py sources/Path.py sources/sim.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'liuf2/pytest'
                }
            }
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install networkx && pip install numpy && pip install mock && python3 sources/NodeTest.py && python3 sources/PathTest.py && python3 sources/NodeFailureTest.py && python3 sources/IntegrationTests.py'
            }
        }
    }
}