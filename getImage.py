# import urllib.request
# import ssl
# from bs4 import BeautifulSoup
#
# context = ssl._create_unverified_context()
# url = "https://500px.com/the-maksimov"
# headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"}
# request = urllib.request.Request(url, headers=headers)
# html = urllib.request.urlopen(request, context=context)
# bsObj = BeautifulSoup(html, "lxml")
# print(bsObj)
# arr = bsObj.find_all('a')
# # print(arr)
# for a in bsObj.find_all('a', class_='photo_link'):
#     print(a.find('img'))

# HTML加载完成以后可以读取的
from selenium import webdriver
from bs4 import BeautifulSoup
# 文件写入
from urllib.request import urlretrieve
# 定时器
import time
# 证书条件
import ssl
import os

# 生成驾驶
driver = webdriver.PhantomJS()
# 驾驶的URL
driver.get('https://500px.com/the-maksimov')
# 请求时间设置成3秒
time.sleep(3)
# https://drscdn.500px.org/photo/231909013/q%3D80_h%3D600/v2?webp=true&sig=7083101bf4199206281ef06074c629e85bf479046bed42f4cf95cf7e55128fd8
# https://drscdn.500px.org/photo/231909013/q%3D80_m%3D1500/v2?user_id=23107567&webp=true&sig=9e2569013c97657bcb3572c567c76f43b49f2ff73ece933e0a201091552d6e1f
# 全局证书设置
ssl._create_default_https_context = ssl._create_unverified_context
# 解析成bsobj对象
bsObj = BeautifulSoup(driver.page_source, 'lxml')
# 下标索引
index = 0
# 拿到所有的图片标签
for a in bsObj.find_all('a', class_='photo_link '):
    # print(a)
    # 得到具体的图片标签
    src = a.find('img')
    # 拿到图片URL
    imageurl = src['src']
    if not os.path.exists("images"):
        os.mkdir("images")
    # 设置图片保存的地址及名称
    imageName = 'images/%s.jpg' % index
    # 存到本地
    urlretrieve(imageurl, imageName)
    print(imageName, imageurl)
    # 索引下标累加
    index += 1