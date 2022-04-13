#!/usr/bin/env python3

import pickle
from scipy import stats

ntk = pickle.load(open("./data/ntk.pickle", "rb"))
ntk_change = pickle.load(open("./data/ntk_change.pickle", "rb"))
region = pickle.load(open("./data/regions.pickle", "rb"))
region_change = pickle.load(open("./data/regions_change.pickle", "rb"))
mse = pickle.load(open("./data/mse.pickle", "rb"))
mse_change = pickle.load(open("./data/mse_change.pickle", "rb"))
accuracy = pickle.load(open("./acc.pickle", "rb"))
del accuracy[105]

combine = [-ntk[i]+region[i] for i in range(len(ntk))]

print("="*100)
print("Latency SRCC between ntk and accuracy: ", stats.spearmanr(ntk, accuracy[:len(ntk)]))
print("Latency SRCC between ntk_change and accuracy: ", stats.spearmanr(ntk_change, accuracy[:len(ntk)]))
print("Latency SRCC between regions and accuracy: ", stats.spearmanr(region, accuracy[:len(region)]))
print("Latency SRCC between regions_change and accuracy: ", stats.spearmanr(region_change, accuracy[:len(region)]))
print("Latency SRCC between mse and accuracy: ", stats.spearmanr(mse, accuracy[:len(mse)]))
print("Latency SRCC between mse_change and accuracy: ", stats.spearmanr(mse_change, accuracy[:len(mse)]))

print("Latency SRCC between combine and accuracy: ", stats.spearmanr(combine, accuracy[:len(region)]))