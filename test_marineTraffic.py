# Generated by Selenium IDE
import pytest
import time
from datetime import datetime, timedelta
import json
import pandas as pd
import random
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driverpath = r"bin\chromedriver_win32\chromedriver.exe"
col_names = [
'Name'
,'LLoydNumber'
,'GrossRegisterTonnage'
,'NetRegisterTonnage'
,'Latest VOS'
,'Latest ETA'
,'Name_New'
,'MMSI'
,'GrossRegisterTonnage_New'
,'NetRegisterTonnage_NEW'
,'CallSign'
,'Flag'
,'Length'
,'Beam'
,'Draught'
,'Deadweight'
,'YearBuilt'
,'OldNames'
,'Status'
]


class TestMarineTraffic():
  def __init__(self, fixname, driverpath):
    self.name = fixname
    self.driver = webdriver.Chrome(driverpath)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_marineTraffic(self, imoNum):
    vsldtl={} 
    vsldtl['imonum'] = imoNum
      
    # Test name: MarineTraffic
    # Step # | name | target | value
    # 1 | open | https://www.marinetraffic.com/en/ais/home/centerx:-12.0/centery:24.8/zoom:4 | 
    self.driver.get("https://www.marinetraffic.com/en/ais/index/search/all/search_type:3/keyword:"+str(imoNum))
    # 2 | setWindowSize | 1476x824 | 
    self.driver.set_window_size(1476, 824)
    # 3 | click | css=.MuiInputBase-input | 
# =============================================================================
#     self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").click()
#     # 4 | runScript | window.scrollTo(0,0) | 
#     self.driver.execute_script("window.scrollTo(0,0)")
#     # 5 | runScript | window.scrollTo(0,0) | 
#     self.driver.execute_script("window.scrollTo(0,0)")
#     # 6 | type | css=.MuiInputBase-input | 9357121
#     self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys("9357121")
#     # 7 | sendKeys | css=.MuiInputBase-input | ${KEY_ENTER}
#     self.driver.find_element(By.CSS_SELECTOR, ".MuiInputBase-input").send_keys(Keys.ENTER)
#     # 8 | mouseOver | linkText=Result type | 
#     element = self.driver.find_element(By.LINK_TEXT, "Result type")
#     actions = ActionChains(self.driver)
#     actions.move_to_element(element).perform()
#     # 9 | mouseOver | linkText=Result | 
#     element = self.driver.find_element(By.LINK_TEXT, "Result")
#     actions = ActionChains(self.driver)
#     actions.move_to_element(element).perform()
# =============================================================================
    # 10 | click | linkText=9357121 | 
    #self.driver.find_element(By.LINK_TEXT, str(imoNum)).click()
    self.driver.get(self.driver.find_element(By.LINK_TEXT, str(imoNum)).get_attribute('href'))
# =============================================================================
#    # 11 | runScript | window.scrollTo(0,408) | 
    #self.driver.execute_script("window.scrollTo(0,408)")
#     # 12 | runScript | window.scrollTo(0,1062) | 
    #self.driver.execute_script("window.scrollTo(0,1062)")
#     # 13 | runScript | window.scrollTo(0,1295) | 
    html = self.driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    #html.send_keys(Keys.END)
    #time.sleep(0.5)
    unlockelement = self.driver.find_element(By.ID, "unlockVesselInfoData") 
    action = ActionChains(self.driver) 
    action.move_to_element(unlockelement).perform() 
    #self.driver.execute_script("window.scrollTo(0,3000)")
    
    time.sleep(0.25)
#     # 14 | runScript | window.scrollTo(0,1816) | 
    #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'shipName')))
# =============================================================================
    #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 15 | click | id=shipName | 
    
    #https://intellipaat.com/community/9224/selenium-debugging-element-is-not-clickable-at-point-x-y
    if len(self.driver.find_elements(By.XPATH,"/html/body/div[2]/div[3]/div/button")) !=0 :
      overlaycheck = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/button")
#    if (overlaycheck):
      actions = ActionChains(self.driver)
      #actions.move_to_element(element).perform()
      actions.move_to_element(overlaycheck).perform().click()
    
    if len(self.driver.find_elements(By.ID, "shipName")) == 0:
      overlaycheck = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/button")
      overlaycheck.click()
#    if (overlaycheck):
      #actions = ActionChains(self.driver)
      #actions.move_to_element(element).perform()
      #actions.move_to_element(overlaycheck).perform().click()
    vsldtl['name'] = self.driver.find_element(By.ID, "shipName").text.replace('Name: ','')
    
    vsldtl['status'] = self.driver.find_element(By.ID, "status").text.replace('Status: ','')
    # 16 | click | id=mmsi | 
    vsldtl['mmsi'] = self.driver.find_element(By.ID, "mmsi").text.replace('MMSI: ','')
    # 17 | click | id=callSign | 
    vsldtl['callsign'] = self.driver.find_element(By.ID, "callSign").text.replace('Call Sign: ','')
    # 18 | click | id=flag | 
    vsldtl['flag'] = self.driver.find_element(By.ID, "flag").text.replace('Flag: ','')
    # 19 | click | id=grossTonnage | 
    vsldtl['grosstonnage'] = self.driver.find_element(By.ID, "grossTonnage").text.replace('Gross Tonnage: ','')
    # 20 | click | id=summerDwt | 
    vsldtl['deadweight'] = self.driver.find_element(By.ID, "summerDwt").text.replace('Summer DWT: ','').replace(' t','')
