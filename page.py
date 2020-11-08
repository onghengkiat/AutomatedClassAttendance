from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from elements import LoginPageElement, ProfilePageElement, CoursePageElement, StatusPageElement, AttendancePageElement
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    user_field = LoginPageElement("uname")
    password_field = LoginPageElement("password")
    status_field = LoginPageElement("domain")

    def select_status(self):
        status_select = Select(self.status_field)
        status_select.select_by_visible_text("Student")

    def login(self, username, password):
        self.user_field = username
        self.password_field = password
        self.select_status()
        login_button = self.driver.find_element_by_class_name("btn")
        # rest it for 5 seconds
        time.sleep(5)

        actions = ActionChains(self.driver)
        actions.click(login_button)
        actions.perform()
        return True


class ProfilePage(BasePage):
    courses = ProfilePageElement("coursename")

    def select_course(self, course_code):
        for course in self.courses:
            if course_code in course.text:
                course.click()
                break

        return True


class CoursePage(BasePage):
    event_element = CoursePageElement("event")

    def enter_status_page(self):
        link_to_attendance = self.event_element[0].find_element_by_tag_name("a")
        link_to_attendance.click()
        return True


class StatusPage(BasePage):
    status_element = StatusPageElement("statuscol")

    def attendance_signed(self):
        if self.status_element.text == 'Present':
            print("Attendance is already signed")
            return True
        else:
            return False

    def enter_attendance_page(self):
        self.status_element.click()


class AttendancePage(BasePage):
    password_field = AttendancePageElement("abc")
    status_field = AttendancePageElement("status")

    def select_status(self):
        status_select = Select(self.status_field)
        status_select.select_by_visible_text("Present")

    def sign_attendance(self, password=None):
        if password is not None:
            # enter password
            self.password_field = password

        submit_button = self.driver.find_element_by_class_name("submit")

        time.sleep(3)

        actions = ActionChains(self.driver)
        actions.click(submit_button)
        actions.perform()
        return True
