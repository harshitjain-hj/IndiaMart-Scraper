import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe";                               #PATH contains the location where the chromedriver.exe is stored
driver = webdriver.Chrome(PATH)
driver.get("https://dir.indiamart.com/chennai/fresh-vegetables-all.html")       #driver.get() => Contains the URL that needs to be scraped
try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "lay-lft"))
    )

    suppliers = content.find_elements_by_class_name("lst_cl")
    # for supplier in suppliers:
    company = [supplier.find_element_by_class_name("gcnm").text for supplier in suppliers]
    address = [supplier.find_element_by_class_name("clg").text for supplier in suppliers]
    precise_add = [supplier.find_element_by_class_name("cty-t").get_attribute("innerText") for supplier in suppliers]
    phone_no = [supplier.find_element_by_css_selector(".bo").get_attribute("innerText") for supplier in suppliers]
    items_list = []
    for supplier in suppliers:
        # items = supplier.find_elements_by_class_name("cp5")
        item = [item.find_element_by_class_name("gpnm").text for item in supplier.find_elements_by_class_name("cp5")]
        items_list.append(item)

finally:
    driver.quit()

supplier_det = pd.DataFrame({
    'Company': company,
    'Address': address,
    'Precise_add': precise_add,
    'Phone_no': phone_no,
    'Items': items_list
})

print(supplier_det)
supplier_det.to_csv("sup_det.csv")

