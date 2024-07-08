from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop


class BasePage:
    DEFAULT_TIMEOUT = 10
    MODAL_WAIT_WINDOW = By.XPATH, "//*[@alt='loading animation']/parent::div"

    def __init__(self, web_drv):
        self.web_drv = web_drv

    @property
    def current_url(self):
        return self.web_drv.current_url

    def wait_loading(self, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.invisibility_of_element(self.MODAL_WAIT_WINDOW))

    def open_page(self, url):
        self.web_drv.get(url)
        self.wait_loading()

    def click_by_element(self, locator, timeout=DEFAULT_TIMEOUT):
        self.wait_loading()
        WDWait(self.web_drv, timeout).until(ec.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, text, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.element_to_be_clickable(locator)).send_keys(text)

    def wait_visible_element(self, locator, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.visibility_of_element_located(locator))

    def wait_invisibility_element(self, locator, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.invisibility_of_element(locator))

    def get_attribute_element(self, locator, attribute, timeout=DEFAULT_TIMEOUT):
        return WDWait(self.web_drv, timeout).until(ec.visibility_of_element_located(locator)).get_attribute(attribute)

    def get_element(self, locator):
        return self.web_drv.find_element(*locator)

    def get_visible_element(self,  locator, timeout=DEFAULT_TIMEOUT):
        return WDWait(self.web_drv, timeout).until((ec.visibility_of_element_located(locator)))

    def get_visible_elements(self, locator, timeout=DEFAULT_TIMEOUT):
        return WDWait(self.web_drv, timeout).until((ec.visibility_of_all_elements_located(locator)))

    def drag_and_drop(self, source_drag, target_drop):
        drag_and_drop(self.web_drv, source_drag, target_drop)
