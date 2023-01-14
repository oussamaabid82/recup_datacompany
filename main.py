from controller.controller import RecupDataAll


def search():
    recup_data = RecupDataAll()
    start_view = recup_data.start_program()

    if start_view == 1:
        recup_data.recup_all_company()
    
    if start_view == 2:
        recup_data.recup_results_company()
        
   