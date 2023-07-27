from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    POPUP_BTN = (By.CSS_SELECTOR, ".popup-close")
    HAM_BTN = (By.CSS_SELECTOR, ".icon.icon-hamburger")

    def open_main_page(self):
        self.open_url("https://shop.cureskin.com/")
        # self.wait_for_element_appear(*self.POPUP_BTN).click()
        self.wait_for_element_click(*self.POPUP_BTN)

    def open_ham_menu(self):
        self.wait_for_element_click(*self.HAM_BTN)