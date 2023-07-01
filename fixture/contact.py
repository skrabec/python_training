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

    def change_field_value(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_dropdown_value(self, dropdown_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element(By.NAME, dropdown_name).click()
            Select(wd.find_element(By.NAME, dropdown_name)).select_by_visible_text(text)

    def fill_contact_form(self, contactData):
        wd = self.app.wd
        self.change_field_value("firstname", contactData.firstname)
        self.change_field_value("middlename", contactData.middlename)
        self.change_field_value("lastname", contactData.lastname)
        self.change_field_value("nickname", contactData.nickname)
        self.change_field_value("title", contactData.title)
        self.change_field_value("company", contactData.company)
        self.change_field_value("address", contactData.address)
        self.change_field_value("home", contactData.home)
        self.change_field_value("mobile", contactData.mobile)
        self.change_field_value("work", contactData.work)
        self.change_field_value("fax", contactData.fax)
        self.change_field_value("email", contactData.email)
        self.change_field_value("email2", contactData.email2)
        self.change_field_value("email3", contactData.email3)
        self.change_field_value("homepage", contactData.homepage)
        self.change_dropdown_value("bday", contactData.bday)
        self.change_dropdown_value("bmonth", contactData.bmonth)
        self.change_field_value("byear", contactData.byear)
        self.change_dropdown_value("aday", contactData.aday)
        self.change_dropdown_value("amonth", contactData.amonth)
        self.change_field_value("ayear", contactData.ayear)
        self.change_field_value("address2", contactData.address2)
        self.change_field_value("phone2", contactData.phone2)
        self.change_field_value("notes", contactData.notes)

    def create(self, contactData):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contactData)
        # submit form
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@type='button' and @value='Delete']").click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        # open modification form
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
