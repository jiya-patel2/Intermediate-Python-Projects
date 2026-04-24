from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
# link of the article whose price you want to track 
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(URL,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0","Accept-Language":"en-GB,en;q=0.9",})
response.raise_for_status()

html_website = response.text

soup = BeautifulSoup(html_website,"html.parser")

symbol_price = soup.find(class_ = "a-price-whole").get_text()
print(symbol_price)
price = float(symbol_price.replace(",","").replace(".",""))
print(price)

# sending email
target_price = 11000
if price <= target_price:
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(email, password)

            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"price drop on article {price}"
            )