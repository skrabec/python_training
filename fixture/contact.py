from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        # fill contact form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)
        # submit form
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@type='button' and @value='Delete']").click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//*[@title='Edit']").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)
        wd.find_element(By.XPATH, "//input[@type='submit' and @value='Update']").click()
        self.return_to_home_page()