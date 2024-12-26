import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

message = f"Subject:Revista LIDL \n\n Vezi revista la LIDL pe saptamana viitoare."
day = datetime.datetime.today()

print(day.weekday())

if day.weekday() == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        connection.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=os.getenv("RECEIVER_EMAIL"),
                            msg=message)
        print("email sent")
