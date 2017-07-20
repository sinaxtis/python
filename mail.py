import smtplib
import getpass






try:
    username = input('Enter Your Mail: ')
    password = getpass.getpass("Enter Your Password Here: ")
    server = smtplib.SMTP("smtp.mail.yahoo.com.ar")
    fromMy = username
    to = input('Enter Other Mail: ')
    subj = input('Enter Subject: ')
    date = '2/1/2010'
    message_text = 'Hello Or any thing you want to send'
    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (fromMy, to, subj, date, message_text)
    server.starttls()
    server.login(username,password)
    # server.sendmail(fromMy, to,msg)
    server.quit()
    print("ok the mail has sent")
except:
    print("can\'t send the Email")
