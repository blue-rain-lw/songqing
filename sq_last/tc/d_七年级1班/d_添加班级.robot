*** Settings ***
Library  pylib.SchoolClassLib

*** Test Cases ***
添加班级-000002
    ${set}    add school class   1      二班     50
    should be true     $set["retcode"]==0
    #列出班级，检查一下
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

修改班级-000004
    ${set}              add school class   1   2班   30
    should be true     $set["retcode"]==0
    ${classid}          evaluate    $set["id"]
    ${modifyclass}      modify school class    ${classid}      3班   30
    should be true      $modifyclass["retcode"]==0

    #列出班级，检查一下
    ${set1}   list school class
    ${retlist}    evaluate     $set1["retlist"]
    classlist shoule contain    ${retlist}
    ...  3班    七年级      &{set}[invitecode]   30   0    &{set}[id]
    [Teardown]   delete school class  ${classid}



修改班级-000005
    ${set}              add school class   1   2班   30
    should be true      $set["retcode"]==0
    ${setList}          list school class  1
    ${classid}          evaluate    $set["id"]
    ${modifyclass}      modify school class    ${classid}      1班   30
    should be true      $modifyclass["retcode"]==1

    #列出班级，检查一下
    ${retlist}          list school class  1
    should be equal      ${setList}   ${retlist}
    [Teardown]   delete school class  ${classid}



修改班级-000006
    ${modifyclass}      modify school class    111      1班   30
    should be true      $modifyclass["retcode"]==404
    should be true      $modifyclass["reason"]=="id 为`111`的班级不存在"

删除班级-000007
    ${modifyclass}      delete school class      111
    should be true      $modifyclass["retcode"]==404
    should be true      $modifyclass["reason"]=="id 为`111`的班级不存在"


删除班级-000008
#列出班级
    ${set}              list school class  1
    ${setlist}          evaluate   $set["retlist"]
#添加班级
    ${addClass}         add school class   1    2班    50    classid
    should be true      $addClass["retcode"]==0
#删除班级
    ${deleteClass}      delete school class    ${classid}
    should be true      $deleteClass["retcode"]==0
#列出班级
    ${set2}              list school class  1
    ${setlist2}          evaluate   $set2["retlist"]
    should be equal      ${setlist2}   ${setlist}


