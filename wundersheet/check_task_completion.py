def checkCompletion(access_token,client_id):
    import wunderpy2
    import pygsheets
    import datetime

    x = 2
    gc = pygsheets.authorize()
    sh = gc.open('wunderlist_update')
    wks = sh.sheet1
    api = wunderpy2.WunderApi()
    client = api.get_client(access_token, client_id)
    current_rows = wks.get_all_values()

    for row_data in current_rows:

        if row_data[2] == 'TRUE':
            x = x + 1
        if row_data[2] == 'FALSE':
            wunder_id = row_data[0]
            listo = client.get_task(task_id=wunder_id)

            if str(listo['completed']) == 'FALSE':
                x = x + 1
            if str(listo['completed']) == 'TRUE':
                date_now = datetime.datetime.now().date()
                wks.update_cell('C' + str(x), 'TRUE')
                wks.update_cell('E' + str(x), str(date_now))
                x = x + 1