from selenium import webdriver
import pyautogui


class SeleniumTest(object):

    def __init__(self, browser):
        self.browser = browser

    def start(self):
        self.go_to_yandex_main_page()
        self.go_to_market_page()
        self.search()
        self.make_screenshot()

    def go_to_yandex_main_page(self):
        self.browser.get('http://www.yandex.ru')

    def go_to_market_page(self):
        market_button = self.browser.find_element_by_partial_link_text('Маркет')
        market_link = market_button.get_attribute('href')
        self.browser.get(market_link)

    def search(self):
        input_line = self.browser.find_element_by_id('header-search')
        input_line.send_keys('ноутбук xiaomi redmibook')

        self.browser.find_element_by_class_name('_1XiEJDPVpk').click()

        self.browser.find_element_by_class_name('_8oEFsr-0y5').click()

    def make_screenshot(self):
        pyautogui.screenshot('screenshot.jpg')


def main():
    browser = webdriver.Chrome()
    browser.maximize_window()

    start_test = SeleniumTest(browser)
    start_test.start()


if __name__ == '__main__':
    main()

