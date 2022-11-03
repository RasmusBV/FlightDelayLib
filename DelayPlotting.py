import pandas as pd
import matplotlib.pylab as plt

def plotKumulativSandsynlighed(forsinkelser: list[pd.Series], grafTitler: list[str], titel: str):
    fig = plt.figure()
    ax = fig.add_subfigure(111)
    ax.set_xlabel('min')
    ax.set_ylabel('Kumulativ Sandsynlighed')
    for i in range(len(forsinkelser)):
        delayList = forsinkelser[i].to_list()
        ax.hist(delayList, label=grafTitler[i], density=True, bins=150, range=(-50, 100), histtype='step', cumulative=True)
    ax.legend(bbox_to_anchor=(0.9,0.3))
    ax.set_title(titel)
    plt.show()


