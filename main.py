import requests
from bs4 import BeautifulSoup
from datetime import datetime
import lxml
import smtplib
import random
from tkinter import *

my_email = "kibirigekalules@gmail.com"
app_password = "the_app_password"
response = requests.get("https://www.monitor.co.ug/uganda/magazines/people-power/museveni-s-famous-quotes-since-1980-1576292")
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
quotes = soup.select(".paragraph-wrapper p")

quote_list = [quote.getText() for quote in quotes]

day_of_week = datetime.now().weekday()

with open("Museveni-Quotes.txt", mode="w", encoding="utf-8") as file:
    for quote in quote_list:
        file.write(f"{quote}\n")

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=app_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="samuelkibirigek@gmail.com",
#         msg=f"Subject: Sampling the Sevo Quotes Program\r\n{random.choice(quote_list)}\r\r\nCompiled by,\r\nSamuel."
#     )

window = Tk()
window.title("Sevo once said...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=474)

quote_text = canvas.create_text(150, 207, text="the quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
window.mainloop()


