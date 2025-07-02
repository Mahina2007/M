# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from utils import random_num
#
# from file_manager import writerows, read
#
#
# def send_email(receiver_email, body):
#
#     sender_email = "sanjarbeksocial@gmail.com"
#     password = "ajvd xsnx jowk hujh"
#
#     subject = "Test Email"
#
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))
#
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             text = msg.as_string()
#             server.sendmail(sender_email, receiver_email, text)
#             print("Email sent successfully!")
#
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")
#
#
#
# def login():
#     email = input("email: ")
#     password = input("password: ")
#
#
# def logout():
#     print("logout")
#
# def register():
#     full_name_T = input("full name: ")
#     email_T =  input("email: ")
#     password1_T = random_num
#     password2_T = input("confirm the password: ")
#
#     data = []

