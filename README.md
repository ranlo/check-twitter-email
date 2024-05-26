# check-twitter-email

check if an email is being used by a user on twitter

usage:

python3 ./email_check.py email1@domain.com email2@domain.com email3@domain.com

or

python3 ./email_check.py < email_list.txt

will output emails used by accounts

important: contains a 30 seconds sleep to prevent 429 when running in a loop
