# Run me. Pulls credentials. Runs pull data, then check task completion

def runWundersheet(access_token,client_id):
    import os

    from pull_all_data import pullData
    pullData(access_token, client_id)

    from check_task_completion import checkCompletion
    checkCompletion(access_token, client_id)

access_token = 'put access_token in'
client_id =  'put client id in'

runWundersheet(access_token,client_id)