

class CompanyView:

    def __init__(self):
        pass

    def show_start_menu(self):
        print("\n---------------* W E L C O M E *---------------\n")
        print("SHEARCH WITH:")
        print("[1] - All")
        print("[2] - Year")
        print("[3] - Sector")
        return int(input("\nEnter your choice: "))

    def show_years_activity_view(self, list_years):
        print("---------------* Y E A R S *---------------\n")
        for i in list_years:
            print(f'* {i}')
        return int(input("CHOOSE THE YEAR: "))

    def show_sectors_activity_view(self, list_sectors):
        print("---------------* S E C T O R S *---------------\n")
        for i, j in zip(list_sectors, range(len(list_sectors))):
            print(f'{j} - {i}')
        return int(input("CHOOSE THE SECTOR NUMBER: "))

    def error_msg(self):
        print('\n************** INCORRECTLY ENTERED **************')

    def display_dataframe(self, dataframe):
        dataframe.columns = [i.upper() for i in dataframe.columns]
        dataframe['NAME'] = dataframe['NAME'].str.upper()
        liste_head = [
                    'name', 'sector', 'siren',
                    'year', 'ca', 'margin', 'ebitda',
                    'loss'
        ]
        dataframe = dataframe[
                            list(map(str.upper, liste_head))
        ]
        return dataframe

    def convert_dataframe_to_html(self, dataframe):
        html = self.display_dataframe(dataframe).to_html()
        with open('data_company.html', "w") as data_html:
            data_html.write(html)
            data_html.close()
