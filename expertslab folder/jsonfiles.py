jdata='''
{ 
   "people":[
       {
        "name":"devin",
        "phone":1234567899,
        "email":"devin@gmail.com",
        "has_license":true
       },
       {
        "name":"dainty",
        "phone":1234444444, 
        "email":null,
        "has_license":false
       }
   ] 
}
'''



import json
# data=json.loads(jdata)
# # print(data)
# for person in data['people']:
#     del person['phone']
# newjdata=json.dumps(data,indent=4,sort_keys=True)
# print(newjdata)

# with open("states.json","r") as js:
#     data =json.load(js)
#     print(data)

# import requests
# response=requests.get('http://jsonplaceholder.typicode.com/todos')
# data=json.loads(response.text)
# with open('new.json','w') as nj:
#     json.dump(data,nj,indent=2)




