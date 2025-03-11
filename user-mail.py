import smtplib
import cv2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



sender_email = 'saiphanikrishna9@gmail.com'
sender_password = 'tspe hjaz ceid ylqg'
recipient_email = 'saiphanikrishna05@gmail.com'

subject = '🚨 Intruder Alert!'
body = 'Motion detected! See attached frames.'


def send_email(frames, sender_email, sender_password, recipient_email, subject, body):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Attach frames as images
        for i, frame in enumerate(frames):
            success, frame_jpeg = cv2.imencode(".jpg", frame)
            if success:  
                image = MIMEImage(frame_jpeg.tobytes())
                image.add_header("Content-Disposition", "attachment", filename=f"frame{i+1}.jpg")
                msg.attach(image)

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("📩 Email sent successfully!")

    except Exception as e:
        print(f"❌ Error sending email: {e}")

