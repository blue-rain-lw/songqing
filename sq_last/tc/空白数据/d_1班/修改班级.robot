*** Settings ***
Library  pylib.SchoolClassLib

*** Test Cases ***
修改班级-000004
    ${listclass}        list school class  1
    ${classid}          evaluate    $listclass["retlist"][0]["id"]
    ${studentlimit}        evaluate    $listclass["retlist"][0]["studentlimit"]
    ${modifyclass}      modify school class    ${classid}      三班    ${studentlimit}
    should be true      $modifyclass["retcode"]==0

    #列出班级，检查一下
    ${newListClass}     list school class  1
    ${newClassName}     evaluate   $newListClass["retlist"][0]["name"]
    should be equal      ${newClassName}  三班