#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def search_fiction(*args,**kwargs):
    base_url = "http://www.danmeila.com"
    search_url = "http://www.danmeila.com/e/search/result/?searchid=1"
    if 'keyword' in  kwargs and len(kwargs['keyword']) > 2:
        if 'author' in kwargs:
            author = kwargs['author']
        else:
            author = ''
        key_word = kwargs['keyword']
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 20)
        browser.get(search_url)
        wait.until(EC.element_to_be_clickable((By.ID, "key")))
        key_word_input = browser.find_element_by_id("key")
        key_word_input.send_keys(key_word)
        enter_button = browser.find_element_by_id("searchBtn")
        enter_button.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\'container\']/div[5]/div/div[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td/span")))
        index = 2
        while True:
            try:
                fiction_title_location = browser.find_element_by_xpath("//*[@id=\'container\']/div[5]/div/div[2]/table/tbody/tr/td/table["+ str(index) +"]/tbody/tr[1]/td/span")
                author_location = browser.find_element_by_xpath("//*[@id=\'container\']/div[5]/div/div[2]/table/tbody/tr/td/table["+ str(index) +"]/tbody/tr[1]/td/a[1]/font")
                fiction_type_location = browser.find_element_by_xpath("//*[@id=\'container\']/div[5]/div/div[2]/table/tbody/tr/td/table["+ str(index) +"]/tbody/tr[1]/td/a[2]/font")
                if fiction_title_location:
                    # print(fiction_title_location.text)
                    # print(author_location.text)
                    # print(fiction_type_location.text)
                    # print(author)
                    fiction_title_text = fiction_title_location.text.replace(' ','')
                    author_text = author_location.text.replace(' ','')
                    fiction_type_text = fiction_type_location.text.replace(' ','')
                    if fiction_title_text == key_word and (author == '' or author_text == author):
                        link_location = browser.find_elements_by_xpath("//*[@id=\'container\']/div[5]/div/div[2]/table/tbody/tr/td/table["+ str(index) +"]/tbody/tr[1]/td/span/a")
                        link = link_location[0].get_attribute('href')
                        browser.get(link)
                        wait.until(EC.element_to_be_clickable((By.ID, "xs-text")))
                        desc_location = browser.find_element_by_id ("xs-text")
                        # print(desc_location.text)
                        desc_text = desc_location.text
                        start_to_read_location = browser.find_elements_by_xpath("//*[@id=\'colmh\']/div[1]/div[2]/div[2]/div[1]/a[1]")
                        fiction_url = start_to_read_location[0].get_attribute('href')
                        ret =  {'flag':True ,
                                'start_url': fiction_url ,
                                'title':fiction_title_text,
                                'author':author_text,
                                'fiction_type':fiction_type_text,
                                'desc':desc_text,
                                'msg':'找到资源!'}
                        break
                index += 1
            except NoSuchElementException:
                # print("ending...")
                ret = {'flag':False ,'msg':'没有找到资源'}
                break
            # except Exception as e:
            #     print("ending...")
            #     ret = {'flag':False ,'msg':'发生异常退出'}
            #     break
        browser.quit()
    else:
        ret = {'flag':False ,'msg':'缺少搜索关键字或者关键字长度少于3'}
    return ret


# print(search_fiction(keyword='宠夫守则'))
# for _ in range(10):
#     print(search_fiction(keyword='宠着你'))

