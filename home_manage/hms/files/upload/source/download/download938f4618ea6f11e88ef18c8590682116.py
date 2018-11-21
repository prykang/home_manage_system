#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Blog    ：https://blog.csdn.net/countofdane

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import traceback



def download(*args,**kwargs):
    if 'path' in kwargs and kwargs['start_url'] != '':
        if 'start_url' in kwargs and kwargs['start_url'] != '':
            if 'author' in kwargs and kwargs['author'] != '':
                author = kwargs['author']
                f = open(kwargs['path_filename'], 'a+')
                f.write('作者：'+ author +'\n')
                start_url = kwargs['start_url']
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                browser = webdriver.Chrome(chrome_options=option)
                # browser = webdriver.Chrome()
                browser.get(start_url)
                while True:
                    try:
                        wait = WebDriverWait(browser, 20)
                        flag = wait.until(EC.element_to_be_clickable((By.ID, "J_article_con")))
                        print('--------------')
                        print(flag)
                        print('--------------')
                        chapter_name = browser.find_element_by_xpath('//*[@id="J_article"]/div[1]/h1').text
                        print(chapter_name)
                        f.write(chapter_name + '\n')
                        f.write('一秒记住【微信公众号 阿蒙分享】，分享各种最新最稀缺精彩资源' + '\n')
                        chapter_content = browser.find_element_by_id('J_article_con').text
                        f.write(chapter_content + '\n\n')
                        next_link = browser.find_element_by_id("next")
                        index_link = browser.find_element_by_id("book")
                        next_url = next_link.get_attribute('href')
                        index_url = index_link.get_attribute('href')
                        if next_url != index_url:
                            browser.get(next_url)
                        else:
                            ret = {'flag': True, 'msg': '下载完成'}
                            break
                    except Exception as e:
                        exstr = traceback.format_exc()
                        ret = {'flag': False, 'msg': '发生异常:'+ exstr}
                        break
                f.close()
                browser.quit()
            else:
                ret = {'flag': False, 'msg': '缺少 author'}
        else:
            ret = {'flag': False, 'msg': '缺少 start_url'}
    else:
        ret = {'flag': False, 'msg': '缺少 path'}
    return ret

# title = '宠夫守则'
# author = '月半小鱼干'
# n = 1
# url = "http://www.danmeila.com/book/20180118/1895914.html"
#
# print(download(start_url=url,title=title,author=author))
