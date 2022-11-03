import pandas as pd
import matplotlib.pylab as plt

def plotKumulativSandsynlighed(forsinkelser: "list[pd.Series]", grafTitler: "list[str]", titel: str, saveLocation = None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('min')
    ax.set_ylabel('Kumulativ Sandsynlighed')
    ax.set_title(titel)
    for i in range(len(forsinkelser)):
        delayList = forsinkelser[i].to_list()
        ax.hist(delayList, label=grafTitler[i], density=True, bins=150, range=(-50, 100), histtype='step', cumulative=True)
    ax.legend(bbox_to_anchor=(0.9,0.3))
    if saveLocation == None:
        plt.show()
    else:
        plt.savefig(f"{saveLocation}/{titel}")

def plotGnsForsinkelse(forsinkelser: "list[pd.Series]", soejleTitler: "list[str]", titel: str, saveLocation = None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel("min")
    gnsForsinkelse = []
    ax.set_title(titel)
    for i in range(len(forsinkelser)):
        positiveForsinkelser = forsinkelser[i][forsinkelser[i] > 0]
        gnsForsinkelse.append(positiveForsinkelser.sum()/forsinkelser[i].size)
    ax.bar(soejleTitler, gnsForsinkelse)
    if saveLocation == None:
        plt.show()
    else:
        plt.savefig(f"{saveLocation}/{titel}")