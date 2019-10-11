from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#import socket
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import wget
import os

"""
def client():#获取验证码

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('47.106.36.114',))#vps端口代理
    msg = 'need code'
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())
    client.close()
    return data.decode()

"""

"""
def baidu():#百度登录

    c.find_element_by_xpath("//div[@class='third-login-btns']/a[4]").click()
    c.find_element_by_id('TANGRAM_3__userName').send_keys('')
    sleep(1)
    c.find_element_by_id('TANGRAM_3__password').send_keys('')
    sleep(2)
    c.find_element_by_id('TANGRAM_3__submit').click()
    win = c.window_handles
    c.switch_to.window(win[-1])
    c.find_element_by_id('TANGRAM__24__button_send_mobile').click()
    time.sleep(5)
    key = client()
    c.find_element_by_id('TANGRAM__24__input_label_vcode').click()
    c.find_element_by_id('TANGRAM__24__input_vcode').send_keys(key)
    time.sleep(1)
    c.find_element_by_id('TANGRAM__24__button_submit').click()
    sleep(0.5)
"""

def mail():
    my_sender = ''  # 发件人邮箱账号
    my_pass = ''  # 发件人邮箱密码
    my_user = ''  # 收件人邮箱账号，我这边发送给自己
    ret = True
    try:
        msg =  MIMEMultipart()
        msg['From'] = formataddr(["my", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "拉勾网登录验证"  # 邮件的主题，也可以说是标题
        msg.attach(MIMEText('请扫码登录', 'plain', 'utf-8'))#邮件正文

        html = """
        <p><img src="cid:0</p>
        """
        msg.attach(MIMEText(html, 'html', 'utf-8'))

        file = open("code.jpg", "rb") #作为附件传送图片
        img_data = file.read()
        file.close()
        img = MIMEImage(img_data)
        img.add_header('Content-ID','<0>')
        msg.attach(img)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False
    return ret

def qq():#qq登录

    c.find_element_by_xpath("//div[@class='third-login-btns']/a[3]").click()
    c.switch_to_frame('ptlogin_iframe')
    time.sleep(1)
    c.find_element_by_xpath("//div[@class='bottom hide']/a[1]").click()
    c.find_element_by_id('u').send_keys('')
    time.sleep(2)
    c.find_element_by_id('p').send_keys('')
    time.sleep(2)
    c.find_element_by_id('login_button').click()
    time.sleep(3)
    if c.current_url == url:
        pass
    else:
        print('需要扫码验证')
        time.sleep(3)
        img = c.find_element_by_xpath('//div[@class="qlogin_list"]/span/img').get_attribute('src')
        name = wget.download(img,out='code.jpg')
        ret = mail()
        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
        os.remove('code.jpg')
def qiehuan():
    all = c.window_handles
    c.switch_to.window(all[-1])

c = webdriver.Chrome()
url = "https://www.lagou.com/"
c.implicitly_wait(3)
c.get(url)
try:
    c.find_element_by_link_text("北京站").click()#地区设置为北京
except:
    pass
c.find_element_by_xpath("//div[@class='lg_tbar_r']/div/a").click()
qq()
try:
    element = WebDriverWait(c, 60).until(
        EC.presence_of_element_located((By.ID, "search_input"))
    )
except Exception:
    print('验证失败')
c.find_element_by_id('search_input').send_keys('运维工程师')
time.sleep(2)
c.find_element_by_id('search_button').click()
c.find_element_by_xpath("//div[@class='details']/li[2]/a[2]").click()
c.find_element_by_xpath("//div[@class='details']/li[2]/a[3]").click()
c.find_element_by_xpath("//div[@class='details']/li[1]/a[3]").click()
c.find_element_by_xpath("//*[@id='order']/li/div[1]/a[2]").click()
c.find_element_by_xpath("//*[@id='order']/li/div[2]/div/span").click()
c.find_element_by_xpath("//*[@id='order']/li/div[2]/div/ul/li[4]/a").click()
num = len(c.find_elements_by_xpath("//div[@class='pager_container']/span"))-2#总页数
n=1
while n<=num:
    all_info = len(c.find_elements_by_xpath("//div[@id='s_position_list']/ul/li"))#当前页面职位数量
    all_li = "//*[@id='s_position_list']/ul/li"
    i=1
    print('当前第%d页,一共%d条职业信息' % (n, all_info))
    while i<=all_info:  # 遍历投递第一页招聘信息15个岗位
        no = all_li + str([i])
        biaoti = c.find_element_by_xpath(no + "/div[1]/div[1]/div[1]/a/h3").text  # 获取li中的岗位标题
        xinzi = c.find_element_by_xpath(no + "/div[1]/div[1]/div[2]/div[1]/span").text  # 获取liW中的薪资
        sleep(0.5)
        try:
            c.find_element_by_xpath(no + "/div[1]/div[1]/div[1]/a/h3").click()  # 逐个点击招聘标题
            print("职位", biaoti, xinzi)  # 打印岗位信息
        except:
            c.execute_script('window.scrollBy(0,200)')
            continue
        sleep(0.5)
        qiehuan()
        sleep(1)
        try:
            c.find_element_by_xpath("//li[@class='resume resume-attachment']/span").click()  # 附件简历
        except:
            pass
        sleep(0.5)

        if c.find_element_by_xpath("//div[@class='resume-deliver']/a").text == '已投递':# 投递简历
            print(biaoti, xinzi, '已经投递过')
            c.close()
            qiehuan()
            i +=1
            continue
        try:
            c.find_element_by_xpath("//*[@id='delayConfirmDeliver']/a").text  # 学历不符合，依然投递
            sleep(1)
            c.find_element_by_xpath("//*[@id='knowed']").click()  # 确认投递成功
            sleep(1)
        except:
            pass
        print(biaoti, xinzi, '投递成功')
        c.close()  # 关闭当前窗口
        qiehuan()  # 返回上层窗口
        i +=1
        sleep(1)
    choice = True
    while choice:
        try:
            yeshu = c.find_elements_by_xpath("//*[@id='s_position_list']/div[2]/div/span")  # 获取页数
            choice = False
        except:
            c.execute_script('window.scrollBy(0,200)')
    yeshu[-1].click()  # 点击下一页
    qiehuan()
    n += 1
    sleep(5)
c.quit()



















