#!/usr/bin/env python
# coding: utf-8

# In[135]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


# # BU_001: Register

# In[124]:


driver = webdriver.Chrome('./chromedriver')
driver.get("http://127.0.0.1:8000/register")
driver.maximize_window()


# In[87]:


driver.find_element_by_id("name").send_keys("bejo")
driver.find_element_by_id("email").send_keys("bejohanroro@gmail.com")
driver.find_element_by_id("password").send_keys("bhhq1A5Z")
driver.find_element_by_id("password_confirmation").send_keys("bhhq1A5Z")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


# In[88]:


# User Diet
age = driver.find_element_by_id("age")
age.send_keys('20')
age.clear()
driver.find_element_by_id("gender-1").click()
driver.find_element_by_id("weight").send_keys("70")
driver.find_element_by_id("height").send_keys("175")
driver.find_element_by_id("age").send_keys("20")
driver.find_element_by_id("activity-2").click()
driver.find_element_by_id("goal-3").click()
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


# In[89]:


driver.quit()


# # BU_002: Login

# In[125]:


driver = webdriver.Chrome('./chromedriver')
driver.get("http://127.0.0.1:8000/login")
driver.maximize_window()


# In[126]:


driver.find_element_by_id("email").send_keys("bejohanroro@gmail.com")
driver.find_element_by_id("password").send_keys("bhhq1A5Z")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


# # BU_003: Menambah Makanan

# In[95]:


today_foods_link = driver.find_element(By.XPATH, '//a[contains(text(), "Today Foods")]')
today_foods_link.click()


# In[96]:


add_food_link = driver.find_element(By.XPATH, '//a[contains(text(), "Add")]')
add_food_link.click()


# In[98]:


tanggal = driver.find_element_by_id('datepicker')
tanggal.clear()
tanggal_baru = '09-06-2023'
tanggal.send_keys(tanggal_baru)
makanan = driver.find_element_by_id("name")
makanan.clear()
makanan.send_keys("Fried Rice")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


# In[99]:


home = driver.find_element(By.XPATH, '//a[contains(text(), "Home")]')
home.click()


# # BU_004: Like Makanan

# In[101]:


fried_rice = driver.find_element_by_xpath('//h1[text()="Fried Rice"]')
fried_rice.click()


# In[104]:


like = driver.find_element_by_xpath('//a[contains(@href, "/like/1")]')
like.click()


# In[110]:


home = driver.find_element(By.XPATH, '//a[contains(text(), "Home")]')
home.click()


# # BU_005: Search Makanan

# In[127]:


search_bar = driver.find_element_by_id('default-search')
search_bar.clear()
search_bar.send_keys('Fried Rice')
search_query = search_bar.get_attribute('value')


# In[128]:


search_food = driver.find_element_by_xpath('//form[@action="/dashboard/search"]')
search_food.submit()


# In[129]:


home = driver.find_element(By.XPATH, '//a[contains(text(), "Home")]')
home.click()


# # BU_006: Edit User Diet

# In[130]:


User_Diets = driver.find_element(By.XPATH, '//a[contains(text(), "User Diets")]')
User_Diets.click()


# In[131]:


edit = driver.find_element_by_xpath('//a[@href="/user-diets/edit"]')
edit.click()


# In[132]:


age = driver.find_element_by_id("age")
weight = driver.find_element_by_id("weight")
height = driver.find_element_by_id("height")
age.clear()
weight.clear()
height.clear()
age.send_keys('25')
driver.find_element_by_id("gender-2").click()
driver.find_element_by_id("weight").send_keys("65")
driver.find_element_by_id("height").send_keys("180")
driver.find_element_by_id("activity-1").click()
driver.find_element_by_id("goal-1").click()
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


# In[133]:


home = driver.find_element(By.XPATH, '//a[contains(text(), "Home")]')
home.click()


# # Hasil Report Testing

# In[143]:


status = [
    {'No': '#1', 'Nama Fitur': 'Registrasi', 'Test Case': 'BU_001', 'Status': 'Passed'},
    {'No': '#2', 'Nama Fitur': 'Login', 'Test Case': 'BU_002', 'Status': 'Passed'},
    {'No': '#3', 'Nama Fitur': 'Menambah Makanan', 'Test Case': 'BU_003', 'Status': 'Passed'},
    {'No': '#4', 'Nama Fitur': 'Like Makanan', 'Test Case': 'BU_004', 'Status': 'Passed'},
    {'No': '#5', 'Nama Fitur': 'Search Makanan', 'Test Case': 'BU_005', 'Status': 'Passed'},
    {'No': '#6', 'Nama Fitur': 'Edit User Diet', 'Test Case': 'BU_006', 'Status': 'Failed'}
]
df = pd.DataFrame(status)
df.to_excel('Test_Report_Kelompok 9.xlsx', index=False)

