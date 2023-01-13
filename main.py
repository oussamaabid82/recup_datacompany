from controller.controller import RecupDataAll


def search():
    recup_data = RecupDataAll()
    start_view = recup_data.start_program()

    if start_view == 1:
        recup_data.search_company_name()
        
   