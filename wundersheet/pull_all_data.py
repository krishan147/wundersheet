def pullData(access_token,client_id):

    import wunderpy2
    import pygsheets
    import time
    import datetime
    import os

    gc = pygsheets.authorize()
    sh = gc.open('wunderlist_update')
    wks = sh.sheet1
    date_added = datetime.datetime.now()
    date_added = datetime.datetime.strptime(str(date_added), '%Y-%m-%d %H:%M:%S.%f')
    date_added = date_added.strftime('%Y-%m-%d')
    api = wunderpy2.WunderApi()
    client = api.get_client(access_token, client_id)
    listo = client.get_tasks(170815027,completed=False)
    where_am_i = open("where_am_i.txt","r")
    x = (where_am_i.readline())
    current_ids = wks.get_col(col = 1)

    for items in listo:
        wunder_id = (items['id'])

        if str(wunder_id) in str(current_ids):
            pass
        if str(wunder_id) not in str(current_ids):
            created_at = (items['created_at'])
            created_at = datetime.datetime.strptime(created_at,'%Y-%m-%dT%H:%M:%S.%fZ')
            created_at = datetime.datetime.strftime(created_at,'%Y-%m-%d')
            completed = (items['completed'])
            title = (items['title'])
            date_added = datetime.datetime
            # Open spreadsheet and then workseet
            sh = gc.open('wunderlist_update')
            wks = sh.sheet1
            wks.update_cell('A'+str(x), wunder_id)
            wks.update_cell('B'+str(x), created_at)
            wks.update_cell('C'+str(x), completed)
            wks.update_cell('D'+str(x), title)
            wks.update_cell('E' + str(x), created_at)
            x = int(x) + 1
            time.sleep(2)

    where_am_i = open("where_am_i.txt","w")
    where_am_i.write(str(x))
    where_am_i.close()