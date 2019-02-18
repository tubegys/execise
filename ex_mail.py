import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# sender = "tubegys@126.com"
# receiver = "tubegys@126.com"
sender = "tubepython@126.com"
receiver1 = "tubepython@126.com"
receiver2 = "Yunsheng.Guan@dellteam.com"
receivers = [receiver1, receiver2]
test = None 

def mail():
    ret = True
    try:
        msg = MIMEText(mailtext, "plain", "utf-8")
        msg['From'] = formataddr(["gys", sender])
        msg['To'] = formataddr(["gys_receiver", receiver1])
        msg['To'] = formataddr(["gys_receiver", receiver2])
        msg['Subject'] = "1121212"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login(sender, "coekie123")
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()

    except Exception:
        ret = False
    return ret

rets = mail()
if rets:
    print("success")
else:
    print("fail")