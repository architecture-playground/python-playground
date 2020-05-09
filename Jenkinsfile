#!groovy
@Library('jenkins-libraries')_

properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }
    triggers { pollSCM('* * * * *') }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("Validate Commits") {
            when {
                expression {
                    return env.BRANCH_NAME != 'master';
                }
            }
            steps {
                validateCommits()
            }
        }
    }
}