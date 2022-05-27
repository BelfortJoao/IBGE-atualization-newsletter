# external imports
import matplotlib.pyplot as plt


# Data class that stores the data information to plot
class Data:
    """Class data:
    data_x: variable array
    data_y: year array
    titulo: graph title
    var_x: x angle information
    var_y: y angle information.
    Saves the information to plot the IBGE API graphs."""

    # init funciton
    def __init__(self):
        self.data_x = []
        self.data_y = []
        self.titulo = 't'
        self.var_x = 'x'
        self.var_y = 'y'

    # function that extract the data from the json
    def data_api_extrator(self, json):
        self.titulo = json[0]['variavel']
        self.var_x = "ano"
        self.var_y = json[0]['unidade']
        self.data_x = list(json[0]['resultados'][0]['series'][0]['serie'].values())
        self.data_y = list(json[0]['resultados'][0]['series'][0]['serie'].keys())


# function that plot the Data obj into a graph and save it as a png in Images
def data_ploter(data: Data):
    """function that plot the Data obj into a graph and save it as a png in Images"""

    # plot the graph
    fig, axs = plt.subplots(1, 1, figsize=(14, 7))
    axs.plot(data.data_y, data.data_x)
    fig.suptitle(data.titulo)
    name = ''.join(data.titulo)

    # saves the plot as png
    plt.savefig(f'Images/{name}')
