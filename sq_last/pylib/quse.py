import requests
import json
payload = {
        "mobile":"admin",
        "password":"123456"
    }
r = requests.post("https://testwx.baijiayun.com/api/adminUser/login",data=payload)
cookie = r.json()["data"]["remember_token"]
headers = {"authorization":f"Bearer  {cookie}"}
url = "https://testwx.baijiayun.com/api/question"
def quseidlist():

    params = {
        "bank":5,
        "ques_type":"",
        "ques_stem":"",
        "creator_id":"",
        "point_id":"",
        "page":3,
        "limit":40
        }
    r = requests.get(url,params=params,headers=headers).json()
    print(r)
    quseidlists = r["data"]["list"]
    return quseidlists
quseidlists = quseidlist()



for quseidlist in quseidlists:
    quseid = quseidlist["id"]
    #right = requests.get("{}/{}".format(url,quseid),headers=headers).json()
    # right = requests.get("{}/{}".format(url, 833), headers=headers).json()
    # right_answer = right["data"]["ques_type"]
    # ques_type = right["data"]["ques_type"]
    # ques_stem = right["data"]["ques_stem"]  #试题题干
    # ques_option = right["data"]["ques_option"]
    # bank_id = right["data"]["bank_id"]
    # ques_analysis = right["data"]["ques_analysis"]
    right = requests.get("{}/{}".format(url, quseid), headers=headers).json()
    right_answer = right["data"]["ques_type"]
    ques_type = right["data"]["ques_type"]
    ques_stem = right["data"]["ques_stem"]
    ques_option = right["data"]["ques_option"]
    bank_id = right["data"]["bank_id"]
    ques_analysis = right["data"]["ques_analysis"]
    newlist = []
    for option in ques_option:
        del option["id"]
        newlist.append(option)
    mewoption = json.dumps(newlist, ensure_ascii=False)

    payloads = {
        "bank_id": "5",
        "point": "6",
        "ques_analysis": ques_analysis,
        "ques_option": mewoption,
        "ques_stem": ques_stem,
        "ques_type": ques_type
    }

    putquse = requests.put("{}/{}".format(url,quseid),data=payloads,headers=headers).json()
    print(putquse)
