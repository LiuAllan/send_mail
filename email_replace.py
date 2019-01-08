#!/usr/bin/python3

import re
import fileinput

def display(letter):
    print (letter)

#def replace(letter):
def replace():
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

    place = 'Lagos, Nigeria'
    title = 'The President/CEO'
    cash = '$47,500,000.00'
    cashtext = 'forty-seven million, five hundred thousand dollars'
    important_person = 'Mr. Justin Trudeau'

    letter = re.sub(r"=LOCATION=", place, letter)
    letter = re.sub(r"=TITLE=", title, letter)
    letter = re.sub(r"=AMOUNT=", cash, letter)
    letter = re.sub(r"=AMOUNTSPELLED=", cashtext, letter)
    letter = re.sub(r"=SUCKER=", important_person, letter)

    display(letter)

def main():
    #for line in fileinput.input():
        #print (line)
        #replace(line)
        replace()

if __name__ == '__main__':
    main()