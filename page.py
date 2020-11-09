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
        index = 0
        for element in self.status_element :
            if element.text == "Submit Attendance":
                return index
            index = index + 1
        return -1

    def enter_attendance_page(self, index):
        self.status_element[index].click()


class AttendancePage(BasePage):
    submit_button = AttendancePageElement("submitbutton")

    def select_status(self):
        WebDriverWait(self.driver, 30).until(
            lambda driver : driver.find_elements_by_name("statusdesc")
        )
        status_select = self.driver.find_elements_by_name("statusdecs")
        for status in status_select:
            if status.text == "Present":
                status.click()
                break

    def sign_attendance(self, password=None):
        if password is not None:
            # enter password
            password_field = AttendancePageElement("studentpassword")
            password_field.clear()
            password_field.send_keys(password)

        time.sleep(3)

        actions = ActionChains(self.driver)
        actions.click(self.submit_button)
        actions.perform()
        return True

