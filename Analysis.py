from selenium import webdriver
import time
import Xpaths
import Ids
import Constants
import Urls
import allure
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Opera(
        executable_path='C:\\Users\\Administrator\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe'
    )
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()


@allure.description("validate login credentials")
@allure.severity(severity_level="CRITICAL")
def test_javaTpoint(test_setup):
    """

    :param test_setup:
    """
    # Opening JavaTPoint Url
    driver.get(Urls.JavaTPointUrl)
    # Wait for Page to Load
    time.sleep(Constants.TwoSeconds)

    # Opening Python Tab
    driver.find_element_by_xpath(Xpaths.PythonTab).click()
    # Wait for page to load
    time.sleep(Constants.TwoSeconds)

    # Going Tab To Tab and extracting notes
    python_Notes = driver.find_element_by_xpath(Xpaths.PythonNotesJavaTPoint).text

    # Updating notes in File
    fileNotes = open('../Automation/FilesCollected/JavaTPointNotes/Python.txt', 'w')
    fileNotes.write("Notes For Python \n")
    fileNotes.write("Introduction To Python \n")
    fileNotes.write(python_Notes)
    fileNotes.close()

    # Updating the program (Code 1#)
    code1 = driver.find_element_by_xpath(Xpaths.Code1).text

    file = open('../Automation/ExtractedProgram/JavaTPoint/JavaTPointProgram1.py', 'w')
    file.write(code1)
    file.close()

    # Updating the program (Code 2#)
    code2 = driver.find_element_by_xpath(Xpaths.Code2).text

    file = open('../Automation/ExtractedProgram/JavaTPoint/JavaTPointProgram2.py', 'w')
    file.write(code2)
    file.close()

    # Updating the program (Code 3#)
    code3 = driver.find_element_by_xpath(Xpaths.Code3).text

    file = open('../Automation/ExtractedProgram/JavaTPoint/JavaTPointProgram3.py', 'w')
    file.write(code3)
    file.close()


@allure.description("validate tutorialspoint")
@allure.severity(severity_level="CRITICAL")
def test_tutorialsPoint(test_setup):
    """

    :param test_setup:
    """
    # Opening JavaTPoint Url
    driver.get(Urls.TutorialsPointUrl)
    driver.maximize_window()
    # Wait for Page to Load
    time.sleep(Constants.TwoSeconds)

    # Going Tab To Tab and extracting notes
    python_Notes = driver.find_element_by_xpath(Xpaths.PythonNotesTutorialsPoint_1).text

    # Updating notes in File
    fileNotes = open('../Automation/FilesCollected/TutorialsPointNotes/Python.txt', 'w')
    fileNotes.write("Notes For Python \n")
    fileNotes.write("Introduction To Python \n")
    fileNotes.write(python_Notes)
    fileNotes.close()

    # Updating the program (Code 1#)
    driver.find_element_by_xpath(Xpaths.tp_operators).click()
    time.sleep(Constants.TwoSeconds)
    code1 = driver.find_element_by_xpath(Xpaths.Code1_tp).text

    file = open('../Automation/ExtractedProgram/TutorialPoint/TutorialsPointProgram1.py', 'w')
    file.write(code1)
    file.close()

    # Updating the program (Code 2#)
    driver.find_element_by_xpath(Xpaths.tp_functions).click()
    time.sleep(Constants.ThreeSeconds)
    code2 = driver.find_element_by_xpath(Xpaths.Code2_tp).text

    file = open('../Automation/ExtractedProgram/TutorialPoint/TutorialsPointProgram2.py', 'w')
    file.write(code2)
    file.close()

    # Updating the program (Code 2#)
    code3 = driver.find_element_by_xpath(Xpaths.Code3_tp).text

    file = open('../Automation/ExtractedProgram/TutorialPoint/TutorialsPointProgram3.py', 'w')
    file.write(code3)
    file.close()


