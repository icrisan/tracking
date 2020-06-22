import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror


class EmailReport(object):
    sender_address = None
    sender_pass = None
    receiver_address = None
    session = None
    message = None

    def __init__(self, mail_content):
        self.sender_address = 'grozamariaelena@gmail.com'
        self.sender_pass = 'Test123!'
        self.receiver_address = 'yoannacrisan@gmail.com'
        self.__set_body(mail_content)
        self.__set_session()

    # private method
    def __set_body(self, mail_content):
        # Setup the MIME
        self.message = MIMEMultipart()
        self.message['From'] = self.sender_address
        self.message['To'] = self.receiver_address
        self.message['Subject'] = 'A test mail sent by Python. It has an attachment.'  # The subject line

        # The body and the attachments for the mail
        self.message.attach(MIMEText(mail_content, 'plain'))

    # private method
    def __set_session(self):
        # Create SMTP session for sending the mail
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(self.sender_address, self.sender_pass)  # login with mail_id and password
            text = self.message.as_string()
            session.sendmail(self.sender_address, self.receiver_address, text)
            session.quit()
            print('Mail Sent')
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
