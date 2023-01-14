import json
import pandas as pd
from pandas.io.json import json_normalize   

from view.view import CompanyView


class RecupDataAll:
    def __init__(self):
        self.view_search = CompanyView()


    def start_program(self):
        return self.view_search.show_start_menu()


    def recup_all_company(self):

        list_keys = []

        with open('db_json.json', "r") as file:
            data = json.load(file)

        for i in data:
                for j in i:
                    if j not in list_keys:
                        list_keys.append(j)
        del list_keys[3]

        dataframe = pd.json_normalize(data, 
                                      record_path=['results'],
                                      meta=list_keys,
                                      )
        self.view_search.display_all_company(dataframe)


    def recup_results_company(self):
        liste = []
        with open('db_json.json', "r") as file:
            data = json.load(file)

        for i in data:
            # for j in i['results']:
                liste.append(i['results'])

        dataframe = pd.json_normalize(liste)

        self.view_search.display_results_company(dataframe)       
