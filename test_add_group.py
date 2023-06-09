# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_new_group(self, wd, group):
        self.open_groups_page(wd)
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page(wd)

    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/")

    def test_add_group(self):
        wd = self.wd
        self.login(wd, "admin", "secret")
        self.create_new_group(wd, Group("test", "test", "teeest"))
        self.logout(wd)

    def test_add_empy_group(self):
        wd = self.wd
        self.login(wd, "admin", "secret")
        self.create_new_group(wd, Group("", "", ""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
