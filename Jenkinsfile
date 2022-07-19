pipeline {
    agent {
        docker {
            image 'funnyzak/java-node-python-go-etc'
            args '-u root:root'
        }
    }
    triggers { pollSCM ('* * * * *') }
    stages {
        stage('Prepare') {
            steps {
                //sh 'yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm'
                sh 'cd /etc/yum.repos.d/'
                sh "sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*"
                sh "sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*"
                sh 'yum install epel-release -y'
                sh 'yum install jq -y'
                sh 'jq -Version'
            }
        }
        
        stage('Get dependencies') {
            environment {
                GITHUB_REPOSITORY = "BasyninNikita/practice_ci"
            }
            
            steps {
                script {
                    LANGS = sh ( script: "curl -s https://api.github.com/repos/${env.GITHUB_REPOSITORY}/languages | jq 'keys'| tr -d '\n []'", returnStdout: true)
                    sh "echo ${LANGS}"
                }
                sh "python3 dependencies.py ${LANGS} > deps.txt"
            }
            post {
                always {
                    archiveArtifacts artifacts: 'deps.txt', onlyIfSuccessful: false
                }
            }
        }
    }
}
