*** Settings ***
Library             pylib.SchoolTeacher
Suite Setup         add school teacher    zhangsanf   张三丰   1   ${suite_g7c1_classid}   17671154564
                ...     2292898465@qq.com   420320125465845698   suite_g7c1_teacherid
Suite Teardown      delete school teacher       ${suite_g7c1_teacherid}