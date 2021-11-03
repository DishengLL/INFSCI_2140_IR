# -*- coding: utf-8 -*-
"""crawler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PORkWPjX12VwayZ-R0C0LE_6ZXzaS7kl


"""# Integration

import json

def store_dict(dict):
    with open('/content/drive/MyDrive/2140-IR/project/data/'+'dic_course.txt','w') as f:
        jsObj = json.dumps(dict)
        f.write(jsObj)

def one_c_info(url):
  one_course = requests.get(url) # Demo网址
  one_course = one_course.text  # 抓取的数据
  soup_1course = BeautifulSoup(one_course, 'html.parser')
  info=(soup_1course.find_all("div", attrs = {"id": "main"}))
  for i in info:

    txt = i.get_text()
    txt = txt.strip()
    if len(txt.split('\n')[-1])>30:
      l = txt.split('\n')[0:-1]
      #print((l))
      txt = '\n'.join(l)
    with open('/content/drive/MyDrive/2140-IR/project/data/'+'course.txt','a+') as f:
      f.write(txt)  
      f.write('\n-------------------\n',)






from bs4 import BeautifulSoup
import requests # 抓取页面
import re
from collections import defaultdict
import os


r_course = requests.get('https://courses.sci.pitt.edu/courses#') # SCI course website
demo_course = r_course.text  # get text

soup_course = BeautifulSoup(demo_course, 'html.parser')  # parse text

def not_lacie(href):
        return href and re.compile("courses/view").search(href)

# return list containing all of course in website
l_course = soup_course.find_all('a',href=not_lacie)

# form a dictionary contain course field, name, link
# dict{field:{name: link}}
d = defaultdict(dict)
for i in l_course:
  field  = i.get_text().split()[0]
  course_name = ' '.join(i.get_text().split()[1:len(i.get_text().split())])
  d[field][course_name] ='https://courses.sci.pitt.edu/'+i.get('href')

store_dict(d)



os.remove(r'/content/drive/MyDrive/2140-IR/project/data/course.txt')
for i in d:
  #print(i)
  for j in d[i].values():
    print(j) #print each course link 
    one_c_info(j)

