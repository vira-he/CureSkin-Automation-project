from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchResult(Page):
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".grid__item .card-wrapper")
    PRODUCT_HEADER = (By.XPATH, "//h1[@class='h2' and contains(text(), 'Sunscreen')]")

    def open_first_prod(self):
        self.driver.wait.until(EC.url_contains('https://shop.cureskin.com/collections/sun-protection'))
        self.click(*self.FIRST_PRODUCT)

    def verify_search_result(self):
        self.driver.wait.until(EC.url_contains('https://shop.cureskin.com/collections/sun-protection'))
        # self.verify_element_text("SPF30 Sunscreen", *self.PRODUCT_HEADER)
        actual_result = self.driver.find_element(*self.PRODUCT_HEADER).text
        assert "Sunscreen" in actual_result, \
            f'Error! Expected "Sunscreen" in {actual_result} '
