# Generated by Selenium IDE
# Basic code generated using the IDE as a means to quickly find the IDs and XPaths 
# of the important objects on the page.
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
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    self.driver = webdriver.Chrome(driverpath,options=options)
    
    self.vars = {}
  
  def finalize(self):
    self.driver.quit()
  
  def test_marineTraffic(self, imoNum):
    vsldtl={} 
    vsldtl['imonum'] = imoNum
      
    # Test name: MarineTraffic
    # Direct call to the search page
    self.driver.get("https://www.marinetraffic.com/en/ais/index/search/all/search_type:3/keyword:"+str(imoNum))

    self.driver.set_window_size(1476, 824)
    self.driver.get(self.driver.find_element(By.LINK_TEXT, str(imoNum)).get_attribute('href'))

    #self.driver.execute_script("window.scrollTo(0,1062)")
    #Scrolling was not working so Page Downs used.
    html = self.driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.25)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
    #A move to element action used to focus on the section that contains the required information
    unlockelement = self.driver.find_element(By.ID, "unlockVesselInfoData") 
    action = ActionChains(self.driver) 
    action.move_to_element(unlockelement).perform() 
    
    time.sleep(0.25)

    #The results page is setup to require scrolling. Once the scrolling (or page down) works, that is no
    #no longer necessary. Additionally, it was used to get rid of the overlay but that is not necessary as the 
    #fields are accessible regardless of its presence.
    #https://intellipaat.com/community/9224/selenium-debugging-element-is-not-clickable-at-point-x-y
    if len(self.driver.find_elements(By.XPATH,"/html/body/div[2]/div[3]/div/button")) !=0 :
      overlaycheck = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/button")
      actions = ActionChains(self.driver)
      actions.move_to_element(overlaycheck).perform().click()
    
    if len(self.driver.find_elements(By.ID, "shipName")) == 0:
      overlaycheck = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/button")
      overlaycheck.click()

    #Some of the data elements required
    vsldtl['name'] = self.driver.find_element(By.ID, "shipName").text.replace('Name: ','')
    vsldtl['status'] = self.driver.find_element(By.ID, "status").text.replace('Status: ','')
    vsldtl['mmsi'] = self.driver.find_element(By.ID, "mmsi").text.replace('MMSI: ','')
    vsldtl['callsign'] = self.driver.find_element(By.ID, "callSign").text.replace('Call Sign: ','')
    vsldtl['flag'] = self.driver.find_element(By.ID, "flag").text.replace('Flag: ','')
    vsldtl['grosstonnage'] = self.driver.find_element(By.ID, "grossTonnage").text.replace('Gross Tonnage: ','')
    vsldtl['deadweight'] = self.driver.find_element(By.ID, "summerDwt").text.replace('Summer DWT: ','').replace(' t','')

    #Length and Beam data values are presented as a string. This just splits them, if existent
    lengthxbeam = self.driver.find_element(By.ID, "lengthOverallBreadthExtreme").text.split(':')
    if ' x ' in lengthxbeam[1]:
      vsldtl['length'] = lengthxbeam[1].split(' x ')[0].replace('m','').replace(' ','')
      vsldtl['beam'] = lengthxbeam[1].split(' x ')[1].replace('m','').replace(' ','')
    else:
      vsldtl['length'] = 'N/A'
      vsldtl['beam'] = 'N/A'
    
    vsldtl['yearbuilt'] = self.driver.find_element(By.ID, "yearBuild").text.replace('Year Built: ','')
    
    #Checks for tabular history of name changes and pulls into a variable as a string of 
    #concatenated values (Flag, ShipName, Last Call Date)
    self.driver.find_element(By.CSS_SELECTOR, "#Ex_Names_History-header .MuiSvgIcon-root").click()
    
    namehistory = self.driver.find_elements(By.XPATH, "//*[@id='Ex_Names_History-content']/div/table/tbody/tr")
    namelist = ''
    for x in range(len(namehistory)):
      if (len(namehistory[x].find_elements(By.XPATH, "td[1]/img")) !=0 ):
        flag = namehistory[x].find_element(By.XPATH, "td[1]/img").get_attribute("alt")
      else:
        flag = 'NA'
      name = namehistory[x].find_element(By.XPATH, "td[2]").text
      lastdate = namehistory[x].find_element(By.XPATH, "td[3]").text
      namelist = namelist + flag + '~' + name + '~' + lastdate + '|'
    
    vsldtl['oldnames'] = namelist

    return vsldtl
    
