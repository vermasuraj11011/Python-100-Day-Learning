import smtplib

my_email = 'myemail@gmail.com'
password = 'mypassword'

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='friend@gmail.com',
                        msg='Subject:Hii\n\nThis is a test email')
