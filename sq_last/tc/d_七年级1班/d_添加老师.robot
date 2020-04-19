*** Settings ***
Library     pylib.SchoolTeacher
Library     pylib.SchoolClassLib


*** Test Cases ***
添加讲师-tc001001
    ${addTeacher}       add school teacher    zhangsanf   张三丰   1   ${suite_g7c1_classid}   17671154564
    ...     2292898465@qq.com   420320125465845698
    ${teacherId}        evaluate      $addTeacher["id"]
    should be true      $addTeacher["retcode"]==0

    #列出班级
    ${list}             list school teacher
    ${listTeacher}      evaluate    $list["retlist"]
    teacherlist shoule contain  ${listTeacher}    zhangsanf   ${suite_g7c1_classid}  张三丰   ${teacherId}  17671154564
    ...     2292898465@qq.com   420320125465845698
    ${listTeacherid}    evaluate    $listTeacher[0]["id"]
    should be equal      ${listTeacherid}    ${teacherId}
    [Teardown]      delete school teacher    ${teacherId}

