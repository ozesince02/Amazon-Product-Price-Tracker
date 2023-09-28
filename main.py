import requests
import smtplib
from bs4 import BeautifulSoup

MY_EMAIL = 'YourEmail@xyz.com'
MY_PASSWORD = 'YourPassword'

target_price = 1499

URL = "https://www.amazon.in/20000mAh-Sandstone-Triple-Charging-Delivery/dp/B08HV83HL3/ref=sr_1_2_sspa?keywords=power" \
      "%2Bbank%2B20000mah&qid=1678905871&sprefix=power%2Caps%2C257&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1 "
response = requests.get(URL,
                        headers={"Accept-Language": "en-US,en;q=0.5",
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 "
                                               "Firefox/110.0"})
data = response.text
# print(data)
soup = BeautifulSoup(data, "lxml")
price_data = soup.find("span", class_="a-offscreen").getText()
price = (price_data.split("₹")[1]).split(",")
price_string = price[0]+price[1]
price_float = float(price_string)

message = "The deal is up for grabs! Go shopaholic on this deal u been waiting for!"

if price_float <= target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert\n\n{message}\n{URL}"
        )
