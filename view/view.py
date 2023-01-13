import pandas as pd
# from tabulate import tabulate
# from prettytable import PrettyTable


class CompanyView:

    def __init__(self):
        pass

    def show_start_menu(self):
        print("\n---------------* B I E N V E N U E *---------------\n")
        print("Rechercher par:")
        print("[1] - All")

        return int(input("\nSaisissez votre choix: "))


    def display_company(self, data):
        dataframe = pd.DataFrame(data)
        html = dataframe.to_html() 
        with open('data_company.html', "w") as data_html:
            data_html.write(html)
            data_html.close()
