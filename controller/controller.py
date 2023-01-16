import json
import pandas as pd
# from pandas.io.json import json_normalize   

from view.view import CompanyView

class RecupDataAll:
    def __init__(self):
        self.view_search = CompanyView()


    def start_program(self):
        return self.view_search.show_start_menu()

  
    def recup_json_data(self):
        with open('db_json.json', "r") as file:
            return json.load(file)


    def recup_head_table(self):
        list_keys = []

        for i in self.recup_json_data():
            for j in i:
                if j not in list_keys and j != 'results':
                    list_keys.append(j)
        return list_keys


    def recup_activity_years(self):
        list_years = []

        for i in self.recup_json_data():
            for j in i['results']:
                if j['year'] not in list_years:
                    list_years.append(j['year'])
        return list_years


    def create_dataframe(self):

        return pd.json_normalize(
                                    self.recup_json_data(), 
                                    record_path=['results'],
                                    meta=self.recup_head_table(),
        )       


    def recup_all_data_companys(self):
        self.view_search.display_all_company(self.create_dataframe())


    def recup_data_companys_with_year(self):
    # Recuperer l'annés depuis la vue pour filtrer
        choice_year = self.view_search.show_years_activity_view(self.recup_activity_years()) 
        
        while choice_year not in self.recup_activity_years():
            self.view_search.error_msg()
            choice_year = self.view_search.show_years_activity_view(self.recup_activity_years())
            
        dataframe = self.create_dataframe()

        dataframe = dataframe.loc[(dataframe['year']==choice_year), :].reset_index()

        self.view_search.display_all_company(dataframe)       
