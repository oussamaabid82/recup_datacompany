

class CompanyView:

    def __init__(self):
        pass


    def show_start_menu(self):
        print("\n---------------* B I E N V E N U E *---------------\n")
        print("Rechercher par:")
        print("[1] - All")
        print("[2] - With Year")

        return int(input("\nSaisissez votre choix: "))


    def show_years_activity_view(self, list_years):
        print("---------------* A N N E E S *---------------\n")
        for i in list_years:
            print(f'* {i}')
        return int(input("Saisissez l'année: "))

    def error_msg(self):
        print('\n************** SAISI INCORRECT **************')
        
    def display_all_company(self, dataframe):
        dataframe.columns = [i.upper() for i in dataframe.columns ]
        dataframe['NAME'] = dataframe['NAME'].str.upper()

        liste_head = ['name', 'sector', 'siren',
                    'year', 'ca', 'margin', 'ebitda',
                    'loss'
        ]

        dataframe = dataframe[
                            list(map(str.upper, liste_head))
        ]

        html = dataframe.to_html()
        with open('data_company.html', "w") as data_html:
            data_html.write(html)
            data_html.close()

