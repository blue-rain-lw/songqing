def f1(a,b,*teacherlist):
    print('a =', a, 'b =', b, "teacherlist=",teacherlist)
    for one in teacherlist:
        id = str(one).split(",")[0]
        name=str(one).split(",")[1]
        print(id,name)

f1(1,2,"5,name1","6,name2")