from Graphs_plot import graphs_plot
from Report import create_pdf
from config import emailsToSend
from functions import send_email

graphs_plot()
create_pdf()
for i in emailsToSend:
    send_email(i)
