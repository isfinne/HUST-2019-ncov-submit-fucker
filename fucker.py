# -*- coding: utf-8 -*-  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from random import uniform
import datetime
from config import *

reload(sys)
sys.setdefaultencoding('utf-8')

uid = m_uid
password = m_password
qq_pwd= m_qq_pwd


'''
def send_email(result):
    port = 465  # For SSL
    smtp_server = "smtp.qq.com"
    global m_sender_email,m_receiver_email
    sender_email = m_sender_email  
    receiver_email = m_receiver_email  
    global qq_pwd
    password = qq_pwd # QQ授权码

    now_time = datetime.datetime.now()
    now_time = datetime.datetime.strftime(now_time,'%m月%d天%H时%M分')
    subject = now_time+"疫情上报结果"

    message = MIMEText(result,'plain','utf-8')
    message['Subject'] = subject
    print("发送邮件")
    print(result)

    context = ssl.create_default_context()
    server=smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("发送成功!")
'''

def wait_for_element_txt(element_txt,driver):
    print('Waiting for loading:'+element_txt)
    while driver.find_elements_by_link_text(element_txt) == []:
        time.sleep(1)

def wait_for_element_class(element_class_name,driver):
    print('Waiting for loading:'+element_class_name)
    while driver.find_elements_by_class_name(element_class_name) == []:
        time.sleep(1)

# 获得正常体温
def generate_normal_body_temperature():
    t = uniform(36.5,37)
    return t

# 提交体温
def post_fuck_action(T1=36.5,T2=36.7):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)
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

    wait_for_element_txt('下一步 Next step',driver)
    #assert driver.find_element_by_id('V1_CTRL154').is_selected() # Submit for myself
    driver.find_element_by_link_text('下一步 Next step').click()

    time.sleep(2)

    wait_for_element_txt('提交 Submit',driver)
    # I will leave all info as-is.
    driver.find_element_by_id('V1_CTRL164').send_keys(str(T1)[:4])
    driver.find_element_by_id('V1_CTRL104').click()
    driver.find_element_by_id('V1_CTRL74').click()

    '''
    # family
    global family_name
    try:
        driver.find_element_by_id('V1_CTRL172_0').send_keys(family_name) # TODO 填你家人的名字
        driver.find_element_by_id('V1_CTRL174_0').send_keys(str(T2)[:4])
        driver.find_element_by_id('V1_CTRL184_0').click()
        driver.find_element_by_id('V1_CTRL186_0').click()
    except:
        pass
    '''
    driver.find_element_by_link_text('提交 Submit').click() # Fucking dynamic id

    wait_for_element_class('dialog_button',driver)
    driver.find_element_by_class_name('dialog_button').click() # first one is 'Ok', second one is 'Cancel'.

    wait_for_element_class('dialog_content',driver)
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

'''
while True:
  now_time = datetime.datetime.now()
  hour = datetime.datetime.strftime(now_time,'%H')
  if hour=='07':
      minites = uniform(0,10) # 每天早上七点到七点十分随机的时间点填报
      time.sleep(minites*60)
      t1 = generate_normal_body_temperature()
      t2= generate_normal_body_temperature()
      result_template['T1'] = t1
      result_template['T2'] = t2
      try :
          result = post_fuck_action(t1,t2)
      except :
          send_email("提交失败,快去服务器上检查一下吧,别又让辅导员罗嗦了🙄") 
          time.sleep(60*60)
      else:
          result_template['post_result'] = result
          send_email(str(result_template))
          time.sleep(21*60*60)
  else:
      print(hour)
      time.sleep(60*60)
'''
# if you want to post per day yourself
#
t1 = generate_normal_body_temperature()
t2= generate_normal_body_temperature()
result_template['T1'] = t1
result_template['T2'] = t2
result = post_fuck_action(t1,t2)
result_template['post_result'] = result
print(result_template)
