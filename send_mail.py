import smtplib
#import email_replace
import re
import fileinput

#letter template to be sent
letter = """
    =LOCATION=

    Attention: =TITLE=

    Having consulted with my colleagues and based on the
    information gathered from the Nigerian Chambers of Commerce
    and industry, I have the privilege to request for your
    assistance to transfer the sum of =AMOUNT=
    (=AMOUNTSPELLED=) into your accounts.
    We are now ready to transfer =AMOUNT= and that is where
    you, =SUCKER=, come in."""

def replace(first, last):
	global letter

	place = 'Lagos, Nigeria'
	title = 'The President/CEO'
	cash = '$47,500,000.00'
	cashtext = 'forty-seven million, five hundred thousand dollars'
	important_person = str(first) + ' ' + str(last)

	letter = re.sub(r"=LOCATION=", place, letter)
	letter = re.sub(r"=TITLE=", title, letter)
	letter = re.sub(r"=AMOUNT=", cash, letter)
	letter = re.sub(r"=AMOUNTSPELLED=", cashtext, letter)
	letter = re.sub(r"=SUCKER=", important_person, letter)

def send():
	global letter
	#changes the letter by substituting the field
	#replace(first_name, last_name)

	#sends the email
	source = '<from email_here>'
	destination = '<to email here>'
	subject = 'Subject: Hello World\n'

	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	type(smtpObj)
	smtpObj.ehlo()
	smtpObj.starttls()

	#login as who will be sending the email
	smtpObj.login('<email>', '<password>')

	smtpObj.sendmail(source, destination, subject + str(letter))
	# print(email_replace.main())

	smtpObj.quit()

#***IS REPLACING ONE NAME ONLY***
def main():
	for line in fileinput.input():
		fullname = re.match("([A-Z][a-z]+)\W([A-Z][a-z]+)", line)
		first_name = fullname.group(1)
		last_name = fullname.group(2)
		print(fullname)
		#replace(first_name, last_name)
		#send()
if __name__ == '__main__':
	main()