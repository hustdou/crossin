#coding: utf-8
from __future__ import division
list1= []
with open('report.txt','r') as f:
    for content in f:
        list = content.split()
        list.append(sum([int(i) for i in list[1:]]))
        list.append(list[-1]/(len(list)-1))
        list1.append(list)
    list1.sort(key=lambda student: student[10],reverse = True)
    list1.insert(0, [0,'姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])
    j = 1
    for i in list1[1:]:
        i.insert(0,j)
        j += 1
        for ii in i[2:-2]:
            if int(ii) < 60:
                i[i.index(ii)] = '不及格'
        f = open('newreport.txt', 'w')
    for newcontent in list1:
        for i in range(0, len(newcontent)):
            newcontent[i] = str(newcontent[i])
        str_convert = ' '.join(newcontent)+'\n'
        f.write(str_convert)
    f.close()