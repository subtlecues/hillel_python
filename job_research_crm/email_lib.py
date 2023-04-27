import os
import smtplib, ssl, poplib, imaplib


class EmailWrapper:
    def __init__(self, login, password, user_email, smtp_server, smtp_port=465, pop_server=None, pop_port=None, imap_server=None, imap_port=None):
        self.user_email = user_email
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.pop_server = pop_server
        self.pop_port = pop_port
        self.imap_server = imap_server
        self.imap_port = imap_port



    def send_email(self, recipient, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
            server.login(self.login, self.password)
            server.sendmail(self.user_email, recipient, message)


    def get_emails(self, messages_nums, protocol='imap'):
        if protocol == 'pop3':
            return self.get_pop3(messages_nums)
        elif protocol == 'imap':
            return self.get_imap(messages_nums)
        else:
            raise ValueError('Unknown protocol')

    def get_pop3(self, messages):
        M = poplib.POP3_SSL(self.pop_server)
        M.port = self.pop_port
        M.user(self.login)
        M.pass_(self.password)
        print(M.stat())
        print(M.list())
        result = []
        for msg_num in messages:
            msg_data = M.retr(msg_num)[1]
            result.append(str(msg_data))
        M.quit()
        return result

    def get_imap(self, messages):
        M = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
        M.login(self.login, self.password)
        M.select()
        result = []
        for msg_num in messages:
            typ, data = M.fetch(msg_num, '(RFC822)')
            result.append(str(data[0][1]))
        M.close()
        M.logout()
        return result


