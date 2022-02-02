# --------------------------------- RANDOM QUOTE --------------------------------- #

import random

with open("quotes.txt", mode="r") as quotes:
    a = quotes.readlines()
    random_quotes = random.choice(a)

# --------------------------------- DAY CHECK  --------------------------------- #

import datetime as dt

now = dt.datetime.now()
day = now.weekday()

# --------------------------------- SENDING MAIL  --------------------------------- #

import smtplib

if day == 1:
    my_mail = "*************@yahoo.com"
    password = "**********************"
    with smtplib.SMTP("smtp.mail.yahoo.com") as c:
        c.starttls()
        c.login(user=my_mail, password=password)
        c.sendmail(
            from_addr=my_mail,
            to_addrs="*********@gmail.com",
            msg=f"Subject: Hello, Have a wonderful day!\n\n{random_quotes}\n\nStay blessed!")
