import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page
from functions.contacts import Contacts
from utilities.excelhelper import load_data_from_excel

class TestRunner:
    td_contacts = load_data_from_excel("testdata/contacts_testdata.xls")
    # @pytest.mark.sanity
    # def test_login(self, setup):
    #     page = setup
    #     contact = Contacts(page)
    #     username = self.td_contacts["UserName"]
    #     password = self.td_contacts["Password"]
    #     contact.login(username[0], password[0])

    @pytest.mark.sanity
    @pytest.set_trace
    def test_add_contacts(self, setup):
        page = setup
        contact = Contacts(page)
        username = self.td_contacts["UserName"]
        password = self.td_contacts["Password"]
        contact.login(username[0], password[0])
        first_name = self.td_contacts["FirstName"]
        last_name = self.td_contacts["LastName"]
        email = self.td_contacts["Email"]
        job_title = self.td_contacts["JobTitle"]
        contact.fun_add_contact(first_name[0], last_name[0], email[0], job_title[0])






