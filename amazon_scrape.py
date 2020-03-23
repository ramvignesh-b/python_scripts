import requests
from bs4 import BeautifulSoup as bs
from decimal import Decimal
import smtplib
import time
from datetime import datetime

URL= 'https://www.amazon.in/Lenovo-Legion-Graphics-Windows-81SY00CKIN/dp/B07W6H9YM9/ref=sr_1_3?keywords=y540&qid=1578141911&sr=8-3' #product URL

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

mail_id = 'ramvignesh.codes@gmail.com' #The mail ID from where the mail will be sent
app_pass = 'whvpktonrsznfnxz' #Generated "app-specific password" from Gmail Account Settings 
recipient = 'ramvigneshgreat@gmail.com' #where the email will be sent to

def check_price():
    target_price = 63000 #Email will be sent once the products price reach below this value
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    ref_price = Decimal(price[2:].replace(",","")) #the actual price of the product
    print(datetime.now().strftime("%H:%M:%S"),'Checking price.....')
    print(price)
    if(ref_price <= target_price):
        send_mail(title,ref_price)

def send_mail(title1,ref_price1): #function to send the mail
    title = title1
    ref_price = ref_price1
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mail_id, app_pass)

    subject = 'Price is slashed ^_^'
    body = r'The price of the product "' + title.strip() + r'" has been reduced to Rs.' + str(ref_price) +'!'
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(mail_id, recipient, message)

    print('Email Sent!')
    server.quit()

while True:
    check_price()
    time.sleep(3600) #check every hour
