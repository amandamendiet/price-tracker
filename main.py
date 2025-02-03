from bs4 import BeautifulSoup
import requests
import os
import dotenv
import smtplib

dotenv.load_dotenv()

URL = "https://www.amazon.com/DUMOS-Armless-Computer-Seating-Adjustable/dp/B0CZLHFWL8/ref=sr_1_5?crid=38TDRJ2KFBPAB&dib=eyJ2IjoiMSJ9.2uH0YobeW2KzwngsMupNiodVDd58qPVv8uHOW5sWqCAXC6bggW82ssXEZb_3-nDfeyqDOW0gEVUhpz55UCjML5alGy-YghbbWq3g_GvJYAHf-mLY6n3cUIn1qOYAL8-U2cQbz7GuJwn5BMjCKtjn3nC558j9zsbE8ywWPmJtOGtB11N1UL5wBwadvkju_v2GTr3BbTuwmfO46exaXDvSYXEUyK6fZsoXJws_SjGOzrgOTZ97DMZC6Tvvay3_KlLPssHoZDF0mg2_3AQIL43V1nnR8mexkuZm0wc6xfOSA3jYvB7b0R7yx26WePIGYePhugka7x_MFyycaB-jRYF5YSz1VtcQbrQzp4ozCqtBYWY.YrSVsWhE27XTGkavpbfBFJQV3VuBjwfljyqY2ULrMv8&dib_tag=se&keywords=foldable%2Bdesk%2Bchair&qid=1738612249&s=home-garden&sprefix=foldable%2Bdesk%2Bchair%2Cgarden%2C88&sr=1-5&ufe=app_do%3Aamzn1.fos.9fe8cbfa-bf43-43d1-a707-3f4e65a4b666&th=1"
TARGET_PRICE = 100
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
AMAZON_HEADERS = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
                  'Accept-Language':'en-US,en;q=0.9',
                  }

response = requests.get(url=URL, headers=AMAZON_HEADERS).text

soup = BeautifulSoup(response, "html.parser")
price = float(soup.find("span", class_="aok-offscreen").text.split("$")[1].split(" ")[0])
print(price)
product = soup.find("span", id="productTitle").text.strip().split("   ")[0]
print(product)

if price < TARGET_PRICE:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=RECEIVER_EMAIL,
                            msg=f"Subject:Price alert for {product}\n\nThe price is: ${price}. Buy now!\n"
                                f"Link: {URL}")
