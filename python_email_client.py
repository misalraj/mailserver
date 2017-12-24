# echo "This is the body of the email" | mail -s "This is the subject line" inimitableharish@gmail.com -r misal@example.com

import os
import subprocess

class MailerClass:

    def __init__(self):
        pass 

    def send_mail_notification(from_email, to_email,
			   mail_subject=None, email_body=None):
        self.from_email = from_email 
	self.to_email = to_email 
	self.mail_subject = mail_subject 
	self.email_body = email_body
	#echo_statement = subprocess.Popen('echo', self.email_body)
	#echo_statement.Pipe()			

if __name__ == '__main__':
	mail_obj = MailerClass()
	mail_obj.send_mail_notification('inimitableharish@gmail.com',
					'mishal@gmail.com',
					'Test',
					'This is test mail from postfix')	
