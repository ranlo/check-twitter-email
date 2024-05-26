import sys
import requests
import json
import time
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
def check_email_availability(email):
    url = f"https://api.x.com/i/users/email_available.json?email={email}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        if 'msg' in data and data['msg'] == 'Email has already been taken.':
            return True
    return False

def main():
    if len(sys.argv) > 1:
        emails = sys.argv[1:]
    else:
        emails = [line.strip() for line in sys.stdin]

    for email in emails:
        if check_email_availability(email):
            print(email)
        time.sleep(30)

if __name__ == "__main__":
    main()

