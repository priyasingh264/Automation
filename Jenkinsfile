pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                python JavaTPointProgram1.py
                python JavaTPointProgram2.py
                python JavaTPointProgram3.py
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                python TutorialsPointProgram1.py
                python TutorialsPointProgram2.py
                python TutorialsPointProgram3.py
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                python TutorialsPointProgram1.py
                python TutorialsPointProgram2.py
                python TutorialsPointProgram3.py
                python JavaTPointProgram1.py
                python JavaTPointProgram2.py
                python JavaTPointProgram3.py
            }
        }
    }
}
