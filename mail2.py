import imaplib
import getpass


def mail():
    try:
        email = input("Enter your mail here: ")
        contrasena = getpass.getpass("Enter Your Password Here: ")
        mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com')
        mail.login(email, contrasena)
        mail.list()
        mail.select("INBOX")
        result, data = mail.search(None, "ALL")

        idEmails = data[0].split()[-10:]  # traigo los ultimos diez correos
        idEmails.reverse()  # se ordena los correo de mas nuevo a mas viejo
        for num in idEmails:
            typ, data = mail.fetch(num, '(RFC822)')
            m = data[0][1].split()
            print('Message %s\n%s\n' % (num, m))
    except:
        print("can\'t connect to mail server")


mail()