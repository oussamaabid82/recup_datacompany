

class CompanyView:

    def __init__(self):
        pass


    def show_start_menu(self):
        print("\n---------------* B I E N V E N U E *---------------\n")
        print("Rechercher par:")
        print("[1] - All")
        print("[2] - Results")

        return int(input("\nSaisissez votre choix: "))


    def display_all_company(self, dataframe):
        # dataframe.columns = [i.upper() for i in dataframe.columns ]
        # dataframe['NAME'] = dataframe['NAME'].str.upper()
        
        html = dataframe.to_html()
        with open('data_company.html', "w") as data_html:
            data_html.write(html)
            data_html.close()


    def display_results_company(self, dataframe):
        
        html = dataframe.to_html()
        with open('data_company.html', "w") as data_html:
            data_html.write(html)
            data_html.close()
