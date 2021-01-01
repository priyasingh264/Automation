from selenium import webdriver
import time
import Xpaths
import Ids
import Constants
import Urls

driver = webdriver.Opera(
    executable_path='C:\\Users\\aj250065\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe')

# Opening JavaTPoint Url
driver.get(Urls.TutorialsPointUrl)
driver.maximize_window()
# Wait for Page to Load
time.sleep(Constants.TwoSeconds)

# Going Tab To Tab and extracting notes
python_Notes = driver.find_element_by_xpath(Xpaths.PythonNotesTutorialsPoint_1).text

# Updating notes in File
fileNotes = open('../pythonProject1/FilesCollected/TutorialsPointNotes/Python.txt', 'w')
fileNotes.write("Notes For Python \n")
fileNotes.write("Introduction To Python \n")
fileNotes.write(python_Notes)
fileNotes.close()

# Updating the program (Code 1#)
driver.find_element_by_xpath(Xpaths.tp_operators).click()
time.sleep(Constants.TwoSeconds)
code1 = driver.find_element_by_xpath(Xpaths.Code1_tp).text

file = open('../pythonProject1/ExtractedProgram/TutorialPoint/TutorialsPointProgram1.py', 'w')
file.write(code1)
file.close()

# Updating the program (Code 2#)
driver.find_element_by_xpath(Xpaths.tp_functions).click()
time.sleep(Constants.ThreeSeconds)
code2 = driver.find_element_by_xpath(Xpaths.Code2_tp).text

file = open('../pythonProject1/ExtractedProgram/TutorialPoint/TutorialsPointProgram2.py', 'w')
file.write(code2)
file.close()

# Updating the program (Code 2#)
code3 = driver.find_element_by_xpath(Xpaths.Code3_tp).text

file = open('../pythonProject1/ExtractedProgram/TutorialPoint/TutorialsPointProgram3.py', 'w')
file.write(code3)
file.close()















