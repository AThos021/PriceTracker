import requests
import smtplib
import ssl
import random
from time import sleep
from email import encoders
from bs4 import BeautifulSoup
from selenium import webdriver
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Check The Price of The item
def get_price(url):
    headr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Accept-Encoding': None
    }
    req = requests.get(url, headers= headr)
    t = BeautifulSoup(req.content, 'html.parser')

    # Checking in Amazon
    if 'amazon' in url:
        price = t.find('span', {'class': 'a-price-whole'}).text
        product = t.find('span', {'id': 'productTitle'}).text
        site = 'amazon'

    # Checking in Flipkart
    elif 'flipkart' in url: 
        price = t.find('div', {'class': '_30jeq3 _16Jk6d'}).text[1:]
        product = t.find('span', {'class': 'B_NuCI'}).text
        site = 'flipkart'

    price = price.replace(",","")
    list = []
    list.append(price)
    list.append(product)
    list.append(site)
    return list

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Show Price
def showPrice(url):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    sleep(random.uniform(2.5, 4.9))
    driver.close()
    driver.quit()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Take Screenshot
def take_screenshot(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    driver.get_screenshot_as_file("Price_Alert.png")
    print()
    print("*"*5 + "-"*10 + "*"*5)
    print("ScreenShot Has been Taken!!")
    print("*"*5 + "-"*10 + "*"*5)
    print()
    sleep(random.uniform(2.5, 4.9))
    driver.close()
    driver.quit()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Sending Whatsapp Message
def what_noti(url, list, ph_no):
    try:
        filepath = "D:\Github\PriceTracker\Price_Alert.png"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('user-data-dir=C:\\Users\debdi\\AppData\\Local\\Google\\Chrome\\User Data')   # Adding the User Data path of Chrome
        driver = webdriver.Chrome(options=options)
        mes = 'https://web.whatsapp.com/send/?phone='+ ph_no+'&amp;text&amp;type=phone_number&amp;app_absent=0'
        driver.get(mes)
        wait = WebDriverWait(driver, 100)

        text = "*!!!!!!!!!! Hurray !!!!!!!!!!*"
        message = "The *"
        message1 = list[1].strip()
        message2 = "* is now Available at "
        message3 = "*" + "\u20B9" + list[0].strip() + "*"
        message4 = "*The Link is Pinned Down Below*"
        message5 = url

        #Click on the Attachment box
        attach_box = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')))
        attach_box.click()
        sleep(random.uniform(2.5, 4.9))
        

        wb_furthe = driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')
        wb_furthe.send_keys(filepath)
        sleep(random.uniform(2.5, 4.9))
        

        write_line = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        write_line.send_keys(text + Keys.SHIFT + Keys.ENTER)
        write_line.send_keys(Keys.SHIFT + Keys.ENTER)
        write_line.send_keys(message)
        write_line.send_keys(message1)
        write_line.send_keys(message2)
        write_line.send_keys(message3)

        write_line.send_keys(Keys.SHIFT + Keys.ENTER)
        write_line.send_keys(Keys.SHIFT + Keys.ENTER)

        write_line.send_keys(message4)
        write_line.send_keys(Keys.SHIFT + Keys.ENTER)
        write_line.send_keys(message5)

        sleep(random.uniform(2.5, 4.9))
    
        wb1 = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        wb1.click()
        sleep(random.uniform(2.5, 4.9))

        driver.close()
        driver.quit()
    
    except Exception as e:
        print(e)
        
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Mailing Price when The Desired price is reached
def mail_price(list, receiver_email):
    subject = list[2] +" Price Alert"
    product = list[1].strip()
    price = list[0].strip()

    message = MIMEMultipart()

    part0= f"{' ' * 20}Hurray!!!!!!!!!!"
    message.attach(MIMEText(part0, "plain"))
    part1 = f"🎉🎉🎉🎉🎉🎉🎉\n\nThe "
    message.attach(MIMEText(part1, "plain"))
    part2 = f"<b>{product}</b>"
    message.attach(MIMEText(part2, "html"))
    part3 = f"is now at "
    message.attach(MIMEText(part3, "plain"))
    part4 = f"<b>{price}</b>"
    message.attach(MIMEText(part4, "html"))

    sender_email = "checkappsandserivices@gmail.com"
    password = 'oszbhhcooymwtkrc'

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = """
    <html>
    <body>
        <p style="font-family: Times New Roman, serif; font-size: 20px; color: #FF0000;">
        Please find the Below Attachment
        </p>
    </body>
    </html>
    """
    message.attach(MIMEText(body, 'html'))

    filename = 'Price_Alert.png'

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Prediction to Buy or not
def price_chart(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 100)

        driver.get('https://pricehistoryapp.com/')
        driver.maximize_window()

        # Search box find
        driver.implicitly_wait(4)
        link_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/section[2]/div/input')))
        link_box = driver.find_element(by= By.XPATH, value='//*[@id="__next"]/div[2]/section[2]/div/input')
        link_box.send_keys(url) 
        

        # Click on Search Button
        search_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/section[2]/div/button')))
        search_button.click()

        sleep(4)

        # Getting The Price Chart
        price = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[3]'))).text.split(".")[:-1]

        # Alert
        exactly = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div[4]/p[2]'))).text

        length = len(price)
        word1 = price[length-2].split()
        word2 = price[length-1].split()

        numbers1 = [int(word) for word in word1 if word.isdigit()]

        CurrentPrice = numbers1[0]
        LowestPrice = numbers1[1]

        numbers2 = [int(word) for word in word2 if word.isdigit()]

        AveragePrice = numbers2[0]
        HighestPrice = numbers2[1]

        list = []
        list.append(CurrentPrice)
        list.append(LowestPrice)
        list.append(AveragePrice)
        list.append(HighestPrice)
        list.append(exactly)

        driver.close()
        driver.quit()
        return list

    except:
        print(" Sorry, The Item Details Cannot be Found!!! ")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Good Time to buy
def buy_time(price_list):

    print()
    print("Is it Good Time To Buy This Product?")
    print()
    print(price_list[4])
    print()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Main Function
if __name__ == '__main__':
    url = input("Enter The Link: ")
    print()
    showPrice(url)
    print()
    price_list = price_chart(url)
    currentPrice = price_list[0]
    lowestPrice = price_list[1]
    averagePrice = price_list[2]
    highestPrice = price_list[3]
    print()
    print("****************** Price List *******************")    
    print("-" * 49)
    print()
    print("Current Price ---------------------->  " + str(currentPrice))
    print()
    print("Lowest Price  ---------------------->  " + str(lowestPrice))
    print()
    print("Average Price ---------------------->  " + str(averagePrice))
    print()
    print("Highest Price ---------------------->  " + str(highestPrice))
    print()

    buy_time(price_list)

    print()
    desired_price = float(input("Enter The Desired Price is"+ ":"))
    print()
    noti = input("Do You Need any Notification about Price(Y/N): ")
    print()
    

    if noti.lower() == 'y':
        print()
        fic = input("Notification on Whatsapp or Gmail or Both: ")
        print()
        if fic.lower() == "whatsapp":
            print()
            ph_no = input("Please Provide Your Phone Number with Country Code: ")              
            print()
        elif fic.lower() == "gmail":
            print()
            receiver_email = input("Enter The Receiver Email: ")
            print()
        else:
            print()
            ph_no = input("Please Provide Your Phone Number with Country Code: ")
            print()
            receiver_email = input("Enter The Receiver Email: ")
            print()

        flag = 1

        while True:
            list = get_price(url)
            price = float(list[0])
            if price <= desired_price:
                    if fic.lower() == "whatsapp":
                        take_screenshot(url)
                        what_noti(url, list, ph_no)
                        print()
                        print("*****----------------******")
                        print("Whatsapp Message Sent Successfully")
                        print()
                        break
                    elif fic.lower() == "gmail":
                        take_screenshot(url)
                        mail_price(list,receiver_email)
                        print()
                        print("*****----------------******")
                        print("Mail Sent Successfully")
                        print()
                        break
                    else:
                        take_screenshot(url)
                        what_noti(url, list, ph_no)
                        sleep(4)
                        mail_price(list, receiver_email)
                        print()
                        print("*****----------------******")
                        print("Whatsapp Message & Mail Sent Successfully")
                        print()
                        break

            else:
                # The below part will print only for the first time when the price will not below or same to the desired price but for next iteration it will not print it
                if(flag == 1):
                    print()
                    print("SORRY!!")
                    print("Now, The Price of The Product is: " + list[0])
                    print()
                    print("We Will reach out to when Your Desired Price Will There")
                    flag = flag + 1
                    print()
        
            sleep(86400) # The Loop will Again rotate after the One Day and checks that the Price got down to the Desired Price or not
    
    else:
        print()
        print("Thank You For Your Response!!")
        print()
