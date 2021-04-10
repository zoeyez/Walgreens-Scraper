import smtplib

def sendText(number, carrier, fromEmail, fromEmailPass, message):
    carriers = {
        'att': '@mms.att.net',
        'tmobile': ' @tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@pm.sprint.com'
    }

    to_number = number+'{}'.format(carriers[carrier])
    Subject = 'Subject: Covid Vaccine:\n\n'
    footer = '- Test'  # add test footer
    conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    conn.ehlo()
    conn.login(fromEmail, fromEmailPass)
    conn.sendmail(fromEmail, to_number, Subject + message)
    conn.quit()

if __name__ == "__main__":

    sendText('4083870249','sprint','zoe.yezhao@gmail.com','dyrc9km=cjS$','hai')