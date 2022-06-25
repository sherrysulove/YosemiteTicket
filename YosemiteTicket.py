import requests
import smtplib
import sys
import time
from random import randint
 
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@page.nextel.com"
}
 
EMAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD

def cli(phone_number, carrier, message):
	url = 'https://www.recreation.gov/api/timedentry/availability/facility/10086745/monthlyAvailabilitySummaryView?year=2022&month=07&inventoryBucket=FIT&tourID=10086746'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}
	r = requests.get(url, headers=headers, verify=False)
	avail = r.json()['facility_availability_summary_view_by_local_date']['2022-07-02']['tour_availability_summary_view_by_tour_id']['10086746']['reservable']
	if avail > 0:
		send_message(phone_number, carrier, message)
 
def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
 
 
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
        sys.exit(0)
 		
    phone_number = sys.argv[1]
    carrier = sys.argv[2]
    message = sys.argv[3]

    while True:
        cli(phone_number, carrier, message)
        time.sleep(randint(20,40))
