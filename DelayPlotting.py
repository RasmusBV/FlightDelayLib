import pandas as pd
import matplotlib.pylab as plt
import numpy as np

def plotKumulativSandsynlighed(forsinkelser: "list[pd.Series]", grafTitler: "list[str]", titel: str):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('min')
    ax.set_ylabel('Kumulativ Sandsynlighed')
    ax.set_title(titel)
    histogrammer: "list[tuple[list[list[float]], list[float], pd.BarContainer | list]]" = []
    for i in range(len(forsinkelser)):
        delayList = forsinkelser[i].to_list()
        density, bins = np.histogram(delayList, density=True, bins=150, range=(-20, 100))
        unity_density = density / density.sum()
        unity_density = np.cumsum(unity_density)
        ax.plot(bins[1:], unity_density, label = grafTitler[i])
    ax.legend(bbox_to_anchor=(0.9,0.3))
    return histogrammer

def plotGnsForsinkelse(forsinkelser: "list[pd.Series]", soejleTitler: "list[str]", titel: str):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel("min")
    gnsForsinkelse = []
    ax.set_title(titel)
    for i in range(len(forsinkelser)):
        positiveForsinkelser = forsinkelser[i][forsinkelser[i] > 0]
        gnsForsinkelse.append(positiveForsinkelser.sum()/forsinkelser[i].size)
    ax.bar(soejleTitler, gnsForsinkelse)
    return soejleTitler, gnsForsinkelse

def plotKumulativSandsynlighedForskel(forsinkelse1: pd.Series, grafTitel1: str, forsinkelse2: pd.Series, grafTitel2: str):
    histogrammer = plotKumulativSandsynlighed([forsinkelse1, forsinkelse2], ["a", "b"], "b")
    plt.clf()
    forskel = np.divide(histogrammer[0][0], histogrammer[1][0])
    titel = f"{grafTitel1} i forhold til {grafTitel2}"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("min")
    ax.set_ylabel("Forskel i Komulativ Sandsynlighed")
    ax.set_title(titel)
    ax.plot(histogrammer[0][1][1:], forskel)
    return forskel, titel