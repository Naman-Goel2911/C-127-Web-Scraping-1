from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('C:\Users\goeln\Desktop\WhiteHat Junior\Python\C127\chromedriver')
browser.get(url)
time.sleep(10)

def scraper():
    headers = ['name', 'distance', 'mass', 'radius']
    sun_data = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for table_tag in soup.find_all('table', attrs = {'class', 'wikitable sortable jquery-tablesorter'}):
        temp_list = []
        tr_tag = table_tag.find_all('tr')
        for tr_tag in tr_tag:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append('')

        sun_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open('scraper2.csv', 'w')as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(sun_data)

scraper()