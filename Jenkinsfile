pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                cd extractedProgram/JavaTPoint
                python JavaTPointProgram1.py
                python JavaTPointProgram2.py
                python JavaTPointProgram3.py
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                cd extractedProgram/TutorialPoint
                python TutorialsPointProgram1.py
                python TutorialsPointProgram2.py
                python TutorialsPointProgram3.py
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                cd extractedProgram/TutorialPoint
                python TutorialsPointProgram1.py
                python TutorialsPointProgram2.py
                python TutorialsPointProgram3.py
                cd ..
                cd extractedProgram/JavaTPoint
                python JavaTPointProgram1.py
                python JavaTPointProgram2.py
                python JavaTPointProgram3.py
            }
        }
    }
}
