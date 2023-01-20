import json
import pandas as pd

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

    def recup_activity_sectors(self):
        list_sectors = []

        for i in self.recup_json_data():
            if i['sector'] not in list_sectors:
                list_sectors.append(i['sector'])
        return list_sectors

    def create_dataframe(self):

        return pd.json_normalize(
                                self.recup_json_data(),
                                record_path=['results'],
                                meta=self.recup_head_table(),
        )

    def recup_all_data_companys(self):
        """Récuperer les donné de toutes les socciétés toutes années confondues"""
        self.view_search.convert_dataframe_to_html(self.create_dataframe())

    def recup_data_companys_with_year(self):
        """Recuperer l'annés depuis la vue pour filtrer"""
        choice_year = self.view_search.show_years_activity_view(self.recup_activity_years())

        while choice_year not in self.recup_activity_years():
            self.view_search.error_msg()
            choice_year = self.view_search.show_years_activity_view(self.recup_activity_years())

        dataframe = self.create_dataframe()

        dataframe = dataframe.loc[(dataframe['year'] == choice_year), :].reset_index()

        self.view_search.convert_dataframe_to_html(dataframe)

    def recup_data_companys_with_sector(self):
        """Recuperer le secteur depuis la vue pour filtrer"""
        choice_sector = self.view_search.show_sectors_activity_view(self.recup_activity_sectors())
        while choice_sector not in range(len(self.recup_activity_sectors())):
            self.view_search.error_msg()
            choice_sector = self.view_search.show_sectors_activity_view(self.recup_activity_sectors())

        choice_year = self.view_search.show_years_activity_view(self.recup_activity_years())

        while choice_year not in self.recup_activity_years():
            self.view_search.error_msg()
            choice_year = self.view_search.show_years_activity_view(self.recup_activity_years())

        dataframe = self.create_dataframe()

        dataframe = dataframe.loc[
            ((dataframe['sector'] == self.recup_activity_sectors()[choice_sector]) & (dataframe['year'] == choice_year)), :
        ].reset_index()

        self.view_search.convert_dataframe_to_html(dataframe)

    def result_table(self):

        dataframe = pd.json_normalize(
            self.recup_json_data(), 
            record_path = ['results'],
            meta = ['name']
        )
        dataframe_2016 = dataframe.loc[(dataframe['year'] == 2016), :]
        dataframe_2017 = dataframe.loc[(dataframe['year'] == 2017), :]

        result = pd.merge(dataframe_2016[['name','year', 'ca']], dataframe_2017[['name','year', 'ca']], on="name")
        result['Croissance CA en %'] = (result['ca_y'] - result['ca_x'])/result['ca_x']*100

        self.view_search.convert_dataframe_to_html(result)
