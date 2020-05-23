import requests
from selenium import webdriver
from config import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn
import json
class SchoolTeacher:
    URL = "http://ci.ytesting.com/api/3school/teachers"
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.find
    def list_school_teacher(self,subjectid=None):
        '''
        :param subjectid: 班级ID
        :return: 班级列表中的数据
        '''
        if subjectid == None:
            params = {
                "vcode":g_vcode,
                "action":"search_with_pagenation"
            }
        else:
            params = {
                "vcode": g_vcode,
                "action": "search_with_pagenation",
                "gradeid":int(subjectid)
            }
        response = requests.get(self.URL,params=params)
        bodyDict = response.json()
        pprint(bodyDict, indent=2)

        return bodyDict

    def add_school_teacher(self,username,realname,subjectid,classlist,
                           phonenumber,email,idcardnumber,idSaveName=None):
        timlist = str(classlist).split(",")
        newclasslist = [{"id":oneid}for oneid in timlist if oneid != '']
        payload = {
            "vcode": g_vcode,
            "action": "add",
            "username":username,
            "realname":realname,
            "subjectid":int(subjectid),
            "classlist":json.dumps(newclasslist),
            "phonenumber":phonenumber,
            "email":email,
            "idcardnumber":idcardnumber
        }
        response = requests.post(self.URL,data=payload)
        bodyDict = response.json()
        if idSaveName:
            #set_global_variable函数传两个值，全局变量的名字和值
            BuiltIn().set_global_variable("${%s}"%idSaveName,bodyDict["id"])
        pprint(bodyDict, indent=2)
        return bodyDict

    def modfiy_school_teacher(self,teacherid,realname=None,subjectid=None,classlist=None,
                           phonenumber=None,email=None,idcardnumber=None):
        payload = {
            "vcode": g_vcode,
            "action": "add"
        }
        if realname is not None:
            payload["realname"]=realname
        if subjectid is not None:
            payload["subjectid"]=subjectid
        if classlist is not None:
            payload["classlist"]=classlist
        if phonenumber is not None:
            payload["phonenumber"]=phonenumber
        if email is not None:
            payload["email"]=email
        if idcardnumber is not None:
            payload["idcardnumber"]=idcardnumber


        URL = "{}/{}".format(self.URL,teacherid)
        response = requests.put(URL, data=payload)
        bodyDict = response.json()
        pprint(bodyDict, indent=2)
        return bodyDict

    def delete_school_teacher(self,teacherid):
        payload = {
            "vcode": g_vcode
        }
        URL = "{}/{}".format(self.URL, teacherid)
        response = requests.delete(URL, data=payload)
        bodyDict = response.json()
        pprint(bodyDict, indent=2)
        return bodyDict

    def delete_all_school_teacher(self):
        rd = self.list_school_teacher()
        for one in rd["retlist"]:
            self.delete_school_teacher(one["id"])
        rd = self.list_school_teacher()
        if rd["retlist"] != []:
            raise Exception("没有删除成功")

    def teacherlist_shoule_contain(self,teacherlist,
                                     username, teacherclasslist,realname,id,
                                     phonenumber, email, idcardnumber,
                                     expectdetimes=1):
        timlist = str(teacherclasslist).split(",")
        newclasslist = [int(oneid) for oneid in timlist if oneid != '']
        item = {
        "username":username,
        "realname":realname,
        "teachclasslist":newclasslist,
        "id":id,
        "phonenumber":phonenumber,
        "email":email,
        "idcardnumber":idcardnumber
        }
        occurTimes = teacherlist.count(item)
        pprint(item)
        print("----------------------------------")
        pprint(teacherclasslist)
        if occurTimes != int(expectdetimes):
            raise Exception(f"班级列表中包含了{occurTimes}次，期望包含{expectdetimes}")
            # 如果后面的条件成立，则不抛出异常
            # assert item in classlist,"班级列表中没有该班级"
if __name__ == "__main__":
    t = SchoolTeacher()
    t.delete_all_school_teacher()