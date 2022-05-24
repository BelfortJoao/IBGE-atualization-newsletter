""" """
from Graphs_plot import graphs_plot
from Report import create_pdf
from Config import emailsToSend
from Helper import send_email
import schedule
import time


def job():
    graphs_plot()
    create_pdf()
    for i in emailsToSend:
        send_email(i)


schedule.every().day.at('9:30').do(job())

while True:
    schedule.run_pending()
    time.sleep(1)
