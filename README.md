# Automation

# About The Project

This project does the automation testing for the web browser and also on basis of automation, filters the important data and stores them in a file. That file automatically created and updated on regular basis as we execute the cases.
Apart from this, this project also filters out some code from important static sites like JavaTPoint and Tutorials Point and through automation only, filters out the code written in those files and test them regularly with the help of Jenkins pipeline. Thus, its help in checking the perfection of site in terms of code written there and also check the updating of code, their status and finally keep track of the stability of site.
Jenkins also keep record of this GitHub and of the CD/CI (Continuous Delivery and Contiguous Integration) process of the various site.


# Project Requirement And Setup

1. Selenium web Driver (Compatible to your browser , you can choose any, here used one is of Opera )
Note :-  Need to setup the path according to your path of webdriver
2. Python 3 or above version
3. PyCharm or any Development enviroment for executing python codes
5. Add pip (It comes by-default with python version > 3) and includ pip install --selenium
4. Needs to setup Jenkins with default plugings installed
5. Add Pipeline through jenkins by giving the master link of this github and file name as jenkinsfile.

# Sample Output
Please refer to the below link for the sample output :-
https://drive.google.com/file/d/1-vyJsq-_LMU9wjPEWe3FlABdcEnz5EWf/view?usp=drivesdk

# Command to generate allure report
python -m pytest Analysis.py --alluredir ./result


allure serve ./result/


