
# coding: utf-8

# In[67]:

from bs4 import BeautifulSoup as BeautifulSoup
#import requests
#import requests.utils as utils
import pandas as pd
import os, sys
#from urlparse import urlparse
#import re
from urllib.parse import urlparse
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

capa = DesiredCapabilities.FIREFOX
capa["pageLoadStrategy"] = "none"

#driver = webdriver.Firefox(desired_capabilities=capa)

#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
opts = Options()#executable_path='C:\Users\dwittaker\Downloads\geckodriver-v0.24.0-win64')
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs = True

#wait = WebDriverWait(driver, 10)
from pymongo import MongoClient
import time

client = MongoClient()

import datetime
#now = datetime.datetime.now()
db = client['IMOScrape']
collIMO = db['IMODetails']

#starturl = "https://www.marinetraffic.com/en/ais/index/search/all"


def getdomain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain

def openurl(imonum):
    try:
        #wait = WebDriverWait(browser, 5)
        old_url = browser.current_url
        print("launching: "+str(imonum))
        browser.get("https://www.marinetraffic.com/en/ais/index/search/all/search_type:3/keyword:"+str(imonum))
        WebDriverWait(browser, 10).until(lambda browser: old_url != browser.current_url and browser.execute_script("return document.readyState == 'complete'"))
        print("page ready")
        #myElem = WebDriverWait(browser, 80).until(EC.presence_of_element_located((By.ID, 'keyword')))
        WebDriverWait(browser,10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'keyword')))
        browser.execute_script("window.stop();")
        #wait.until(EC.presence_of_element_located((By.CLASS, 'search_vessels_input search_keyword form-control ui-autocomplete-input')))
        #wait.until(EC.presence_of_element_located((By.ID, 'keyword')))
        
    #try:
       #element = WebDriverWait(driver, 10).until(
       #     EC.presence_of_element_located((By.ID, "myDynamicElement"))
       # )
        
        #searchbox = browser.find_element_by_class_name("MuiInputBase-input MuiInput-input data-hj-whitelist")
        #searchbox.send_keys(8807349)
        #searchbox.send_keys(Keys.ENTER)
        time.sleep(5)
        srchsoup = BeautifulSoup(browser.page_source, 'lxml')
        print(imonum)
        rsltstbl = srchsoup.find("div",{"class":"col-xs-12 filters_results_table"}).find("table",{"class":"table table-hover text-left"}).tbody.find_all("tr")
        #totalset = []
        
        onerslt = {}
        for row in rsltstbl:
            cols = row.find_all("td")
            if len(cols) > 1:
                onerslt['url'] = cols[0].a['href']
                onerslt['IMOnum'] = cols[0].a.text.strip()
                onerslt['rslttype'] = cols[1].text.strip()
                onerslt['Description'] = cols[2].text.strip()
                
                
                
                urltoload = getdomain(browser.current_url) + onerslt['url']
                browser2.get(urltoload)
                myElem2 = WebDriverWait(browser2, 10).until(EC.presence_of_element_located((By.ID , 'details_wiki_accordion')))
                time.sleep(5)
                browser2.execute_script("window.stop();")
                
                infosoup = BeautifulSoup(browser2.page_source, 'lxml')
                headerblock = infosoup.find("div",{"class":"well bg-primary padding-10 radius-4 text-left"}).find("div",{"class":"table-cell text-overflow text-left collapse-768"})
                headerblock = [i for i in headerblock.stripped_strings]
                onerslt['Description'] = headerblock[0]
                onerslt['vesseltype'] = headerblock[1]
                
                infoblock = infosoup.find("div",{"class":"bg-info bg-light padding-10 radius-4 text-left"})
                infoblock = [i for i in infoblock.stripped_strings]
