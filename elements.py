from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    def __init__(self, locator):
        self.locator = locator


class LoginPageElement(BaseElement):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element


class ProfilePageElement(BaseElement):
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_elements_by_class_name(self.locator)
        )
        element = driver.find_elements_by_class_name(self.locator)
        return element


class CoursePageElement(BaseElement):
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements_by_class_name(self.locator)
        )
        element = driver.find_elements_by_class_name(self.locator)
        return element


class StatusPageElement(BaseElement):
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(self.driver, 30).until(
            lambda driver : driver.find_elements_by_class_name(self.locator)
        )
        element = driver.find_elements_by_class_name(self.locator)
        return element


class AttendancePageElement(BaseElement):
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(self.driver, 30).until(
            lambda driver : driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element
