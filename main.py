from selenium import webdriver
from time import sleep



brower = webdriver.Chrome('C:/Users/Hoang Nguyen/Desktop/auto/chromedriver.exe')
brower.get('https://youtube.com/')
brower.close()