# =============================================================================
#                 onerslt['callsign'] = infoblock[5]
#                 onerslt['flag'] = infoblock[7]
#                 onerslt['grt'] = infoblock[11].replace(' t','')
#                 onerslt['dwt'] = infoblock[13].replace(' t','')
#                 onerslt['length'] = infoblock[15].split(' × ')[0].replace('m','')
#                 onerslt['breadth'] = infoblock[15].split(' × ')[1].replace('m','')
# =============================================================================
                for i in range(len(infoblock)):
                    if ':' in infoblock[i] and ':' in infoblock[i+1]:
                        infoblock.insert(i+1, 'N/A')
                        i = 0
                        #i=i-1
                
                for i in range(0, len(infoblock), 2):
                    #if ':' not in infoblock[i+1]:
                    onerslt['%s'%(str(infoblock[i])).replace(':','')] = infoblock[i+1]
                    #else:
                    #    i=i-1
                
                if ' × ' in onerslt['Length Overall                    x Breadth Extreme']:
                    onerslt['length'] = onerslt['Length Overall                    x Breadth Extreme'].split(' × ')[0].replace('m','')
                    onerslt['breadth'] = onerslt['Length Overall                    x Breadth Extreme'].split(' × ')[1].replace('m','')
                else:
                    onerslt['length'] = 'N/A'
                    onerslt['breadth'] = 'N/A'
                
                exnamesblock = infosoup.find("div",{"id":"vessel_details_exnames"})
                exnamesblock = [i for i in exnamesblock.stripped_strings]
                
                exvesslst = []
                exvess = {}
                vnindices = [i for i, x in enumerate(exnamesblock) if x == 'Vessel Name:']
                for i in range(len(vnindices)):
                    strt = vnindices[i]
                    end = vnindices[i+1]-1 if i < len(vnindices)-1 else len(exnamesblock)-1
                    for x in range(strt,end+1, 2):
                        #print(x)
                        exvess['%s'%(exnamesblock[x])]  = exnamesblock[x+1]
                    exvesslst.append(exvess)
                    exvess = {}
    #                for i in range(len(exnamesblock)):
    #                    if exnamesblock[i] == 'Vessel Name:':
    #                        nextind = 
    #                        exvess[exnamesblock[i]]  = exnamesblock[i+1]
    #                        exvess[exnamesblock[i+2]]  = exnamesblock[i+3]
    #                        exvess[exnamesblock[i+2]]  = exnamesblock[i+3]
    #                        #need to write a different way since the number of params are unknown
                onerslt['exvessnames'] = exvesslst
        print(onerslt)
        return onerslt
    except Exception as e:
            print("An exception occurred - ", " - ", e)  
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print("Exc found - continuing")
            
            
def runset():
    try:
        pcsdf = pd.read_csv("src/Vessels.csv", error_bad_lines=False)
        exstIMO = pullexistIMO()
        #for row in pcsdf:
        #    print(row)
        Imolist = pcsdf['LLoydNumber ']
        Imolist = [str(i).replace('.0','') for i in Imolist if str(i).lower() != 'nan']
        pagersltset = []
        cnt=0
        for imo in Imolist:
            if imo not in exstIMO:
                rslt = {}
                rslt = openurl(imo)
                if rslt != {}:
                    pagersltset.append(rslt)
                time.sleep(1)
                
                if cnt >= 3:    
                    collIMO.insert_many(pagersltset)
                    pagersltset = []        
                    cnt = 0
                cnt+=1
    except Exception as e:
            print("An exception occurred - ", " - ", e)  
#            exc_type, exc_obj, exc_tb = sys.exc_info()
#            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#            print(exc_type, fname, exc_tb.tb_lineno)
#            print("Exc found - continuing")
#
    finally:
        browser.close()
        browser.quit()
        browser2.close()
        browser2.quit()    


def pullexistIMO():
    return [i['IMOnum'] for i in collIMO.find({},{'IMOnum':1, '_id':0})]



browser = Firefox(options=opts, desired_capabilities=capa)
#browser.implicitly_wait(5)
browser2 = Firefox(options=opts, desired_capabilities=capa)
#browser2.implicitly_wait(5)


#runset()
openurl(9148805)