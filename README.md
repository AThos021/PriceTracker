# Price Tracker
This is a Python script for tracking the price of an item on popular e-commerce websites like Amazon and Flipkart. It uses web scraping with BeautifulSoup and Selenium to fetch the price of the item and send notifications via email and WhatsApp when the desired price is reached.

# Prerequisites
- Python 3.x
- BeautifulSoup 4
- Selenium
- Chromedriver (for Selenium)
- Requests
- smtplib (Python built-in library)
# Installation
- Install Python on your machine, if not already installed.
- Install the required libraries using the following pip command:
```
pip install beautifulsoup4 selenium requests
```
- Download and install the latest Chromedriver from https://chromedriver.chromium.org/downloads based on your operating system and Chrome version.
- Update the Chromedriver path in the code to the location where you installed it.
# Usage
- Clone or download the repository to your local machine.
- Open the price_tracker.py file and update the url, desired_price, receiver_email, and ph_no variables according to your requirements.
- Run the script using the following command:
```
python Pricetracker.py
```
- The script will start tracking the price of the item on the specified website (Amazon or Flipkart) and send notifications via email and WhatsApp when the desired price is reached.
# Features
- Fetches the price of the item from Amazon or Flipkart using web scraping.
- Sends email notifications with an attached screenshot of the item when the desired price is reached.
- Sends WhatsApp notifications with a link to the item and an attached screenshot when the desired price is reached.
- Takes a screenshot of the item for email and WhatsApp notifications.
- Uses Selenium for web automation tasks like taking screenshots and sending WhatsApp messages.

# Customization
- The script can be easily customized according to your requirements. Some possible customizations include:
- Updating the website URL to track prices from a different e-commerce website.
- Modifying the email and WhatsApp message templates to suit your preferences.
- Changing the desired price threshold for notifications.
- Updating the sender and receiver email addresses for notifications.

# Note
- The script uses web scraping, which relies on the HTML structure of the e-commerce websites. Any changes to the website's structure may break the script.
- Use this script responsibly and in compliance with the terms of use of the e-commerce websites.
- Make sure to update the Chromedriver path in the code to the location where you installed it on your machine.
- The script uses the Gmail SMTP server for sending email notifications. Make sure to enable "Less Secure Apps" in your Gmail settings if you're using a Gmail account for sending email notifications.
# License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.