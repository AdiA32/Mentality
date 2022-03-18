# sms: vtext.com
# mms: mypixmessages.com
# xdncltargkvgrvbn
import email, smtplib, ssl


def send_sms_via_email(
    number: str,
    message: str,
    sender_credentials: tuple,
    subject: str = "Mentality python script",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiever_email = f"{number}@vtext.com"

    # email_message = f"Subject:{subject}\nTo:{receiever_email}\n{message}"
    email_message = f"To:{receiever_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiever_email, email_message)
def main():
    number = "9258758376"
    message = "hello!"

    sender_credentials = ("ccvdc123@gmail.com", "xdncltargkvgrvbn")

    send_sms_via_email(number, message, sender_credentials)

if __name__ == "__main__":
    main()
