from selenium import webdriver
import time
import Xpaths
import Ids
import Constants
import Urls

driver = webdriver.Opera(
    executable_path='C:\\Users\\aj250065\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe')

# Opening JavaTPoint Url
driver.get(Urls.JavaTPointUrl)
# Wait for Page to Load
time.sleep(Constants.TwoSeconds)

# Opening Python Tab
driver.find_element_by_xpath(Xpaths.PythonTab).click()
# Wait for page to load
time.sleep(Constants.TwoSeconds)

# Going Tab To Tab and creating notes
python_Notes = driver.find_element_by_xpath("(//*[@id='city']//p)[5]").text

# Updating notes in File
fileNotes = open('../pythonProject1/FilesCollected/JavaTPointNotes/Python.txt', 'w')
fileNotes.write("Notes For Python \n")
fileNotes.write("Introduction To Python \n")
fileNotes.write(python_Notes)
fileNotes.close()

# Updating the program (Code 1#)
code1 = driver.find_element_by_xpath(Xpaths.Code1).text

file = open('../pythonProject1/ExtractedProgram/JavaTPoint/JavaTPointProgram1.py', 'w')
file.write(code1)
file.close()

# Updating the program (Code 2#)
code2 = driver.find_element_by_xpath(Xpaths.Code2).text

file = open('../pythonProject1/ExtractedProgram/JavaTPoint/JavaTPointProgram2.py', 'w')
file.write(code2)
file.close()

# Updating the program (Code 3#)
code3 = driver.find_element_by_xpath(Xpaths.Code3).text

file = open('../pythonProject1/ExtractedProgram/JavaTPoint/JavaTPointProgram3.py', 'w')
file.write(code3)
file.close()










