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

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time
import ssl
context = ssl._create_unverified_context()
driver = webdriver.PhantomJS()
driver.get('https://500px.com/the-maksimov')
time.sleep(3)
# https://drscdn.500px.org/photo/231909013/q%3D80_h%3D600/v2?webp=true&sig=7083101bf4199206281ef06074c629e85bf479046bed42f4cf95cf7e55128fd8
# https://drscdn.500px.org/photo/231909013/q%3D80_m%3D1500/v2?user_id=23107567&webp=true&sig=9e2569013c97657bcb3572c567c76f43b49f2ff73ece933e0a201091552d6e1f
ssl._create_default_https_context = ssl._create_unverified_context
bsObj = BeautifulSoup(driver.page_source, 'lxml')
index = 0
for a in bsObj.find_all('a', class_='photo_link '):
    # print(a)
    src = a.find('img')
    image = src['src']

    imageName = 'images/%s.jpg' % index
    urlretrieve(image, imageName)
    print(imageName, image)
    index += 1