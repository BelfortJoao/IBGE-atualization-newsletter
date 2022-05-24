from fpdf import FPDF
from datetime import date
from Graphs_plot import Populacao

pop = Populacao()
width = 210
height = 297


def create_title(pdf):
    pdf.set_font('Times', 'B', 24)
    pdf.ln(55)
    pdf.write(35, "IBGE Analytics Report")
    pdf.ln(10)
    pdf.set_font('Times', '', 20)
    if date.today().month == 12:
        pdf.write(35, f'{date.today().day}/{date.today().month}/{date.today().year}')
    else:
        pdf.write(35, f'{date.today().day}/0{date.today().month}/{date.today().year}')
    pdf.ln(5)
    pdf.set_font('Times', '', 14)
    pdf.cell(35,35,
             f'População atual: {pop.get_pupulation()}, todos os dados referidos neste documentos foram retirados ',
             0, 1, '', False, 'https://servicodados.ibge.gov.br/api/docs/agregados?versao=3')
    pdf.cell(0, -5,
             f'da API de dados do IBGE em {pop.get_horario()}',
             0, 1, '', False, 'https://servicodados.ibge.gov.br/api/docs/agregados?versao=3')
    pdf.ln(5)


def create_pdf():
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Times', 'B', 14)
    '''page 1'''
    pdf.add_page()
    pdf.image("Images/Pag_model_1.png", 0, 0, width)
    create_title(pdf)
    pdf.image("Images/PIB - variação em volume.png", 5, 160, width - 15)
    '''page 2'''
    pdf.add_page()
    pdf.image("Images/Pag_model_2.png", 0, 0, width)
    pdf.image("Images/PIB per capita - valores correntes.png", 5, 50, width - 15)
    pdf.image("Images/IPCA - Variação mensal.png", 5, 160, width - 15)
    '''page 3'''
    pdf.add_page()
    pdf.image("Images/Pag_model_3.png", 0, 0, width)
    pdf.image("Images/IPCA - Variação acumulada em 12 meses.png", 5, 50, width - 15)
    pdf.image("Images/IPCA - Variação acumulada no ano.png", 5, 160, width - 15)
    pdf.output('PDFs/report.pdf', 'F')


create_pdf()