@allure.description("validate geeksforgeeks")
@allure.severity(severity_level="CRITICAL")
def test_geeksForGeeks(test_setup):
    """

    :param test_setup:
    """
    # Opening GeeksForGeeks Url
    time.sleep(Constants.TwoSeconds)
    driver.get(Urls.GeeksForGeeks)
    # Wait for Page to Load
    time.sleep(Constants.TwoSeconds)
    driver.maximize_window()
    time.sleep(Constants.TwoSeconds)

    # Authentication
    driver.find_element_by_xpath(Xpaths.AuthenticationButton).click()
    time.sleep(Constants.TwoSeconds)

    # Adding loginId and password
    # Login Id
    driver.find_element_by_id(Ids.Username).click()
    driver.find_element_by_id(Ids.Username).send_keys(Constants.SampleMailId)
    # Password
    driver.find_element_by_id(Ids.Password).click()
    driver.find_element_by_id(Ids.Password).send_keys(Constants.SamplePassword)
    driver.find_element_by_xpath(Xpaths.SignInButton).click()
    time.sleep(Constants.FourSeconds)

    # Updating notes in File
    file = open('../Automation/FilesCollected/GeeksForGeeks/AutomationResult.txt', 'w')
    file.write("Extracting Results \n")
    file.write("Site Name :- \n")
    file.write("Site URL :- \n")
    file.write(driver.current_url)
    file.write(" ... \n")
    file.write(".................Account Information.................... \n")

    # Task 1 :- Visualizing the profile
    driver.find_element_by_xpath(Xpaths.UserProfileId).click()
    driver.find_element_by_xpath(Xpaths.UserInformation).click()
    time.sleep(Constants.TwoSeconds)

    # 1. Basic Page
    file.write("..................Basic Information......................\n\n")
    driver.find_element_by_xpath(Xpaths.MyProfile).click()
    time.sleep(Constants.ThreeSeconds)

    # 1.1 Extracting the profile data
    name = driver.find_element_by_xpath(Xpaths.Name).text
    file.write("Name :- " + name + "  \n")
    institution = driver.find_element_by_xpath(Xpaths.InstitutionName).text
    file.write("Institution Name :- " + institution + "  \n")
    emailId = driver.find_element_by_xpath(Xpaths.EmailId).text
    file.write("Email Id id :- " + emailId + " \n")

    # 1.2 About Courses And other
    file.write("..............1.2 Information about courses and others................\n\n")
    driver.find_element_by_xpath(Xpaths.Practice).click()
    time.sleep(Constants.ThreeSeconds)
    courses = driver.find_element_by_xpath(Xpaths.Courses).text
    file.write("Courses Attended :- " + courses + " \n")

    # 1.3 Search Other tabs (Feeds/ Interest)
    driver.find_element_by_xpath(Xpaths.FeedSection).click()
    time.sleep(Constants.TwoSeconds)
    # Interest Section
    driver.find_element_by_xpath(Xpaths.InterestSection).click()
    time.sleep(Constants.TwoSeconds)

    # Go Back To Main Page
    driver.find_element_by_xpath(Xpaths.GfgBackIcon).click()
    time.sleep(Constants.ThreeSeconds)

    # Sectioning Other Labels (Tutorials --> Algorithm Page --> Analysis Of Algorithm --> Asymptotic Notation
    driver.find_element_by_xpath(Xpaths.Tutorials).click()
    driver.find_element_by_xpath(Xpaths.AlgorithmPage).click()
    driver.find_element_by_xpath(Xpaths.AlgorithmAnalysisPage).click()
    driver.find_element_by_xpath(Xpaths.AsymptoticNotationPage).click()
    time.sleep(Constants.ThreeSeconds)

    # Adding Course
    title = driver.find_element_by_xpath(Xpaths.TitleOfPage).text
    file.write("...............Sample Learning..................\n")
    file.write(title + "    \n")
    text = driver.find_element_by_xpath(Xpaths.TextAsymptoticNotation).text
    file.write(text)

    driver.find_element_by_xpath(Xpaths.Logo).click()
    time.sleep(Constants.ThreeSeconds)

    file.write("\n\n ..........................End Of Sample Learning.......................\n\n")

    # Courses Page
    driver.find_element_by_xpath(Xpaths.CoursesPage).click()
    time.sleep(Constants.FourSeconds)

    # get Hired Page
    driver.find_element_by_xpath(Xpaths.GetHiredPage).click()
    time.sleep(Constants.FourSeconds)

    driver.find_element_by_id(Ids.Search).send_keys(Constants.Teradata)
    driver.find_element_by_id(Ids.Search).send_keys(Keys.RETURN)
    time.sleep(Constants.TenSeconds)
    driver.find_element_by_xpath(Xpaths.CrossPage).click()

    # Go To Back-page
    driver.find_element_by_xpath(Xpaths.BackButton).click()

    file.write(".................Thanks For Visiting..............")
    file.close()
    driver.close()

    file.close()