##############################################################################
### Start of script action    
print("Script started at: ", datetime.now())
#Using pandas to read in data to be checked
dataList = pd.read_csv('src/Vessel Referential Correction.csv',header=0)
#Convenience function to convert everything to string
dataList = dataList.astype(str)
#Only pull in data where the file does not have a recently checked name.
#Important since the script will need to be run multiples so it does not overrun
#the web server
#dataList = dataList[dataList['Name_New'].isnull()]

#Instantiate the Chrome Web Driver under a custom class
IMOChecker = TestMarineTraffic('IMO Check', driverpath)

#Single test for results
#vesseldetail = IMOChecker.test_marineTraffic("9085596")
#Could be used to run through via index sequence
#for index, rowList in dataList.iterrows(): 
for i in range(len(dataList)):
  try:
    #One option to run through by iterating through random indexes in the set
    #randomrow = random.randint(1,len(dataList)-1)
    #A more specific option to randomly run through the items that have still not been checked
    randomrow = random.choice(dataList[dataList['Name_New'] == 'nan'].index)
    #This checks if the record is yet to be checked successfully. No longer 
    #necessary since we use the random choice above
    if ('nan' == dataList.at[randomrow,'Name_New']):
      print("Started: " + str(i) + " for: " + dataList.at[randomrow,'LLoydNumber'])
      #Call to the Class method which opens the website and gets the details in a 
      #dictionary object. Uses the IMO # to search, which may need to be modded
      #to also search by Name and return results for multiple pages found.
      #Would need to use string similarity calculations to determine which 
      #is the most relevant one based on IMO or Name similarity
      vesseldetail = IMOChecker.test_marineTraffic(dataList.at[randomrow,'LLoydNumber'])
      #Use the returned details to update the pandas dataframe
      dataList.at[randomrow,'Name_New'] = vesseldetail['name']
      dataList.at[randomrow,'MMSI'] = vesseldetail['mmsi']
      dataList.at[randomrow,'GrossRegisterTonnage_New'] = vesseldetail['grosstonnage']
      #This data was not seen on the page
      dataList.at[randomrow,'NetRegisterTonnage_NEW'] = ''
      dataList.at[randomrow,'CallSign'] = vesseldetail['callsign']
      dataList.at[randomrow,'Flag'] = vesseldetail['flag']
      dataList.at[randomrow,'Length'] = vesseldetail['length']
      dataList.at[randomrow,'Beam'] = vesseldetail['beam']
      #This data was not seen on the page
      dataList.at[randomrow,'Draught'] = ''
      dataList.at[randomrow,'Deadweight'] = vesseldetail['deadweight']
      dataList.at[randomrow,'YearBuilt'] = vesseldetail['yearbuilt']
      dataList.at[randomrow,'OldNames'] = vesseldetail['oldnames']
      dataList.at[randomrow,'Status'] = vesseldetail['status']
      
      #Dataframe used to update the file with the provided column names. 
      #Could be possibly set to update every X runs instead of each.
      dataList.to_csv('src/Vessel Referential Correction.csv',columns=col_names, index=False)
      
      #Basic printout for manual review and sleep, so we do not overwhelm the server
      print("Completed: " + str(i) + " for: " + dataList.at[randomrow,'LLoydNumber'] + " - " + dataList.at[randomrow,'Name'] + " to " + dataList.at[randomrow,'Name_New'])
      time.sleep(2)
    else:
      print("Done already: " + str(i))
  except:
    print('Error occurred')

#Close the chrome driver object    
IMOChecker.finalize()