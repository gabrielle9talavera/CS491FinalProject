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
                export PYTHONPATH=$WORKSPACE:$PYTHONPATH
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