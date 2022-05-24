import matplotlib.pyplot as plt


class Data:
    def __init__(self):
        self.data_x = []
        self.data_y = []
        self.titulo = 't'
        self.var_x = 'x'
        self.var_y = 'y'
        self.index = 0

    def data_api_extrator(self, json):
        self.titulo = json[0]['variavel']
        self.var_x = "ano"
        self.var_y = json[0]['unidade']
        self.data_x = list(json[0]['resultados'][0]['series'][0]['serie'].values())
        self.data_y = list(json[0]['resultados'][0]['series'][0]['serie'].keys())


def data_ploter(data: Data):
    fig, axs = plt.subplots(1, 1, figsize=(14, 7))
    axs.plot(data.data_y, data.data_x)
    fig.suptitle(data.titulo)
    name = ''.join(data.titulo)
    plt.savefig(f'Images/{name}')
