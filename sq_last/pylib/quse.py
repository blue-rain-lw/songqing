import requests
payload = {
    "mobile":"admin",
    "password":"123456"
}
r = requests.post("https://testwx.baijiayun.com/api/adminUser/login",data=payload)
cookie = r.json()["data"]["remember_token"]
headers = {"authorization":f"Bearer  {cookie}"}

url = "https://testwx.baijiayun.com/api/question"
params = {
    "bank":5,
    "ques_type":"",
    "ques_stem":"",
    "creator_id":"",
    "point_id":""
}
r = requests.get(url,params=params,headers=headers).json()
print(r)
quseidlists = r["data"]["list"]


#
#
# for quseidlist in quseidlists:
#     quseid = quseidlist["id"]
#     #right = requests.get("{}/{}".format(url,quseid),headers=headers).json()
#     right = requests.get("{}/{}".format(url, 833), headers=headers).json()
#     right_answer = right["data"]["ques_type"]
#     ques_type = right["data"]["ques_type"]
#     ques_stem = right["data"]["ques_stem"]  #试题题干
#     ques_option = right["data"]["ques_option"]
#     bank_id = right["data"]["bank_id"]
#     ques_analysis = right["data"]["ques_analysis"]
#
#     payloads = {
#         "point":5,
#         "ques_type":ques_type,
#         "ques_stem":ques_stem,
#         "ques_option":ques_option,
#         "bank_id":bank_id,
#         "connection_result":[],
#         "connection_answer":[]
#     }
#
#     print(ques_stem)
#     print(ques_option)
#     putquse = requests.put("{}/{}".format(url,quseid),data=payloads,headers=headers).json()
#     print(putquse)
#


right = requests.get("{}/{}".format(url, 833), headers=headers).json()
print("试题833的信息")
print(right)
right_answer = right["data"]["ques_type"]
ques_type = right["data"]["ques_type"]
ques_stem = right["data"]["ques_stem"]
ques_option = right["data"]["ques_option"]
bank_id = right["data"]["bank_id"]
ques_analysis = right["data"]["ques_analysis"]
#更新试题，
'''
ques_analysis:试题解析
ques_stem：试题名称
ques_option：试题题干

'''
payloads = {
    "bank_id":5,
    "point":"6",
    "ques_analysis":ques_analysis,
    "ques_option":f'''{ques_option}''',
    "ques_stem":ques_stem,
    "ques_type": "2"
}
putquse = requests.put("{}/{}".format(url,833),data=payloads,headers=headers).json()

print(putquse)

# payloads1 = {
# "bank_id": "5",
# "point": "6",
# "ques_analysis": "<p>地方萨芬萨</p>",
# "ques_option": '''[{"content":"<p>范德萨发撒</p>","is_right":0},{"content":"<p>定时发</p>","is_right":1},{"content":"<p>地方萨芬</p>","is_right":1}]''',
# "ques_stem": "<p>发大水发生</p>",
# "ques_type": "2"
# }
# add = requests.post(url,data=payloads1,headers=headers).json()
# print(add)
# putquse1 = requests.put("{}/{}".format(url,851),data=payloads1,headers=headers).json()
# print(putquse1)