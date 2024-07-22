import pytest


class Contacts:

    def __init__(self, page):
        self.username = page.locator("//input[@id='username']")
        self.password = page.locator("//input[@id='password']")
        self.login_button = page.locator("//button[@type='submit']")
        self.my_account = page.locator("//div[@data-testid='my-accounts-container']//img")
        self.add_contact = page.locator("//span[text()='Add contact']")
        self.first_name = page.locator("//input[contains(@name,'firstName')]")
        self.last_name = page.locator("//input[contains(@name,'lastName')]")
        self.email = page.locator("//input[@type='email']")
        self.job_title = page.locator("//input[contains(@name,'jobTitle')]")
        self.save_button = page.locator("//button[@type='submits']")

    def login(self, userid, passwd):
        self.username.fill(userid)
        self.username.press("Tab")
        self.password.fill(passwd)
        self.login_button.click()

    def fun_add_contact(self, first_name, last_name, email, job_title):
        self.my_account.click()
        self.add_contact.click()
        self.email.fill(email)
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.job_title.fill(job_title)
        self.save_button.click()
