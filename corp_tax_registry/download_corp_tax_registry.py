#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Get Corporate Tax Registration Data from Ministry of Finance
# 財政部財政資訊中心 全國營業(稅籍)登記資料集
# 	
# Keywords: 營業稅, 稅籍資料
#
# 資料集描述	
# 全國營業(稅籍)登記資料集。因考量營業稅歷年停歇業資料量太大，開啟檔案困難，故所開放檔案僅涵蓋營業中資料。 105年5月1日起檔案為壓縮檔，密碼為1234
#
# 主要欄位說明
# 營業地址、統一編號、總機構統一編號、營業人名稱、資本額(單位:元)、設立日期(民國年月日，YYYMMDD)、使用統一發票(Y/N)、行業代號、名稱。 105年5月1日起檔案為壓縮檔，密碼為1234
#
# Author: Conrad Yang
# Date: 13-Feb-2017
# Version: 1.0
# 
# Import required modules
from bs4 import BeautifulSoup
import requests, requests.models
import os,re,zipfile,contextlib
#ts=time.strftime('%Y%m%d%T%H%M%S')

# Start a new web session
s=requests.Session()
url='http://data.gov.tw/node/9400'

# Get catalog data 
r=s.get(url)

# Parse filename and URL from catalog
#soup=BeautifulSoup(r.content,"lxml")
soup=BeautifulSoup(r.content,"html.parser")
urls=[tr.find('a').get('href').rsplit('dataUrl=')[1].rsplit('&')[0] for tr in soup.findAll('td',{'class':u'views-field views-field-field-resource-url-g 壓縮檔'})]

# Check what we have to download
print urls[0]
c=s.get(urls[0])

# Write content to ZIP file
filename='corp_tax_registry.zip' 
f=open(filename,'wb')
f.write(c.content)
f.close()

# Extract ZIP file
with contextlib.closing(zipfile.ZipFile('corp_tax_registry.zip','rb')) as myzip:
    myzip.pwd='1234'
    filename = myzip.namelist()[0]
    myzip.extract(filename)

# Character replacement function to deal with Big5 unsupported characters
char_dict = {}
with open('charmap.txt') as f:
    for line in f:
        (key, value) = line.split(',')
        char_dict[key] = value.rstrip()

pattern = '|'.join(char_dict.keys())
repl_func = lambda matchobj: char_dict[matchobj.group(0)]

# Replace Big5 unsupported characters with question mark
output = open('corp_tax_registry.csv', 'w')
with open('BGMOPEN1.csv','r') as f:
    for line in f:
        text = re.sub(pattern, repl_func, line)
        output.write(text)
output.close()


