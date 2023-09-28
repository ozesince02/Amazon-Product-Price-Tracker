# Amazon Price Tracker

This Python script allows you to track the price of a product on Amazon and sends you an email notification if the price falls below your specified target price. It uses web scraping techniques to extract the price information from the Amazon product page.

### Features

* Web scrapes the Amazon product page for the current price.
* Sends an email alert if the price is below the target price.
* Easy to configure with your own email and target price.
* Uses popular libraries such as BeautifulSoup and requests.

### Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.x installed on your system.
* Required Python packages installed. You can install them using 'pip':

```
    pip install requests
    pip install smtplib
    pip install beautifulsoup4
```

### Usage

1. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/amazon-price-tracker.git
```
2. Open the 'amazon_price_tracker.py' file in a text editor.
3.Replace the following variables with your own information:

    * 'MY_EMAIL': Your Gmail email address.
    * 'MY_PASSWORD': Your Gmail email password.
    * 'target_price': The target price at which you want to receive a notification.
    * 'URL': The URL of the Amazon product you want to track. Make sure it's the correct product page URL.

4. Save your changes.

5. Run the script:
```
    python amazon_price_tracker.py
```
The script will scrape the Amazon product page, check the price against your target price, and send you an email alert if the price is lower than or equal to the target price.
The script uses Gmail for sending email notifications. If you haven't already, you may need to enable "Less secure apps" in your Gmail settings to allow the script to send emails using your Gmail account.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Disclaimer

This script is intended for educational and personal use only. Use it responsibly and in accordance with Amazon's terms of service. The authors are not responsible for any misuse or violation of Amazon's terms.

### Acknowledgments

* This script was created with the help of Python, requests, BeautifulSoup, and smtplib.
* Inspired by online tutorials and resources on web scraping and email notifications in Python.
