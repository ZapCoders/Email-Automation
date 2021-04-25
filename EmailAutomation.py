import smtplib

sender = input("Who is the sender?")
receivers = input("Who are the recipients?")
message = input("What is the message?")

filterRecipients = receivers.replace(" ", "")
listRecipients = filterRecipients.split(",")

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("USERNAME", "PASSWORD")

    for i in listRecipients:
        server.sendmail(sender, i, message)

    print("The message has been sent!")

except:
    print("Oops! Something went wrong.")