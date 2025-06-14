import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "Dear Team,\n Please find the attached day end report status."
sender_email = "ofx.shotbuzz@gmail.com"
receiver_email = "narendhar.c.c@gmail.com,ofx.shotbuzz@gmail.com"
password = "shotBuzz#5262"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
reciepients = ['narendhar.c.c@gmail.com', 'ofx.shotbuzz@gmail.com']
print(", ".join(reciepients))
message["Cc"] = ", ".join(reciepients)  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "./test/test.txt"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)