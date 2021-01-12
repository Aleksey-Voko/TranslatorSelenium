import random
from time import sleep

import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from definitions import ROOT_DIR


def translate(f_name):
    with webdriver.Chrome(ROOT_DIR / 'drivers/chromedriver') as driver:
        driver.get(f_name.as_uri())
        driver.maximize_window()

        html_code_in = driver.page_source
        soup_in = BeautifulSoup(html_code_in, 'html.parser')
        pre_in_tags = soup_in.find_all('pre')
        table_in_tags = soup_in.find_all('table')
        dt_in_tags = soup_in.find_all('dt')

        doc_height = driver.execute_script('return document.body.scrollHeight')
        scroll_count = int(doc_height / (driver.get_window_size()['height'] * 0.76)) + 1

        try:
            h1_element = driver.find_element_by_tag_name('h1')
            anchor = h1_element
        except NoSuchElementException:
            anchor = driver.find_element_by_css_selector('body')

        action_chains = ActionChains(driver)
        action_chains.move_to_element(anchor).perform()
        action_chains.context_click().perform()

        sleep(0.2)
        for _ in range(3):
            pyautogui.press('up')
        pyautogui.press('enter')

        sleep(5)
        body = driver.find_element_by_css_selector('body')
        for _ in range(scroll_count):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(0.8)

        html_code_out = driver.page_source
        soup_out = BeautifulSoup(html_code_out, 'html.parser')
        pre_out_tags = soup_out.find_all('pre')
        table_out_tags = soup_out.find_all('table')
        dt_out_tags = soup_out.find_all('dt')

        for pre_in_tag, pre_out_tag in zip(pre_in_tags, pre_out_tags):
            pre_out_tag.replace_with(pre_in_tag)

        for table_in_tag, table_out_tag in zip(table_in_tags, table_out_tags):
            table_out_tag.replace_with(table_in_tag)

        for dt_in_tag, dt_out_tag in zip(dt_in_tags, dt_out_tags):
            dt_out_tag.replace_with(dt_in_tag)

        html_code_out = str(soup_out)

        sleep(random.randint(10, 30))
        return html_code_out
