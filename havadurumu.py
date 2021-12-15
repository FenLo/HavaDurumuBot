from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
class weather:
    def __init__(driver,city):
        driver.url = "https://mgm.gov.tr/?il="
        driver.browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
        driver.city = city

    def cityWeather(driver):
        driver.browser.get(driver.url + driver.city)          
        time.sleep(2)
        info = driver.browser.find_element(By.XPATH,'//*[@id="t1"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element(By.XPATH,'//*[@id="t1"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element(By.XPATH,'//*[@id="t1"]/div/div[1]/div[5]/span[1]').text
        time.sleep(1)
        print("\n")
        print(f" gün: Bugün\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element(By.XPATH,'//*[@id="t2"]/div/div[1]/div[1]').text
        info = driver.browser.find_element(By.XPATH,'//*[@id="t2"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element(By.XPATH,'//*[@id="t2"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element(By.XPATH,'//*[@id="t2"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element(By.XPATH,'//*[@id="t3"]/div/div[1]/div[1]').text
        info = driver.browser.find_element(By.XPATH,'//*[@id="t3"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element(By.XPATH,'//*[@id="t3"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element(By.XPATH,'//*[@id="t3"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element(By.XPATH,'//*[@id="t4"]/div/div[1]/div[1]').text
        info = driver.browser.find_element(By.XPATH,'//*[@id="t4"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element(By.XPATH,'//*[@id="t4"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element(By.XPATH,'//*[@id="t4"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element(By.XPATH,'//*[@id="t5"]/div/div[1]/div[1]').text
        info = driver.browser.find_element(By.XPATH,'//*[@id="t5"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element(By.XPATH,'//*[@id="t5"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element(By.XPATH,'//*[@id="t5"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")

Weather = weather("Ankara")
Weather.cityWeather()