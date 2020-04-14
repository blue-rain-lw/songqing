import requests
from wangxiao1.sq_last.config import g_vcode


class SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"
    def listSchoolClass(self,gradeid=None):
        '''
        :param gradeid: 班级ID
        :return: 班级列表中的数据
        '''
        if gradeid == None:
            params = {
                "vcode":g_vcode,
                "action":"list_classes_by_schoolgrade"
            }
        else:
            params = {
                "vcode": g_vcode,
                "action": "list_classes_by_schoolgrade",
                "gradeid":int(gradeid)
            }
        response = requests.get(self.URL,params=params)
        bodyDict = response.json()

        return  bodyDict

    def addSchoolClass(self,grade,name,studentlimit):
        payload = {
            "vcode": g_vcode,
            "action": "add",
            "grade":int(grade),
            "name":name,
            "studentlimit":int(studentlimit)
        }
        response = requests.post(self.URL,data=payload)
        bodyDict = response.json()
        return bodyDict

    def modfiySchoolClass(self,classid,grade,name,studentlimit):
        payload = {
            "vcode": g_vcode,
            "action": "add",
            "grade": int(grade),
            "name": name,
            "studentlimit": int(studentlimit)
        }
        URL = "{}/{}".format(self.URL,classid)
        response = requests.put(URL, data=payload)
        bodyDict = response.json()
        return bodyDict

    def deleteSchoolClass(self,classid):
        payload = {
            "vcode": g_vcode
        }
        URL = "{}/{}".format(self.URL, classid)
        response = requests.delete(URL, data=payload)
        bodyDict = response.json()
        return print(bodyDict)

    def deleteAllSchoolClass(self):
        rd = self.listSchoolClass()
        for one in rd["retlist"]:
            self.deleteSchoolClass(one["id"])
        rd = self.listSchoolClass()
        if rd["retlist"] != []:
            raise Exception("没有删除成功")


c = SchoolClassLib()
c.deleteAllSchoolClass()