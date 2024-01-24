from selenium import webdriver

class InfiniteCampus():
    def __init__(self,username,password,url):
        self.url = url
        self.username = username
        self.password = password
    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()