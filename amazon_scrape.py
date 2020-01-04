import requests
from bs4 import BeautifulSoup as bs
from decimal import Decimal
import smtplib

URL= 'https://www.amazon.in/Lenovo-Legion-Graphics-Windows-81SY00CKIN/dp/B07W6H9YM9/ref=sr_1_3?keywords=y540&qid=1578141911&sr=8-3'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

target_price = Decimal(input("Target Price: "))
page = requests.get(URL, headers=headers)
soup = bs(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
ref_price = Decimal(price[2:].replace(",",""))

def check_price():
    if(ref_price <= target_price):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    mail_id = 'ramvignesh.codes@gmail.com'
    app_pass = 'whvpktonrsznfnxz'
    recipient = 'ramvigneshgreat@gmail.com'
    server.login(mail_id, app_pass)

    subject = 'Price is slashed ^_^'
    body = 'The price of the product ' + title.strip() + 'has been reduced to ' + str(ref_price) +''
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(mail_id, recipient, message)

    print('Email Sent!')
    server.quit()


check_price()
