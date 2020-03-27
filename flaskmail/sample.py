# This is self tutorial on flask 
# here is a listing of all the available flask email configurations and their default values
# 1) MAIL_SERVER : Name/IP address of the email server.- 'localhost'(default value)
# 2) MAIL_PORT : Port number of server used. -25  (default value)
# 3) MAIL_USE_TLS : Enable/disable Transport Security Layer encryption.- False
# 4) MAIL_USE_SSL : Enable/disable Secure Sockets Layer encryption- False
# 5) MAIL_DEBUG : Debug support. The default is Flask application’s debug status. - True
# 6) MAIL_USERNAME : Username of the sender = None
# 7) MAIL_PASSWORD : The password of the corresponding Username of the sender. =None
# 8) MAIL_ASCII_ATTACHMENTS : If set to true, attached filenames converted to ASCII. =False
# 9) MAIL_DEFAULT_SENDER : sets default sender =none
# 10) MAIL_SUPPRESS_SEND : Sending suppressed if app.testing set to true =False
# 11) MAIL_MAX_EMAILS : Sets maximum mails to be sent =none
# To use Gmail's SMTP server, you will need the following settings for your outgoing emails:

# Outgoing Mail (SMTP) Server: smtp.gmail.com
# Use Authentication: Yes
# Use Secure Connection: Yes (TLS or SSL depending on your mail client/website SMTP plugin)
# Username: your Gmail account (e.g. user@gmail.com)
# Password: your Gmail password
# Port: 465 (SSL required) or 587 (TLS required)

# importation
# from flask_mail import Mail

# to instantiate the mail here's the syntax
# mail = Mail(app)
# or
# mail = Mail()
# mail.init_app(app)

# @app.route('/')
# def index():
#     msg =Message('Hey There',recipients =['recipient@gamil.com',example@gmail.com])
#     mail.send(msg)
