# Amazon Price Tracker

A Python script that **monitors an Amazon product’s price** and sends an **email alert** when it drops below your desired threshold.  
Built using **BeautifulSoup** for web scraping, **requests** for fetching page data, and **smtplib** for sending notifications via Gmail.

---

## What It Does
- Scrapes an Amazon product page for its **current price** and **title**
- Compares the price to your `TARGET_PRICE`
- Sends an **email notification** if the price drops below that threshold
- Automatically includes the **product link** for quick access

---

## How It Works
1. Uses `requests` to fetch the product page with custom headers (bypassing Amazon bot filters)  
2. Parses the page with `BeautifulSoup` to extract:
   - Product title
   - Current price  
3. If the price < `TARGET_PRICE`, it:
   - Logs into your Gmail account (securely via `smtplib`)
   - Sends you an alert email with the product name, price, and URL  

---

## Customize the Script
Edit your constants in the script:
```python
URL = "https://www.amazon.com/your-product-link"
TARGET_PRICE = 100
```
---

## Example Email Alert
```
Subject: Price alert for DUMOS Armless Computer Chair

The price is: $99.00. Buy now!
Link: https://www.amazon.com/DUMOS-Armless-Computer-Seating-Adjustable/dp/B0CZLHFWL8
```

