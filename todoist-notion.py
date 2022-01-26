# https://github.com/akarri2001/ToDoIst-to-Notion/blob/main/ToDoIst%20to%20Notion%20-%20Public.py
import todoist
import os
from dotenv import load_dotenv
load_dotenv()

TODOIST_API_KEY =  #copy and paste the api key 
TODOIST_label_id = #when you're on the website and under the specific label, you'll be able to get the id by inspect element and finding the number
NOTION_API_KEY =     #  "secret_somneklhjslkdgjsdljfg" or something like that 
database_id =  #get the mess of numbers and letters before the "?" on your dashboard URL and then split it into 8-4-4-4-12 characters between each dash



api = todoist.TodoistAPI(TODOIST_API_KEY)
api.sync()

import requests
resultList=requests.get(
    "https://api.todoist.com/rest/v1/tasks",
    params={
        "label_id": TODOIST_label_id
    },
    headers={
        "Authorization": "Bearer %s" % TODOIST_API_KEY
    }).json()


taskData = []

import os
from notion_client import Client
from pprint import pprint
from datetime import datetime

os.environ['NOTION_TOKEN'] = NOTION_API_KEY
notion = Client(auth=os.environ["NOTION_TOKEN"])

for result in resultList:
    print(result)
    print("\n")

    taskName = result['content']
    dueDate = result['due']['date']

    #Enter the task into Notion
    my_page = notion.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            "properties": {
                'Task': {
                    "type": 'title',
                    "title": [
                    {
                        "type": 'text',
                        "text": {
                        "content": taskName,
                        },
                    },
                    ],
                },
                'Date': {
                    "type": 'date',
                    'date': {
                        'start': dueDate, 
                        'end': None,
                    }
                },
                'Dashboard':  {
                    "type": 'multi_select', 
                    'multi_select': [{
                        "name": "ToDoIst"
                    }],
                },
            },
        },
    )

    #Delete the task from ToDoIst (the api stuff is defined in the first 3 lines of the program)

    item = api.items.get_by_id(result['id'])
    item.delete()
    api.commit()

    