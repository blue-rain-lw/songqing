#*** Keywords ***
#定义全局变量
#suit setup action
#    ${ret}      add school class    1    1班    30
#    set global variable     ${suite_g7c1_clasid}    &{ret}[id]
*** Settings ***
Library  pylib.SchoolClassLib
Suite Setup       add school class    1     1班    30    suite_g7c1_classid
Suite Teardown    delete school class   ${suite_g7c1_classid}