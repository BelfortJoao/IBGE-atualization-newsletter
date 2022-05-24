import functions
import Data


def graphs_plot():
    time_list_IPCA = functions.generate_trimestral_timelist(2020, 1)
    time_list_PIB = functions.generate_timelist(1996)

    pib_percapta_URL = f'http://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/{time_list_PIB}/variaveis/9812?localidades=N1[all]'
    pib_em_variacao_URL = f'https://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/{time_list_PIB}/variaveis/9810?localidades=N1[all]'
    ipca_variacao_mensal_URL = f'http://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_IPCA}/variaveis/63?localidades=N1[all]&classificacao=315[7169]'
    ipca_variacao_acumulada_ano_URL = f'http://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_IPCA}/variaveis/69?localidades=N1[all]&classificacao=315[7169]'
    ipca_variacao_12_meses_URL = f'https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_IPCA}/variaveis/2265?localidades=N1[all]&classificacao=315[7169]'

    pib_percapta_json = functions.make_json(pib_percapta_URL)
    pib_em_variacao_json = functions.make_json(pib_em_variacao_URL)
    ipca_variacao_mensal_json = functions.make_json(ipca_variacao_mensal_URL)
    ipca_variacao_acumulada_ano_json = functions.make_json(ipca_variacao_acumulada_ano_URL)
    ipca_variacao_12_meses_json = functions.make_json(ipca_variacao_12_meses_URL)

    pib_percapta_data = Data.Data()
    pib_em_variacao_data = Data.Data()
    ipca_variacao_mensal_data = Data.Data()
    ipca_variacao_acumulada_ano_data = Data.Data()
    ipca_variacao_12_meses_data = Data.Data()

    pib_percapta_data.data_api_extrator(pib_percapta_json)
    pib_em_variacao_data.data_api_extrator(pib_em_variacao_json)
    ipca_variacao_mensal_data.data_api_extrator(ipca_variacao_mensal_json)
    ipca_variacao_acumulada_ano_data.data_api_extrator(ipca_variacao_acumulada_ano_json)
    ipca_variacao_12_meses_data.data_api_extrator(ipca_variacao_12_meses_json)

    Data.data_ploter(pib_percapta_data)
    Data.data_ploter(pib_em_variacao_data)
    Data.data_ploter(ipca_variacao_mensal_data)
    Data.data_ploter(ipca_variacao_acumulada_ano_data)
    Data.data_ploter(ipca_variacao_12_meses_data)


class populacao:
    def __init__(self):
        self.json = ""

    def get_pupulation(self):
        populacao_URL = 'http://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
        self.json = functions.make_json(populacao_URL)
        Index_populacao = self.json['projecao']['populacao']
        return Index_populacao

    def get_horario(self):
        populacao_URL = 'http://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
        self.json = functions.make_json(populacao_URL)
        Index_horario = self.json['horario']
        return Index_horario
# functions.send_email(addres)
