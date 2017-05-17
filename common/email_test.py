# -*- coding: utf-8 -*-
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import xlrd
from email import encoders


"""
可采用email模块发送电子邮件附件。发送一个未知MIME类型的文件附件其基本思路如下：

1. 构造MIMEMultipart对象做为根容器
2. 构造MIMEText对象做为邮件显示内容并附加到根容器
3. 构造MIMEBase对象做为文件附件内容并附加到根容器
　　a. 读入文件内容并格式化
　　b. 设置附件头
4. 设置根容器属性
5. 得到格式化后的完整文本
6. 用smtp发送邮件
"""


def Email(file,fname):

    server = u"smtp.163.com"
    path = "C:\Users\liaojinling\PycharmProjects\untitled1\Bindo\common\email_data.xlsx"
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    fromto = table.row(0)[0].value
    addrto = table.col(1)[0].value
    password = u'a809337633'
    msg = MIMEMultipart()
    with open(file) as fp:
        html_data = fp.read()
    msg.attach(MIMEText(u"Bindo测试报告，请查看附件",'html','utf-8'))
    mybase = MIMEBase('html','html',filename=fname)
    mybase.add_header('Content-Disposition','attachment',filename=fname)
    mybase.set_payload(html_data)
    encoders.encode_base64(mybase)
    msg.attach(mybase)
    msg['Subejct'] = Header(u'Bindo测试报告','utf-8').encode()
    smtp = smtplib.SMTP(server)
    smtp.login(fromto,password)
    smtp.sendmail(fromto,addrto,msg.as_string())
    smtp.quit()


# if __name__=="__main__":
#     Email()





