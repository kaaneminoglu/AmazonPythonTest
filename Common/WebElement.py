import time

from selenium.common.exceptions import TimeoutException
from PageModel.Configs import CONFIGS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WebElement:
    def __init__(self):
        self.driver = CONFIGS["Driver"]
        self.url = CONFIGS["url"]
        self.username = CONFIGS["username"]
        self.password = CONFIGS["password"]
        self.search_key = CONFIGS["search_key"]

    def getPage(self):
        self.driver.get(self.url)
        self.driver.refresh()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-link-accountList')))
        except TimeoutException:
            print("Sayfa açılamadı.")
            self.driver.close()
            self.driver.quit()

    def signIn(self):
        self.driver.find_element_by_id("nav-link-accountList").click()
        self.driver.find_element_by_id("ap_email").send_keys(self.username)
        self.driver.find_element_by_id("continue").click()
        self.driver.find_element_by_id("ap_password").send_keys(self.password)
        self.driver.find_element_by_id("signInSubmit").click()
        time.sleep(30)

    def Search(self):
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(self.search_key)
        self.driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search"]/span[2]/h1/div/div[1]/div/div/span[1]')))
        except TimeoutException:
            print("Sonuç bulunamadı.")
            self.driver.close()
            self.driver.quit()
        self.driver.execute_script("window.scrollTo(0,6689);")
        time.sleep(3)
        self.driver.find_element_by_link_text("2").click()
        self.driver.execute_script("window.scrollTo(0,6689);")
        time.sleep(3)
        assert self.driver.find_element_by_xpath('//*[@id="search"]/span[2]/h1/div/div[1]/div/div/span[1]').text == "17-32 of over 10,000 results for", "2. Sayfa açılmadı."
        self.driver.find_element_by_xpath(
            "//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()

    def AddList(self):
        self.driver.find_element_by_id("add-to-wishlist-button-submit").click()
        time.sleep(5)
        self.driver.find_element_by_id("WLHUC_viewlist").click()
        self.driver.find_element_by_name("submit.deleteItem").click()
