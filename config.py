# -*- coding: utf-8 -*-  
""" 
family_name: 你的同居住的家人的名字,由于只填一个就行了,我这里只写了一个,两个以上去源码增加
m_uid: 学号,类似U201714***
m_password: hust认证密码
m_qq_pwd: QQ授权码
m_sender_email: 发送的QQ邮箱
m_receiver_email: 接受邮件的邮箱
"""
import os

family_name = "" 

m_uid = os.environ.get('UID')
m_password = os.environ.get('PASSWD')
push_key = os.environ.get('PUSH_KEY')
m_qq_pwd = "" # # QQ授权码

m_sender_email = "" # 发送的QQ邮箱
m_receiver_email = "" # 接受邮件的邮箱
