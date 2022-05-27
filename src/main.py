"""the main codes that actualize every graph and the pdf every day in 9:30am"""

# internal functions imports
from Graphs_plot import graphs_plot
from Report import create_pdf
from Config import emailsToSend
from Helper import send_email

# external libraries imports
import schedule
import time


# create a function for the schedule execute
def job():
    # graphs plotting
    graphs_plot()
    # creating pdfs
    create_pdf()
    # send email for every email in the email list, on config file.
    for i in emailsToSend:
        send_email(i)


# schedule
schedule.every().day.at('9:30').do(job())

# infinity loop of schedule
while True:
    schedule.run_pending()
    time.sleep(1)
