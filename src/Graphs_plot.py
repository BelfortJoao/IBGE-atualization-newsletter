import Helper
import Data


def graphs_plot():
    time_list_ipca = Helper.generate_trimestral_timelist(2020, 1)
    time_list_pib = Helper.generate_timelist(1996)

    pib_percapta_url = f'http://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/{time_list_pib}/variaveis/9812?localidades=N1[all]'
    pib_em_variacao_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/{time_list_pib}/variaveis/9810?localidades=N1[all]'
    ipca_variacao_mensal_url = f'http://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_ipca}/variaveis/63?localidades=N1[all]&classificacao=315[7169]'
    ipca_variacao_acumulada_ano_url = f'http://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_ipca}/variaveis/69?localidades=N1[all]&classificacao=315[7169]'
    ipca_variacao_12_meses_url = f'https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/{time_list_ipca}/variaveis/2265?localidades=N1[all]&classificacao=315[7169]'

    pib_percapta_json = Helper.make_json(pib_percapta_url)
    pib_em_variacao_json = Helper.make_json(pib_em_variacao_url)
    ipca_variacao_mensal_json = Helper.make_json(ipca_variacao_mensal_url)
    ipca_variacao_acumulada_ano_json = Helper.make_json(ipca_variacao_acumulada_ano_url)
    ipca_variacao_12_meses_json = Helper.make_json(ipca_variacao_12_meses_url)

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


class Populacao:
    def __init__(self):
        self.json = ""

    def get_pupulation(self):
        populacao_URL = 'http://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
        self.json = Helper.make_json(populacao_URL)
        Index_populacao = self.json['projecao']['populacao']
        return Index_populacao

    def get_horario(self):
        populacao_URL = 'http://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
        self.json = Helper.make_json(populacao_URL)
        Index_horario = self.json['horario']
        return Index_horario
