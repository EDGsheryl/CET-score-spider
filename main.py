#coding=gbk
import requests
from bs4 import BeautifulSoup
import re

def mod1(zkz,name):
    url = "http://www.chsi.com.cn/cet/query?zkzh=" + zkz + "&xm=" + name
    f = open(zkz+'.txt', 'w')
    data={}
    headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
               'Referer':'http://www.chsi.com.cn/cet/',
               'x-forwarded-for':'127.0.0.1'
               }
    response = requests.post(url,data=data,headers=headers)
    soup = BeautifulSoup(response.text)
    for x in soup.findAll("td"):
        ret = x.string
        if (ret!=None):
            f.write(ret)
    f.close()
    f2 = open(zkz + '.txt', 'r')
    fnew = open('out.txt', 'a+')
    str2 = f2.readlines()
    strout = ''
    for kk in str2 :
        kk = ''.join(kk.split(' '))
        kk = ''.join(kk.split('\t'))
        kk = ''.join(kk.split('\n'))
        kk = ''.join(kk.split('-'))
        if (kk!=""):
            strout = strout+" "+kk
    fnew.write(strout)
    fnew.write("\n");
    fnew.close()
    f2.close()

md = open('mingdan.txt', 'r')
for stringmd in md.readlines():
    str= stringmd.split('\t')
    mod1(zkz=str[1],name=str[0])
