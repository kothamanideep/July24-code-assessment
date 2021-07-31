import json
import requests
try:
 data=requests.get("https://jsonplaceholder.typicode.com/todos")
 ED=data.json()
 #print(ED)
 # li=[]
 # for i in ED:
 #     if i["completed"]==True:
 #         li.append(i)
 # print(li)
 lis=[x for x in ED if x["completed"]==True]
 print(lis)
except:
    print("something went wrong")
finally:
    print("work done")