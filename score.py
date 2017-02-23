#coding: utf-8
list = []
dic = {}
with open('report.txt') as f:
    for content in f:
        list = content.split()
        dic[list[0]] = list[1:]
        print dic