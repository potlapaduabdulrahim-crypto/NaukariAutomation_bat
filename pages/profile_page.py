from selenium.webdriver.common.by import By
import time
from utils.logger import get_logger
import os
import utils.config as config
logger = get_logger(__name__)

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_View_profile(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='View profile']").click()
        time.sleep(5)
        logger.info("Clicked On View Profile...")
        self.driver.save_screenshot(
            os.path.join(
                config.screenshot_dir,
                "Navigate_to_Profile.png"
            )
        )

        # self.driver.find_element(By.XPATH, "//a[text()='View Profile']").click()
