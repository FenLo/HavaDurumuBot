from selenium import webdriver
import time 

class weather:
    def __init__(driver,city):
        driver.url = "https://mgm.gov.tr/?il="
        driver.browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
        driver.city = city
        driver.browser.set_window_position(0, 0)
        driver.browser.set_window_size(0,0)

    def cityWeather(driver):
        driver.browser.get(driver.url + driver.city)          
        time.sleep(2)
        info = driver.browser.find_element_by_xpath('//*[@id="t1"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element_by_xpath('//*[@id="t1"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element_by_xpath('//*[@id="t1"]/div/div[1]/div[5]/span[1]').text
        time.sleep(1)
        print("\n")
        print(f" gün: Bugün\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element_by_xpath('//*[@id="t2"]/div/div[1]/div[1]').text
        info = driver.browser.find_element_by_xpath('//*[@id="t2"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element_by_xpath('//*[@id="t2"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element_by_xpath('//*[@id="t2"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element_by_xpath('//*[@id="t3"]/div/div[1]/div[1]').text
        info = driver.browser.find_element_by_xpath('//*[@id="t3"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element_by_xpath('//*[@id="t3"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element_by_xpath('//*[@id="t3"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element_by_xpath('//*[@id="t4"]/div/div[1]/div[1]').text
        info = driver.browser.find_element_by_xpath('//*[@id="t4"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element_by_xpath('//*[@id="t4"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element_by_xpath('//*[@id="t4"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")
        day = driver.browser.find_element_by_xpath('//*[@id="t5"]/div/div[1]/div[1]').text
        info = driver.browser.find_element_by_xpath('//*[@id="t5"]/div/div[1]/div[3]').text
        celciusMin = driver.browser.find_element_by_xpath('//*[@id="t5"]/div/div[1]/div[4]/span[1]').text
        celciusMax = driver.browser.find_element_by_xpath('//*[@id="t5"]/div/div[1]/div[5]/span[1]').text
        print("\n")
        print(f" gün: {day}\n hava durumu: {info}\n minimum hava sıcaklığı: {celciusMin}\n maximum hava sıcaklığı: {celciusMax}")

Weather = weather("Ankara")
Weather.cityWeather()