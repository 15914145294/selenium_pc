# encoding:utf-8


"""
@version: python27
@author: fafa
@software: PyCharm Community Edition
@file: send_email.py
@time: 2016/12/10 0010 下午 3:08
"""

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(report):
    smtp_server = u'smtp.163.com'
    from_addr = u'xx.com'
    passwd = u'xx123456'
    to_addr = u'xx@qq.com'
    to_addr1 = u'1946528031@qq.com'

    # 构造邮件对象
    msg = MIMEMultipart()
    msg["From"] = _format_addr(u"自动化测试<%s>" % from_addr)
    msg["To"] = _format_addr(u"我%s" % to_addr)
    msg["Subject"] = Header(u"测试报告，请查收", 'utf-8').encode()
    # 邮件正文
    y = MIMEText(u"附件是测试报告，请查收", "plain", "utf - 8")
    msg.attach(y)

    with open(report, 'rb') as f:
        # 设置文件的mine和类型
        mime = MIMEBase("report", "HTML", filename=report)
        # 添加头信息
        mime.add_header("Content-Disposition", "attachment", filename=report)
        mime.add_header("Content-ID", "<0>")
        mime.add_header("X-Attachment-Id", "0")
        # 加载附件
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, passwd)
    server.set_debuglevel(1)
    server.sendmail(from_addr, [to_addr, to_addr1], msg.as_string())
    server.quit()
    print "send ok"


if __name__ == '__main__':
    send_email()
