""" """
from datetime import date

subject = "Daily Report"

email_body = f"""
<p>This is a daily report</p>
<p>Good morning</p>
<p>date:{date.today().day}/{date.today().month}/{date.today().year}</p>
"""
emailAddres = "IBGEAtualizationService@gmail.com"
emailpassword = "Password"
emailsToSend = ["goldchaos216@gmail.com", "wellington1belfort@gmail.com"]
