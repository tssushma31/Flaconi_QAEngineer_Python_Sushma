from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyshadow.main import Shadow

#Variables
url = "https://flaconi.de"

delay = 20
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, Nav_Parfum_sub_Menu))).click()
time.sleep(10)
driver.execute_script("""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""").click()
scroll_flag = WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//*[@alt='CHANEL COCO MADEMOISELLE Eau de Parfum']")))
driver.execute_script("arguments[0].scrollIntoView();", scroll_flag)
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'CHANEL')]")))
WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//*[@alt='CHANEL COCO MADEMOISELLE Eau de Parfum']"))).click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'EAU DE PARFUM ZERSTÄUBER')]")))
scroll_add_cart = WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//button[contains(text(),'In den Warenkorb')]")))
driver.execute_script("arguments[0].scrollIntoView();", scroll_add_cart)
WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//button[contains(text(),'In den Warenkorb')]"))).click()
time.sleep(10)
WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//a[contains(@href, '/warenkorb/')]"))).click()
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//p[.='Eau de Parfum 35 ml']")))
WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//label[text()='Gutscheincode']//following-sibling::*"))).send_keys("abc123")
WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element(By.XPATH, "//*[text()='Einlösen']"))).click()
time.sleep(10)
ActualError = WebDriverWait(driver, delay).until(EC.visibility_of(driver.find_element_by_xpath("//*[text()='Es tut uns Leid! Der Gutscheincode ist nicht verfügbar.']"))).text
ExpectedError  = "Es tut uns Leid! Der Gutscheincode ist nicht verfügbar."
if ExpectedError == ActualError:
    print(ExpectedError + "    is displayed when Gutscheincode field is entered with value abc123")


