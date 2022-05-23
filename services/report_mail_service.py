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
for xfile in glob.glob(report_dir):
    tid = xfile.split('_')[3]
    json_file = './mail_list.json'
    with open(json_file) as jfile:
        json_data = json.load(jfile)
    for jdata in json_data:
        if jdata['id'] == tid:
            subject = "{}".format(xfile.split('\\')[-1].split('.')[0])
            receiver_email = ', '.join(jdata['to'])
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = ', '.join(jdata['to'])
            message["Subject"] = subject
            message["Cc"] = ", ".join(jdata['cc'])  # Recommended for mass emails

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

            filename = xfile  # In same directory as script
            actual_name = xfile.split('\\')[-1]

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
                f"attachment; filename= {actual_name}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            # Send the message via local SMTP server.
            s = smtplib.SMTP("192.168.5.3")
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
            s.sendmail(sender_email, receiver_email, message.as_string())
            s.quit()
