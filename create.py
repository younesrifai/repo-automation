import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os

def create_repo(usr, pwd, repo_name, privacy, path, description):
    driver = webdriver.Chrome()
    sleep(3)
    url = 'https://www.github.com/login'
    driver.get(url)
    driver.maximize_window()
    sleep(2)

    #Logging In
    username_box = driver.find_element(By.ID, 'login_field')
    username_box.send_keys(usr)
    sleep(1)
    
    password_box = driver.find_element(By.ID, 'password')
    password_box.send_keys(pwd)
    sleep(1)

    login_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]')
    login_box.click()

    #New Repository Form
    new_url = 'https://github.com/new'
    driver.get(new_url)

    sleep(30)

    repo_box = driver.find_element(By.ID, ':r4:')
    repo_box.send_keys(repo_name)
    sleep(5)

    desc_box = driver.find_element(By.ID, ':r5:')
    desc_box.send_keys(description)
    sleep(5)

    if privacy == 'private':
        driver.find_element(By.ID, ':r8:').click()
    else:
        pass

    sleep(2)

    create_repo_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button')
    create_repo_box.click()
    sleep(15)

    #Get SSH
    ssh_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/git-clone-help/div[1]/div/div[3]/div/form[2]/button')
    ssh_box.click()
    sleep(5)

    ssh_value = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/git-clone-help/div[1]/div/div[4]/div/span/input").get_attribute('value')
    print(ssh_value)
    sleep(5)
    #Link Local Project to Repo

    cd_command = "cd " + path

    os.system(cd_command)
    os.system(r'git init')
    os.system(r'git add -A')
    os.system(r'git commit -m "first commit"')
    os.system(r'git branch -M main')
    os.system(r'git remote add origin ' + str(ssh_value))
    os.system(r'git push -u origin main')

    sleep(30)
    
    return("Repo has been created and pushed to Github")