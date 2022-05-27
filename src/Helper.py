"""Some functions that help others, ina others archives."""

# external imports
import urllib3
import json
import smtplib
from datetime import date

# internal imports
import Config
from email.message import EmailMessage

# path of the project in the device, put yours
path = 'C:/Users/Belfo/OneDrive/Área de Trabalho/projeto api ibge'


# make a Json
def make_json(url: str):
    """Get the request from the selected API url, and show if the response is true or false.
    Return a Json of the URL"""
    # get the URL
    http = urllib3.PoolManager()
    urlportalapiibge = url

    # se if the URL respond
    response = http.request('GET', urlportalapiibge)
    if response.status == 200:
        print(f"accessing website:\n {url}\n response status: True\n")
    else:
        print(f"accessing website:\n {url}\n response status: False\n")

    # make and return Json
    getteddatajson = json.loads(response.data.decode("utf-8"))
    return getteddatajson


# send the email
def send_email(addres):
    """Get the email information from the config file.
    Send the graph to a gmail.
    Login Credentials for sending the e-mail."""

    # get the email information
    msg = EmailMessage()
    msg["Subject"] = Config.subject
    msg["From"] = Config.emailAddres
    msg["To"] = addres
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(Config.email_body)
    with open(f'{path}/IBGE-Auctualization-service/src/PDFs/report.pdf', 'rb') as f:
        data = f.read()

    msg.add_attachment(data, filename='report.pdf', maintype='application/pdf', subtype='pdf')

    # login the gmail
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(Config.emailAddres, Config.emailpassword)
    s.sendmail(Config.emailAddres, [addres], msg.as_string().encode('utf-8'))
    print(f"email enviado para:{addres}")


# create the trimestral most recent URL str.
def generate_trimestral_timelist(year: int, trimester: int):
    """Make a list that fit in the IBGE API URL link, to get the most recent information."""

    current_year = date.today().year
    time_list = ''
    for i in range(year, current_year + 1):
        for j in range(trimester, 5):
            if i == current_year and j == 4:
                time_list += str(i) + '0' + str(j)
            else:
                time_list += str(i) + '0' + str(j) + '|'
        if i == current_year:
            return time_list
    return time_list


# create the most recent URL str
def generate_timelist(year: int):
    """Make a list that fit in the IBGE API URL link, to get the most recent information."""

    current_year = date.today().year
    time_list = ''
    for i in range(year, current_year + 1):
        if i == current_year:
            time_list += str(i)
            return time_list
        time_list += str(i) + '|'

    return time_list
