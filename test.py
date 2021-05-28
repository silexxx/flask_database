import requests

BASE="http://127.0.0.1:5000/"


data=[
    {"likes":10,'name':"daneshwar","views":100},
    {"likes":1,'name':"how to make rest api","views":200},
    {"likes":2,'name':"kallya","views":50},
    {"likes":3,'name':"daneshwar1","views":1},
    {"likes":4,'name':"how to make rest api2","views":2},
    {"likes":5,'name':"kallya3","views":3},
    {"likes":10,'name':"daneshwar4","views":4},
    {"likes":1000,'name':"how to make rest api5","views":5},
    {"likes":50,'name':"kallya6","views":6}
    ]

for i in range(len(data)):
    print(i)
    response =requests.put(BASE+f"video/{i}",data[i])
    print(response.json())

# response = requests.put(BASE+"video/1",{ 'name': 'daneshwar', 'views': 100, 'likes': 10})
# print(response.json())
# input()
# response = requests.delete(BASE+"video/1")
# print(response)

# input()
# response = requests.patch(BASE+"video/1",{'likes':1})
# print(response.json())

# http://127.0.0.1:5000/video/1


# response =requests.put(BASE+"video/1",{"likes":10,'name':"daneshwar","views":100})
# print(response.json())
# input()
# response = requests.get(BASE+"video/1")
# print(response.json())

# response = requests.get(BASE+"video")
# print(response.json())