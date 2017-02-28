#coding: utf-8
from __future__ import division
list1= []
with open('report.txt','r') as f:
    for content in f:
        list = content.split()
        list.append(sum([float(i) for i in list[1:]]))
        ave = "%.1f" % (list[-1]/(len(list)-2))
        list.append(ave)
        list1.append(list)
    list1.sort(key=lambda student: student[10],reverse = True)
    list1.insert(0, ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分'])
    list3 = ['0','平均']
    list2 = []
    for i in range(1,len(list1[1])):
        for j in range(1,len(list1)):
            list2.append(list1[j][i])
            sum1 = sum([float(m) for m in list2[:]]) / (len(list2))
            sum1= "%.1f" % (sum1)
        list3.append(sum1)
        del list2[:]
    list1.insert(1,list3)
    j = 1
    for i in list1[2:]:
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