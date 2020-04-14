import requests
from config import g_vcode

class SchoolTeacher:
    URL = "http://ci.ytesting.com/api/3school/teachers"
    def listSchoolTeacher(self,subjectid=None):
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

        return  bodyDict

    def addSchoolTeacher(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber):
        payload = {
            "vcode": g_vcode,
            "action": "add",
            "username":username,
            "realname":realname,
            "subjectid":int(subjectid),
            "classlist":classlist,
            "phonenumber":phonenumber,
            "email":email,
            "idcardnumber":idcardnumber
        }
        response = requests.post(self.URL,data=payload)
        bodyDict = response.json()
        return bodyDict

    def modfiySchoolTeacher(self,teacherid,grade,name,studentlimit):
        payload = {
            "vcode": g_vcode,
            "action": "add",
            "grade": int(grade),
            "name": name,
            "studentlimit": int(studentlimit)
        }
        URL = "{}/{}".format(self.URL,teacherid)
        response = requests.put(URL, data=payload)
        bodyDict = response.json()
        return bodyDict

    def deleteSchoolTeacher(self,classid):
        payload = {
            "vcode": g_vcode
        }
        URL = "{}/{}".format(self.URL, classid)
        response = requests.delete(URL, data=payload)
        bodyDict = response.json()
        return print(bodyDict)

    def deleteAllSchoolTeacher(self):
        rd = self.listSchoolClass()
        for one in rd["retlist"]:
            self.deleteSchoolClass(one["id"])
        rd = self.listSchoolClass()
        if rd["retlist"] != []:
            raise Exception("没有删除成功")
