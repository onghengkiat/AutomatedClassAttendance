from selenium import webdriver
from datetime import datetime
from page import LoginPage, ProfilePage, CoursePage, StatusPage, AttendancePage

SCHEDULE = [
    {"code": "WIX2001", "time": [
        {"day": "Monday", "begin": "15", "end": "18"}
    ]},
    {"code": "WIX2002", "time": [
        {"day": "Wednesday", "begin": "09", "end": "11"},
        {"day": "Friday", "begin": "09", "end": "10"}
    ]},
    {"code": "WIA2001", "time": [
        {"day": "Tuesday", "begin": "13", "end": "15"},
        {"day": "Thursday", "begin": "15", "end": "16"}
    ]},
    {"code": "WIA2003", "time": [
        {"day": "Monday", "begin": "09", "end": "11", "password": "1pjir6"},
        {"day": "Wednesday", "begin": "14", "end": "15"}
    ]},
    {"code": "GLT1011", "time": [
        {"day": "Tuesday", "begin": "16", "end": "19"}
    ]}]

USERNAME = "username"
PASSWORD = "password"

current_time = datetime.now()
current_day = current_time.strftime("%A")
current_hour = current_time.strftime("%H")

for course in SCHEDULE:
    course_code = course['code']
    times = course['time']
    for time in times:
        if time['day'] == current_day and time['begin'] <= current_hour <= time['end']:
            password = time['password']
            driver = webdriver.Chrome("chromedriver_linux64/chromedriver")
            driver.get(
                "https://casv.um.edu.my/cas/loginAllType?service=https%3A%2F%2Fspectrum.um.edu.my%2Flogin%2Findex.php")

            loginPage = LoginPage(driver)
            loginPage.login(USERNAME, PASSWORD)
            while True:
                try:
                    profilePage = ProfilePage(driver)
                    profilePage.select_course(course_code)
                    coursePage = CoursePage(driver)
                    coursePage.enter_status_page()
                    statusPage = StatusPage(driver)
                    if not statusPage.attendance_signed():
                        statusPage.enter_attendance_page()
                        attendancePage = AttendancePage(driver)
                        if password is not None:
                            attendancePage.sign_attendance(password=password)
                        else:
                            attendancePage.sign_attendance()
                    break
                except:
                    try:
                        loginPage = LoginPage(driver)
                        loginPage.login(USERNAME, PASSWORD)
                    except:
                        driver.quit()
                        break

