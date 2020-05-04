pipeline {
    agent {docker {
                    image 'python:3.8-slim-buster' 
                } }
    stages {
        stage('Build') { 
            // agent {
            //     docker {
            //         image 'python:3.8-slim-buster' 
            //     }
            // }
            steps {
                // // sh 'sudo -H pip3 install mock'
                // sh 'sudo -H pip3 install --upgrade pip'
                // sh 'sudo -H pip3 install networkx'
                // sh 'sudo -H pip3 install numpy'
                sh 'export PYTHONPATH=$WORKSPACE:$PYTHONPATH'
                sh 'virtualenv environment_name -p python3'
                sh 'source environment_name/bin/activate'
                sh "pip installnetworkx'
                sh 'python3 -m py_compile sources/Node.py sources/NodeFailure.py sources/Path.py sources/sim.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        stage('Test') {
            // agent {
            //     docker {
            //         image 'qnib/pytest'
            //     }
            // }
            steps {
                // sh 'py.test --junit-xml test-reports/results.xml sources/PathTest.py'
                sh 'python3 sources/PathTest.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}