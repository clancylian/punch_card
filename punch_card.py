# -*- coding: UTF-8 -*-

from selenium import webdriver
from time import sleep
from email.mime.text import MIMEText
import smtplib
import logging
import json

# 校园网用户名密码
username = '用户名'
password = '密码'

# qq邮箱
email = 'QQ邮箱'
# qq邮箱里面设置
auth = '授权码'

def sentemail(str):
    host = 'smtp.qq.com'
    port = 465
    sender = email
    # 去qq生成授权码
    pwd = auth
    receiver = email
    body = str
    msg = MIMEText(body)
    msg['subject'] = '打卡通知'
    msg['from'] = sender
    msg['to'] = receiver
    try:
        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())
        mylog.info("发送邮件成功")
    except smtplib.SMTPException:
        mylog.error("发送邮件失败")


if __name__ == '__main__':

    json_data = []
    with open('./config.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        fp.close()

    username = json_data['username']
    password = json_data['password']
    email = json_data['email']
    auth = json_data['auth']

    mylog = logging.getLogger('mylogger')
    mylog.setLevel(logging.INFO)

    # 处理器
    handler = logging.FileHandler('./logs/log_test.txt')
    handler.setLevel(logging.DEBUG)
    # 格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    mylog.addHandler(handler)

    # 不显示浏览器
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    # 通过  chrome://version/ 查看浏览器版本
    # http://chromedriver.storage.googleapis.com/index.html 下载对应版本插件
    # 解压填入路径
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=option)
    # 打卡网站
    driver.get('https://xmuxg.xmu.edu.cn/xmu/login?app=214')
    # 统一身份认证按钮
    driver.find_elements_by_class_name("primary-btn")[2].click()
    sleep(2)
    # 用户密码登录
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    # 点击登录
    driver.find_element_by_class_name("auth_login_btn").click()
    sleep(5)
    driver.find_elements_by_class_name("app_child")[1].click()
    sleep(5)
    # 跳转到新网页
    driver.switch_to.window(driver.window_handles[-1])
    # 停止一下，不然太快
    sleep(5)
    # 点击我的表单
    driver.find_elements_by_class_name("tab")[1].click()
    sleep(5)
    # 判断是否已经打卡
    text = driver.find_element_by_xpath("//div[@data-name='select_1582538939790']").text
    if('Yes' in text):
        sentemail("今日已经打卡")
        mylog.info("今日已经打卡")
    else:
        # vue和传统下拉框不一样
        driver.find_element_by_css_selector("[data-name='select_1582538939790']").click()
        sleep(3)
        driver.find_element_by_css_selector("[title='是 Yes'][class='btn-block']").click()
        # 点击保存
        driver.find_element_by_class_name("form-save").click()
        sleep(3)
        # 点击弹出框确定
        driver.switch_to.alert.accept()
        mylog.info("打卡成功")
        # 发送邮件
        sentemail("打卡成功")

    sleep(1)
    driver.close()
    exit(0)

