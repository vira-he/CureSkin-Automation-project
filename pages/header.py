from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SHOP_BY_PROD_BTN = (By.XPATH, "//span[@class='label'][normalize-space()='Shop by Product']")
    SUNSCREENS_BTN = (By.XPATH, "//span[@class='label'][normalize-space()='Sunscreens']")

    # def search_amazon(self, search_word):
    #     self.input_text(search_word, *self.SEARCH_FIELD)
    #     self.click(*self.SUBMIT_BTN)

    def click_shop_by_prod(self):
        self.click(*self.SHOP_BY_PROD_BTN)

    def click_sunscreen(self):
        self.click(*self.SUNSCREENS_BTN)
    #
    # def click_signin_popup(self):
    #     self.click(*self.POPUP_SIGNIN_BTN)
    #
    # def hover_lang(self):
    #     lang_options = self.find_element(*self.LANG_OPTIONS)
    #
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(lang_options)
    #     actions.perform()
    #
    # def verify_spanish_present(self):
    #     self.wait_for_element_appear(*self.SPANISH_LANG)
    #
    # def open_cart(self):
    #     self.click(*self.CART_BTN)
    #
    # def select_dept(self):
    #     dept_select = self.find_element(*self.DEPT_SELECT)
    #     select = Select(dept_select)
    #     select.select_by_value("search-alias=hpc")
