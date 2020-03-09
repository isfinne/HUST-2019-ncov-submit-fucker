#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import smtplib, ssl
from random import uniform
import datetime
from config import *

reload(sys)
sys.setdefaultencoding('utf-8')

# TODO set your name and password in there
uid = m_uid
password = m_password
qq_pwd= m_qq_pwd

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)


def send_email(result):
    port = 465  # For SSL
    smtp_server = "smtp.qq.com"
    global m_sender_email,m_receiver_email
    sender_email = m_sender_email  # TODO there change youre sender email
    receiver_email = m_receiver_email  # TODO there change your receiver email
    global qq_pwd
    password = qq_pwd # QQ授权码
    message = """\
    Subject: 每日疫情上报结果
    
    This message is sent from Python on the linux.\n\n"""

    message += result
    
    context = ssl.create_default_context()
    server=smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

def wait_for_element_txt(element_txt):
    print('Waiting for loading: %s',element_txt)
    while driver.find_elements_by_link_text(element_txt) == []:
        time.sleep(1)

def wait_for_element_class(element_class_name):
    print('Waiting for loading: %s',element_class_name)
    while driver.find_elements_by_class_name(element_class_name) == []:
        time.sleep(1)

# 获得正常体温
def generate_normal_body_temperature():
    t = uniform(36.1,37)
    return t

# 提交体温
def post_fuck_action(T1=36.5,T2=36.7):
    url = "https://yqtb.hust.edu.cn/infoplus/form/BKS/start"
    driver.get(url)

    assert "统一身份认证系统" in driver.title

    time.sleep(2)

    elem = driver.find_element_by_id('un')
    elem.clear()
    elem.send_keys(uid)
    elem = driver.find_element_by_id('pd')
    elem.clear()
    elem.send_keys(password)
    driver.find_element_by_id('index_login_btn').click()

    time.sleep(2)

    wait_for_element_txt('下一步 Next step')
    assert driver.find_element_by_id('V1_CTRL154').is_selected() # Submit for myself
    driver.find_element_by_link_text('下一步 Next step').click()

    time.sleep(2)

    wait_for_element_txt('提交 Submit')
    # I will leave all info as-is.
    driver.find_element_by_id('V1_CTRL164').send_keys(str(T1)[:4])
    driver.find_element_by_id('V1_CTRL104').click()
    driver.find_element_by_id('V1_CTRL74').click()

    # family
    try:
        driver.find_element_by_id('V1_CTRL174_0').send_keys(str(T2)[:4])
        driver.find_element_by_id('V1_CTRL184_0').click()
        driver.find_element_by_id('V1_CTRL186_0').click()
    except:
        pass
    driver.find_element_by_link_text('提交 Submit').click() # Fucking dynamic id

    wait_for_element_class('dialog_button')
    driver.find_element_by_class_name('dialog_button').click() # first one is 'Ok', second one is 'Cancel'.

    wait_for_element_class('dialog_content')
    #while 'If you have anything to comment' in driver.find_element_by_class_name('dialog_content').text:
    #    wait_for_element_class('dialog_content')
    #while '' == driver.find_element_by_class_name('dialog_content').text:
    #    wait_for_element_class('dialog_content')
    print(driver.find_element_by_class_name('dialog_content').text)
    time.sleep(5) # magic bug, I give it up, and simply sleeps 2 second. Fix the4 code lines above if you could.
    result = driver.find_element_by_class_name('dialog_content').text
    print(result)

    driver.find_element_by_class_name('dialog_button').click() # Unnecessary.

    driver.close()
    return result


result_template = {'T1':0,'T2':0,'post_result':''}

while True:
    now_time = datetime.datetime.now()
    hour = datetime.datetime.strftime(now_time,'%H')
    if hour==7:
        minites = uniform(0,120) # 每天早上七点到九点随机的时间点填报
        time.sleep(minites*60)
        t1 = generate_normal_body_temperature()
        t2= generate_normal_body_temperature()
        result_template['T1'] = t1
        result_template['T2'] = t2
        try :
            result = post_fuck_action(t1,t2)
        except :
            send_email("提交失败,快去服务器上检查一下吧,别又让辅导员罗嗦了🙄")
            time.sleep(23*60*60)
        else:
            result_template['post_result'] = result
            send_email(str(result_template))
            time.sleep(23*60*60)
    else:
        time.sleep(60*60)

# if you want to post per day yourself

# t1 = generate_normal_body_temperature()
# t2= generate_normal_body_temperature()
# result_template['T1'] = t1
# result_template['T2'] = t2
# try :
#     result = post_fuck_action(t1,t2)
#     print(result)
# except :
#     print("Eroer")