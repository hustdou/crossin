# coding: utf-8
import re
import thread
import requests
import os
def getHtml(url):
    r = requests.get(url)
    html = r.text
    return html
def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False
def saveImages(html, name):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    for imageURL in imglist:
        splitPath = imageURL.split('/')
        fileName = splitPath[-1]
        print fileName, u' 下载完成'
        dirName = name + "/" + fileName
        try:
            if "http:" in imageURL:
                rr = requests.get(imageURL)
            else:
                rr = requests.get('http:' + imageURL)
            data = rr.content
            f = open(dirName, 'wb+')
            f.write(data)
            f.close()
        except :
            continue
if __name__ == '__main__':
    num1 = input('The initial page: ')
    num2 = input('The final page: ')
    print u'开始下载'
    path = u'图片'
    mkdir(path)
    for i in range(num1,num2+1):
        html = getHtml("http://jandan.net/ooxx/page-%d#comments" % i)
        thread.start_new_thread(saveImages, (html, path))
    raw_input('press ENTER to exit...\n')