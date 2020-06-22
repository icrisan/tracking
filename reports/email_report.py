import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror


class EmailReport(object):
    __sender_address = None
    __sender_pass = None
    __receiver_address = None
    __email = None

    def __init__(self, mail_content):
        self.__sender_address = 'grozamariaelena@gmail.com'
        self.__sender_pass = 'Test123!'
        self.__receiver_address = 'yoannacrisan@gmail.com'
        self.__configure_email(mail_content)
        self.__set_session()

    # private method
    def __configure_email(self, mail_content):
        # Setup the MIME
        self.__email = MIMEMultipart()
        self.__email['From'] = self.__sender_address
        self.__email['To'] = self.__receiver_address
        self.__email['Subject'] = 'A test mail sent by Python. It has an attachment.'  # The subject line

        # The body and the attachments for the mail
        with open('utils/app.log', "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {'app.log'}",
            )

            self.__email.attach(part)
        self.__email.attach(MIMEText(
            " Test_Run_Details: {}\n" +
            mail_content
        ))

    # private method
    def __set_session(self):
        # Create SMTP session for sending the mail
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(self.__sender_address, self.__sender_pass)  # login with mail_id and password
            text = self.__email.as_string()
            session.sendmail(self.__sender_address, self.__receiver_address, text)
            session.quit()
            print('Mail Sent')
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
