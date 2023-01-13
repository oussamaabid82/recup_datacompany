import json
from pprint import pprint

from view.view import CompanyView


class RecupDataAll:
    def __init__(self):
        self.view_search = CompanyView()

    def start_program(self):
        return self.view_search.show_start_menu()

    def search_company_name(self):

        with open('db_json.json', "r") as file:
            data = json.load(file)

        self.view_search.display_company(data)    

