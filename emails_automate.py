import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 1. Load Excel file (columns: Name, Email)
df = pd.read_excel("sample emails data.xlsx")  

# 2. Your Gmail credentials
your_email = "youremail@gmail.com"
your_password = "yourpassword"   # use Gmail app password

# 3. File to attach (your resume)
resume_path = "sample resume.pdf"   

# 4. Setup SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(your_email, your_password)

# 5. Loop through each row and send email
for index, row in df.iterrows():
    name = row["Name"]
    recipient = row["Email"]

    # Create the message
    msg = MIMEMultipart()
    msg["From"] = "yourname"
    msg["To"] = recipient
    msg["Subject"] = "write your subject"

    # Body with personalization
    body = f"""
Hi {name},
I hope you're doing well. My name is (yourname), and I wanted to reach out and introduce myself. I’ve been following your work and really admire [something specific about their role, company, or content].
If you're open to it, I’d love to connect and learn more about your journey. I’m exploring new opportunities and always keen to exchange ideas with people doing impactful work.
Thanks for your time,
(yourname)

    """
    msg.attach(MIMEText(body, "plain"))

    # Attach Resume
    with open(resume_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={resume_path}")
        msg.attach(part)

    # Send the email
    server.sendmail(your_email, recipient, msg.as_string())
    print(f"✅ Email sent to {name} at {recipient}")

# 6. Close server
server.quit()
