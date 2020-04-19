import requests
from config import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn

class  SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode

    def modify_school_class(self,classid,name,studentlimit):
        payload = {
            'vcode': self.vcode,
            'action': 'modify',
            'name': name,
            'studentlimit': int(studentlimit),
        }

        response = requests.put("{}/{}".format(self.URL,classid), data=payload)
        bodyDict = response.json()
        pprint(bodyDict, indent=2)
        return bodyDict

    def delete_school_class(self,classid):
        payload = {
            'vcode': self.vcode,
        }

        url = '{}/{}'.format(self.URL,classid)
        response = requests.delete(url,data=payload)
        print(response.json())
        return response.json()


    def list_school_class(self,gradeid=None):
        if gradeid != None:
            params = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        else:
            params = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade'
            }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict


    def add_school_class(self,gradeid,name,studentlimit,idSaveName=None):
        '''
        :param studentlimit: 班级的最大人数
        :param idSaveName: 保存classid的名字
        '''
        payload = {
            'vcode'  : self.vcode,
            'action' : 'add',
            'grade'  : int(gradeid),
            'name'   : name,
            'studentlimit'  : int(studentlimit),
        }
        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        if idSaveName:
            #set_global_variable函数传两个值，全局变量的名字和值
            BuiltIn().set_global_variable("${%s}"%idSaveName,bodyDict["id"])

        return bodyDict

    def delete_all_school_classes(self):
        # 先列出所有班级
        rd =  self.list_school_class()
        pprint(rd, indent=2)

        # 删除列出的所有班级
        for one in rd['retlist']:
            self.delete_school_class(one['id'])

        #再列出七年级所有班级
        rd =  self.list_school_class(1)
        pprint (rd,indent=2)

        # 如果没有删除干净，通过异常报错给RF
        # 参考http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#reporting-keyword-status
        if rd['retlist'] != []:
            raise  Exception("班级没有删除干净")

    def classlist_shoule_contain(self,
                                 classlist,
                                 classname,
                                 gradename,
                                 invitecode,
                                 studentlimit,
                                 studentnumber,
                                 classid,
                                 expectdetimes=1):
        item = {
            "name":classname,
            "grade__name":gradename,
            "invitecode":invitecode,
            "studentnumber":int(studentnumber),
            "studentlimit":int(studentlimit),
            "id":classid,
            "teacherlist":[]
        }
        occurTimes = classlist.count(item)
        pprint(item)
        print("----------------------------------")
        pprint(classlist)
        if occurTimes != int(expectdetimes):
            raise Exception(f"班级列表中包含了{occurTimes}次，期望包含{expectdetimes}")
        #如果后面的条件成立，则不抛出异常
        # assert item in classlist,"班级列表中没有该班级"

if __name__ == '__main__':
    scm = SchoolClassLib()
    #ret = scm.list_school_class(1)
    #scm.delete_all_school_classes()
    scm.list_school_class()

