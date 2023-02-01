
import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("snafaba5003@gmail.com", "ydqqnvkwvimisnuu")
mail.select("inbox")

status, messages = mail.search(None, 'UNSEEN')

for msg_id in messages[0].split():
    status, msg = mail.fetch(msg_id, "(RFC822)")
    email_message = email.message_from_bytes(msg[0][1])
    print(email_message['subject'])


#snafaba5003@gmail.com
#ydqqnvkwvimisnuu
