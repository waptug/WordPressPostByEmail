import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from getpass import getpass

# Load existing environment variables
load_dotenv()

# Get the email address and password
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')

# If the email, password, SMTP server or port is not set, ask for them
if not email or not password or not smtp_server or not smtp_port:
    email = input("Please enter the email address to post to: ")
    password = getpass("Please enter the password for the email account: ")
    smtp_server = input("Please enter the SMTP server address: ")
    smtp_port = input("Please enter the SMTP server port: ")

    # Write the email, password, SMTP server and port to the .env file
    with open('.env', 'w') as file:
        file.write(f'EMAIL={email}\n')
        file.write(f'PASSWORD={password}\n')
        file.write(f'SMTP_SERVER={smtp_server}\n')
        file.write(f'SMTP_PORT={smtp_port}\n')

# Select a random file from a nested folder of text files
folder = input("Please enter the path to the text files folder: ")
text_files = [os.path.join(root, name)
              for root, dirs, files in os.walk(folder)
              for name in files
              if name.endswith((".txt"))]

random_file = random.choice(text_files)

# Read the content of the random file and set the subject to the first line
with open(random_file, 'r') as file:
    lines = file.readlines()
    subject = lines[0].strip()
    content = ''.join(lines[2:]).strip()  # Skip the blank line after the title

# Replace two consecutive newline characters with HTML paragraph tags
content = content.replace('\n\n', '</p><p>')

# Select a random image from a folder
image_folder = input("Please enter the path to the images folder: ")
image_files = [os.path.join(root, name)
               for root, dirs, files in os.walk(image_folder)
               for name in files
               if name.endswith((".png", ".jpg", ".jpeg", ".gif"))]

random_image = random.choice(image_files)

# Set up the email
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = email
msg['Subject'] = subject

# Convert the content to HTML and attach it to the email
html_content = f'<html><body><p>{content}</p></body></html>'
msg.attach(MIMEText(html_content, 'html'))

# Attach the text file
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(random_file, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(random_file))
msg.attach(part)

# Attach the image
with open(random_image, 'rb') as img:
    msg.attach(MIMEImage(img.read()))

# Send the email
server = smtplib.SMTP(smtp_server, int(smtp_port))
server.starttls()
server.login(email, password)
server.send_message(msg)
server.quit()
