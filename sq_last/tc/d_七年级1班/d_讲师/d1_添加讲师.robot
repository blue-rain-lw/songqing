*** Settings ***
Library             pylib.SchoolTeacher

*** Test Cases ***
添加讲师-tc00001002
    ${addTeacher}       add school teacher    lixiaosi   李小四   2   ${suite_g7c1_classid}   17671754564
    ...     2292898465@qq.com   420320125465845698
    ${teacherId}        evaluate      $addTeacher["id"]
    should be true      $addTeacher["retcode"]==0
    #列出班级
    ${list}             list school teacher
    ${listTeacher}      evaluate    $list["retlist"]
    teacherlist shoule contain  ${listTeacher}    lixiaosi   ${suite_g7c1_classid}  李小四   ${teacherId}  17671154564
    ...     2292898465@qq.com   420320125465845698
    ${listTeacherid}    evaluate    $listTeacher[0]["id"]
    should be equal      ${listTeacherid}    ${teacherId}
    [Teardown]      delete school teacher    ${teacherId}