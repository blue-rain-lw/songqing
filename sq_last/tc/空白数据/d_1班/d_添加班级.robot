*** Settings ***
Library  pylib.SchoolClassLib

*** Test Cases ***
添加班级-000002
    ${set}    add school class   1      二班     50
    should be true     $set["retcode"]==0

    ${set1}   list school class
    ${ret}    evaluate     $set1["retlist"]
    classlist shoule contain    ${ret}
    ...  二班    七年级      &{set}[invitecode]   50   0    &{set}[id]
    [Teardown]   delete school class  &{set}[id]


添加班级-000003
    ${listBefore}      list school class  1
    ${set}    add school class    1     1班    30
    should be true     $set["retcode"]==1
    #列出班级，检查一下
    ${set1}   list school class  1
    should be equal  ${listBefore}    ${set1}
