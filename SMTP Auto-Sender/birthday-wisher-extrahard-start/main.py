##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import os
import random
import smtplib
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def dateMatch(dataRow, currentDate):
    if dataRow['month'] == currentDate.month and dataRow['day'] == currentDate.day:
        return True
    
    return False

#get todays date
today = dt.datetime.now()

birthday_data = pd.read_csv('SMTP Auto-Sender/birthday-wisher-extrahard-start/birthdays.csv')

for index, row in birthday_data.iterrows():
    if dateMatch(row, today):
        #send them an email
        
        #pick a letter
        letters_list = os.listdir('SMTP Auto-Sender/birthday-wisher-extrahard-start/letter_templates')
        letter = random.choice(letters_list)
        with open(f'SMTP Auto-Sender/birthday-wisher-extrahard-start/letter_templates/{letter}') as f:
            body = f.readlines()
        
        #fill in the persons name
        for i in range(len(body)):
            body[i] = body[i].replace('[NAME]', row['name'])

        email_body = ''.join(body)
        person_name = row['name']

        #send the email
        with smtplib.SMTP(os.getenv('SMTP_ADDR')) as connection:
            connection.starttls()
            connection.login(user=os.getenv('SENDER_ID'), password=os.getenv('SENDER_PWD'))
            connection.sendmail(
                from_addr=os.getenv('SENDER_ID'), 
                to_addrs=row['email'], 
                msg=f'Subject:Happy Birthday {person_name}!\n\n {email_body}')