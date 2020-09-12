# Generated by Selenium IDE
import pytest
import time
from datetime import datetime, timedelta
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driverpath = r"bin\chromedriver_win32\chromedriver.exe"


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
    self.driver.find_element(By.LINK_TEXT, str(imoNum)).click()
# =============================================================================
#     # 11 | runScript | window.scrollTo(0,408) | 
#     self.driver.execute_script("window.scrollTo(0,408)")
#     # 12 | runScript | window.scrollTo(0,1062) | 
#     self.driver.execute_script("window.scrollTo(0,1062)")
#     # 13 | runScript | window.scrollTo(0,1295) | 
#     self.driver.execute_script("window.scrollTo(0,1295)")
#     # 14 | runScript | window.scrollTo(0,1816) | 
# =============================================================================
    self.driver.execute_script("window.scrollTo(0,1816)")
    # 15 | click | id=shipName | 
    vsldtl['name'] = self.driver.find_element(By.ID, "shipName").text
    # 16 | click | id=mmsi | 
    vsldtl['mmsi'] = self.driver.find_element(By.ID, "mmsi").text
    # 17 | click | id=callSign | 
    vsldtl['callsign'] = self.driver.find_element(By.ID, "callSign").text
    # 18 | click | id=flag | 
    vsldtl['flag'] = self.driver.find_element(By.ID, "flag").text
    # 19 | click | id=grossTonnage | 
    vsldtl['grosstonnage'] = self.driver.find_element(By.ID, "grossTonnage").text
    # 20 | click | id=summerDwt | 
    vsldtl['deadweight'] = self.driver.find_element(By.ID, "summerDwt").text
    # 21 | click | css=#lengthOverallBreadthExtreme > b | 
    self.driver.find_element(By.CSS_SELECTOR, "#lengthOverallBreadthExtreme > b").click()
    # 22 | click | id=lengthOverallBreadthExtreme | 
    self.driver.find_element(By.ID, "lengthOverallBreadthExtreme").click()
    # 23 | click | css=#yearBuild > b | 
    self.driver.find_element(By.CSS_SELECTOR, "#yearBuild > b").click()
    # 24 | click | css=#yearBuild > b | 
    self.driver.find_element(By.CSS_SELECTOR, "#yearBuild > b").click()
    # 25 | doubleClick | css=#yearBuild > b | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#yearBuild > b")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 26 | click | css=#homePort > b | 
    self.driver.find_element(By.CSS_SELECTOR, "#homePort > b").click()
    # 27 | click | css=#homePort > b | 
    self.driver.find_element(By.CSS_SELECTOR, "#homePort > b").click()
    # 28 | click | css=#homePort > b | 
    self.driver.find_element(By.CSS_SELECTOR, "#homePort > b").click()
    # 29 | doubleClick | css=#homePort > b | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#homePort > b")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 30 | click | css=#Ex_Names_History-header .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, "#Ex_Names_History-header .MuiSvgIcon-root").click()
    # 31 | click | css=.MuiTableBody-root > .MuiTableRow-root:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableBody-root > .MuiTableRow-root:nth-child(1)").click()
    # 32 | click | css=.MuiTableRow-root:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(2)").click()
    # 33 | click | css=.MuiTableRow-root:nth-child(3) > .MuiTableCell-root:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(3) > .MuiTableCell-root:nth-child(2)").click()
    # 34 | click | css=.MuiTableRow-root:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(3)").click()
    # 35 | click | css=.MuiTablePagination-actions | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTablePagination-actions").click()
    # 36 | click | css=.MuiTablePagination-actions | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTablePagination-actions").click()
  
print("Script started at: ", datetime.now())
dataList = pd.read_csv('samples/Vessel Referential Correction.csv')
IMOChecker = TestMarineTraffic('IMO Check', driverpath)

for index, rowList in dataList.iterrows(): 
  NAME_NEW, GRT_NEW, NRT_NEW = IMOChecker.test_marineTraffic(rowList.LLoydNumber)
    