import pandas
from datetime import *
from random import *
import smtplib
MAIL = "your_mail"
PASSWORD = "your_password"
today = (datetime.now().month,datetime.now().day)

data = pandas.read_csv("./birthdays.csv")
birthday_dict = {(data_row.month,data_row.day):data_row  for (index,data_row) in data.iterrows()}
if today in birthday_dict:
    birth_day = birthday_dict[today]
    file = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(file) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birth_day["name"])
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MAIL,password=PASSWORD)
        connection.sendmail(from_addr=MAIL,to_addrs=birth_day["email"],
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{contents}")

    
