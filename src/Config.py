"""The only file that needs to be open to edit the email configurations."""

# internal imports
from datetime import date

# email message configurations
subject = "Daily Report"

email_body = f"""
<p>This is a daily report</p>
<p>Good morning</p>
<p>date:{date.today().day}/{date.today().month}/{date.today().year}</p>
"""

# email login, and password configurations
emailAddres = "IBGEAtualizationService@gmail.com"
emailpassword = "Password"

# email list to send emails
emailsToSend = ["goldchaos216@gmail.com", "wellington1belfort@gmail.com"]