# =============================================================================
#     vsldtl['draught'] = ''
#     searchstring = 'current draught is reported to be'
#     summarysec = self.driver.find_element(By.XPATH, "//*[@id='vesselDetails_summarySection']/div[2]/div/div/div/div[6]/div")
#     if searchstring in summarysec:
#       position = summarysec.find(searchstring)
#       vsldtl['draught'] = summarysec[position+len(searchstring):position+len(searchstring)+12]
# =============================================================================
    # 22 | click | id=lengthOverallBreadthExtreme | 
    lengthxbeam = self.driver.find_element(By.ID, "lengthOverallBreadthExtreme").text.split(':')
    if ' x ' in lengthxbeam[1]:
      vsldtl['length'] = lengthxbeam[1].split(' x ')[0].replace('m','').replace(' ','')
      vsldtl['beam'] = lengthxbeam[1].split(' x ')[1].replace('m','').replace(' ','')
    else:
      vsldtl['length'] = 'N/A'
      vsldtl['beam'] = 'N/A'
    
    vsldtl['yearbuilt'] = self.driver.find_element(By.ID, "yearBuild").text.replace('Year Built: ','')
    
# =============================================================================
#     # 23 | click | css=#yearBuild > b | 
#     self.driver.find_element(By.CSS_SELECTOR, "#yearBuild > b").click()
#     # 24 | click | css=#yearBuild > b | 
#     self.driver.find_element(By.CSS_SELECTOR, "#yearBuild > b").click()
#     # 25 | doubleClick | css=#yearBuild > b | 
#     element = self.driver.find_element(By.CSS_SELECTOR, "#yearBuild > b")
#     actions = ActionChains(self.driver)
#     actions.double_click(element).perform()
#     # 26 | click | css=#homePort > b | 
#     self.driver.find_element(By.CSS_SELECTOR, "#homePort > b").click()
#     # 27 | click | css=#homePort > b | 
#     self.driver.find_element(By.CSS_SELECTOR, "#homePort > b").click()
#     # 28 | click | css=#homePort > b | 
#     self.driver.find_element(By.CSS_SELECTOR, "#homePort > b").click()
#     # 29 | doubleClick | css=#homePort > b | 
#     element = self.driver.find_element(By.CSS_SELECTOR, "#homePort > b")
#     actions = ActionChains(self.driver)
#     actions.double_click(element).perform()
# =============================================================================
    # 30 | click | css=#Ex_Names_History-header .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, "#Ex_Names_History-header .MuiSvgIcon-root").click()
    # 31 | click | css=.MuiTableBody-root > .MuiTableRow-root:nth-child(1) | 
    namehistory = self.driver.find_elements(By.XPATH, "//*[@id='Ex_Names_History-content']/div/table/tbody/tr")
    namelist = ''
    for x in range(len(namehistory)):
      flag = namehistory[x].find_element(By.XPATH, "td[1]/img").get_attribute("alt")
      name = namehistory[x].find_element(By.XPATH, "td[2]").text
      lastdate = namehistory[x].find_element(By.XPATH, "td[3]").text
      namelist = namelist + flag + '~' + name + '~' + lastdate + '|'
      #print(namehistory.find_elements(By.XPATH, ""))
    vsldtl['oldnames'] = namelist
    #self.driver.find_element(By.CSS_SELECTOR, ".MuiTableBody-root > .MuiTableRow-root:nth-child(1)").click()
    # 32 | click | css=.MuiTableRow-root:nth-child(2) | 
    #self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(2)").click()
    # 33 | click | css=.MuiTableRow-root:nth-child(3) > .MuiTableCell-root:nth-child(2) | 
    #self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(3) > .MuiTableCell-root:nth-child(2)").click()
    # 34 | click | css=.MuiTableRow-root:nth-child(3) | 
    #self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(3)").click()
    # 35 | click | css=.MuiTablePagination-actions | 
    #self.driver.find_element(By.CSS_SELECTOR, ".MuiTablePagination-actions").click()
    # 36 | click | css=.MuiTablePagination-actions | 
    #self.driver.find_element(By.CSS_SELECTOR, ".MuiTablePagination-actions").click()
    return vsldtl
    
    
    
    
    
print("Script started at: ", datetime.now())
dataList = pd.read_csv('src/Vessel Referential Correction.csv',header=0)
dataList = dataList.astype(str)
#dataList = dataList[dataList['Name_New'].isnull()]
IMOChecker = TestMarineTraffic('IMO Check', driverpath)

#vesseldetail = IMOChecker.test_marineTraffic("9198305")
#for index, rowList in dataList.iterrows(): 
for i in range(len(dataList)):
  randomrow = random.randint(1,len(dataList)-1)
  if ('nan' == dataList.at[randomrow,'Name_New']):
    vesseldetail = IMOChecker.test_marineTraffic(dataList.at[randomrow,'LLoydNumber'])
    dataList.at[randomrow,'Name_New'] = vesseldetail['name']
    dataList.at[randomrow,'MMSI'] = vesseldetail['mmsi']
    dataList.at[randomrow,'GrossRegisterTonnage_New'] = vesseldetail['grosstonnage']
    dataList.at[randomrow,'NetRegisterTonnage_NEW'] = ''
    dataList.at[randomrow,'CallSign'] = vesseldetail['callsign']
    dataList.at[randomrow,'Flag'] = vesseldetail['flag']
    dataList.at[randomrow,'Length'] = vesseldetail['length']
    dataList.at[randomrow,'Beam'] = vesseldetail['beam']
    dataList.at[randomrow,'Draught'] = ''
    dataList.at[randomrow,'Deadweight'] = vesseldetail['deadweight']
    dataList.at[randomrow,'YearBuilt'] = vesseldetail['yearbuilt']
    dataList.at[randomrow,'OldNames'] = vesseldetail['oldnames']
    dataList.at[randomrow,'Status'] = vesseldetail['status']
    
    dataList.to_csv('src/Vessel Referential Correction.csv',columns=col_names, index=False)
    
    print("Completed: " + str(i))