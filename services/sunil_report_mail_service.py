import glob
import json
import smtplib
import ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

body = "Dear Team,\n Please find the attached day end report status."
sender_email = "shotbuzzalerts@oscarfx.com"

today_date = datetime.now().date()
report_dir = './{}/*.xlsx'.format(today_date)
subject = "OFX DAY END TEAM REPORTS-{}".format(today_date)
receiver_email = "sunil.milkuri@oscarfx.com"
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = """<html><body>
        <div>Dear Team,\n Please find the attached day end report status.<br><br></div>
        <div>
    </br>
    </br>
    </br>
    </br>
    <h5>Do not reply to this email. This is automated email notification from ShotBuzz Automated Email Service.</h5>
    <div style="font-size: 13px; font-family: Tahoma, Helvetica, sans-serif;"><span style="color: rgb(153, 153, 153); font-family: tahoma, sans-serif; font-size: x-small; background-color: rgb(255, 255, 255);">This message and any attachment(s) is intended only for the use of the addressee(s) and may contain information that is PRIVILEGED and CONFIDENTIAL. If you are not the intended addressee(s), you are hereby notified that any use, distribution, disclosure or copying of this communication is strictly prohibited. If you have received this communication in error, please erase all copies of the message and its attachment(s) and notify the sender immediately.</span></div>&nbsp;</div>
    </div>
</body></html>"""
message.attach(MIMEText(html, "html"))

report_dir = './{}\\*.xlsx'.format(today_date)
for xfile in glob.glob(report_dir):
    filename = xfile  # In same directory as script
    actual_name = xfile.split('\\')[-1]

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        partt = MIMEBase("application", "octet-stream")
        partt.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(partt)

    # Add header as key/value pair to attachment part
    partt.add_header(
        "Content-Disposition",
        f"attachment; filename= {actual_name}",
    )

    # Add attachment to message and convert message to string
    message.attach(partt)
# Send the message via local SMTP server.
s = smtplib.SMTP("192.168.5.3")
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(sender_email, receiver_email, message.as_string())
s.quit()

