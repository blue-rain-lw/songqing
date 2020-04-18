*** Settings ***
Library  pylib.SchoolClassLib

*** Test Cases ***
添加班级-000001
    ${set}    add school class   1      一班     50
    should be true     $set["retcode"]==0
    #检查新添加的班级是否在列表中
    ${set1}   list school class
    ${ret}    evaluate     $set1["retlist"][0]
    should be true         $ret["name"]=="一班"
    should be true         $ret["id"]==$set["id"]

    [Teardown]   delete school class  &{ret}[id]