import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

email_id = os.getenv('SENDER_ID')
email_password = os.getenv('SENDER_PWD')
recepient = os.getenv('TO_ID')

now = dt.datetime.now()
week_day = now.weekday()


if week_day == 0:
    with open("SMTP Auto-Sender\quotes.txt") as f:
        quotes_list = f.readlines()
        chosen_quote = random.choice(quotes_list)

    print('Sending Email')

    with smtplib.SMTP('smtp.gmail.com:587') as connection:
        connection.starttls()
        connection.login(user = email_id, password = email_password)
        connection.sendmail(from_addr=email_id, to_addrs=recepient, msg=f'Subject:Motivational Quote of the Day!\n\n{chosen_quote}')