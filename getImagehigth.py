import ssl
from selenium import webdriver
import urllib.request
import os
import time
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

url = ''
driver = webdriver.PhantomJS()
driver.get('https://500px.com/the-maksimov')
time.sleep(3)

index = 0

def getHightPicture(imageUrl):
    global index
    imageDriver = webdriver.PhantomJS()
    imageDriver.get(imageUrl)
    time.sleep(1)
    imgObj = BeautifulSoup(imageDriver.page_source, 'lxml')
    print(imageUrl)
    imageDiv = imgObj.find('div', class_='photo_container')
    # imagePhoto = imageDiv.find('image', class_='photo')
    print('*********************imageDiv=%s' % (imageDiv))
    if imageDiv is not None:
        hightImageUrl = imageDiv.find('img', class_='photo')['src']
        print(hightImageUrl)
        if not os.path.exists('highPiture'):
            os.mkdir('highPiture')
        imageFile = 'highPiture/%s.jpg' % index
        urllib.request.urlretrieve(hightImageUrl, imageFile)
        index += 1
    else:
        print('哎呦，不能读到成人图')
    # try:
    #     hightImageUrl = imgObj.find('img', class_='photo')['src']
    #     print(hightImageUrl)
    #     if not os.path.exists('highPiture'):
    #         os.mkdir('highPiture')
    #     imageFile = 'highPiture/%s.jpg' % index
    #     urllib.request.urlretrieve(hightImageUrl, imageFile)
    # except:
    #     print('哎呦，不能读到成人图')



bsObj = BeautifulSoup(driver.page_source, 'lxml')

imageUrls = []
for imageData in bsObj.find_all('a', class_='photo_link '):
    imUrl = 'https://500px.com' + imageData['href']
    imageUrls.append(imUrl)


for imageUrl in imageUrls:
    getHightPicture(imageUrl)