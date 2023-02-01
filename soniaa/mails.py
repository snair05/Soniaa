import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("snafaba5003@gmail.com", "ydqqnvkwvimisnuu")
mail.select("inbox")

status, messages = mail.search(None, 'UNSEEN')

for msg_id in messages[0].split():
    status, msg = mail.fetch(msg_id, "(RFC822)")
    email_message = email.message_from_bytes(msg[0][1])
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                print(part.get_payload(decode=True).decode("utf-8"))
    else:
        print(email_message.get_payload(decode=True).decode("utf-8"))
