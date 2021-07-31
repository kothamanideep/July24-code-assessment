import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    edata=data.json()
    emptylist=[]
    true=[i for i in edata if i["completed"]==True]
    emptylist.append(true)
    print(emptylist)

except:
    print("Please check the link if it is not correct")