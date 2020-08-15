#!/usr/bin/env python3

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://www.toptal.com/developers/gitignore')

driver.execute_script('''var myhistory = []
document.addEventListener("keydown", keyDownTextField, false);

function keyDownTextField(e) {
var keyCode = e.keyCode;
    myhistory.push(keyCode)
}''')

def get_history():
    return driver.execute_script('myhistory')

element = driver.find_element_by_class_name('select2-search__field')

element.send_keys('vim')
element.send_keys(Keys.ENTER)
button = driver.find_element_by_id('btn-gitignore').click()

time.sleep(1)

print('keys:', get_history())
