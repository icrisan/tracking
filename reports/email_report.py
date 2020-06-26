import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.logger_util import *
from config_util.config_manager import  get_config_property

logger = logging.getLogger(__name__)


class EmailError(object):
    pass


class EmailReport(object):
    __sender_address = None
    __sender_pass = None
    __receiver_address = None
    __email = None

    def __init__(self, mail_content):
        logger.info(
            " --------------------------------------------------------- "
            + "Starting Email report:"
            + " ----------------------------------------------------------\n"
        )
        self.__sender_address = get_config_property('Email','username')
        self.__sender_pass = get_config_property('Email','password')
        self.__receiver_address = get_config_property('Email','receiver')
        self.__configure_email(mail_content)
        self.__set_session()

    # private method
    def __configure_email(self, mail_content):
        # Setup the MIME
        self.__email = MIMEMultipart()
        self.__email['From'] = self.__sender_address
        self.__email['To'] = self.__receiver_address
        self.__email['Subject'] = 'Test report ' + str(datetime.now())

        # The body and the attachments for the mail
        with open('logs/app.log', "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {'logs/app.log'}",
            )

            self.__email.attach(part)
        self.__email.attach(MIMEText(
            mail_content
        ))

    # private method
    def __set_session(self):
        # Create SMTP session for sending the mail
        try:
            session = smtplib.SMTP('smtp.gmail.com', get_config_property('Email','port'))  # use gmail with port
            session.starttls()  # enable security
            try:
                session.login(self.__sender_address, self.__sender_pass)
            except Exception:
                raise EmailError(
                    "User not logged into server. Please check your credentials."
                )
            else:
                logger.info("User successfully logged into email server")
            text = self.__email.as_string()

            try:
                session.sendmail(self.__sender_address, self.__receiver_address, text)
            except Exception:
                raise EmailError(
                    "Email was not sent."
                )
            else:
                session.quit()
                logger.info("Email successfully sent to %s" % self.targets)
        except:
            logger.info("Email successfully sent to %s" )

                


