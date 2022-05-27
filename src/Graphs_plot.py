"""Plot every graph searching in the apis for data and plotting it in pictures on the Images File.
Uses 2 APIs the IBGE API and the SIDRA API"""

# external imports
import Helper
import Data


# creating a graphs plot function
def graphs_plot():
    """make the most actualized link, for the IBGE API and search for the data.
    return error if the link don't work.
    Create a Data object that contains all the data for plotting.
    Plot the data from the Data, and plot a graph using the plotting function."""

    # generate a str to compleat the IBGE API links
    time_list_ipca = Helper.generate_trimestral_timelist(2020, 1)
    time_list_pib = Helper.generate_timelist(1996)

    # save the modified URLs
    pib_percapta_url = f'http://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/{time_list_pib}/variaveis/9812?localidades=N1[all]'
    pib_em_variacao_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/{time_list_pib}/variaveis/9810?localidades=N1[all]'
    ipca_variacao_mensal_url = f'http://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_ipca}/variaveis/63?localidades=N1[all]&classificacao=315[7169]'
    ipca_variacao_acumulada_ano_url = f'http://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_ipca}/variaveis/69?localidades=N1[all]&classificacao=315[7169]'
    ipca_variacao_12_meses_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_ipca}/variaveis/2265?localidades=N1[all]&classificacao=315[7169]'

    # transform the URLS in a Json variable
    pib_percapta_json = Helper.make_json(pib_percapta_url)
    pib_em_variacao_json = Helper.make_json(pib_em_variacao_url)
    ipca_variacao_mensal_json = Helper.make_json(ipca_variacao_mensal_url)
    ipca_variacao_acumulada_ano_json = Helper.make_json(ipca_variacao_acumulada_ano_url)
    ipca_variacao_12_meses_json = Helper.make_json(ipca_variacao_12_meses_url)

    # create Data objects for every Graph
    pib_percapta_data = Data.Data()
    pib_em_variacao_data = Data.Data()
    ipca_variacao_mensal_data = Data.Data()
    ipca_variacao_acumulada_ano_data = Data.Data()
    ipca_variacao_12_meses_data = Data.Data()

    # extract the Json information and put it in the Data object
    pib_percapta_data.data_api_extrator(pib_percapta_json)
    pib_em_variacao_data.data_api_extrator(pib_em_variacao_json)
    ipca_variacao_mensal_data.data_api_extrator(ipca_variacao_mensal_json)
    ipca_variacao_acumulada_ano_data.data_api_extrator(ipca_variacao_acumulada_ano_json)
    ipca_variacao_12_meses_data.data_api_extrator(ipca_variacao_12_meses_json)

    # plot the graphs
    Data.data_ploter(pib_percapta_data)
    Data.data_ploter(pib_em_variacao_data)
    Data.data_ploter(ipca_variacao_mensal_data)
    Data.data_ploter(ipca_variacao_acumulada_ano_data)
    Data.data_ploter(ipca_variacao_12_meses_data)


class Populacao:
    """An object that saves the population Json information."""

    # init
    def __init__(self):
        self.json = ""

    # get the population
    def get_pupulation(self):
        """Takes the population from the URL, make a Json, and return the population."""

        populacao_url = 'http://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
        self.json = Helper.make_json(populacao_url)
        index_populacao = self.json['projecao']['populacao']
        return index_populacao

    # get the time
    def get_horario(self):
        """Takes the time from the URL, make a Json, and return the time."""

        populacao_url = 'http://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
        self.json = Helper.make_json(populacao_url)
        index_horario = self.json['horario']
        return index_horario
