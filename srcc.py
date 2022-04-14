#!/usr/bin/env python3

import pickle
from scipy import stats

ntk = pickle.load(open("./data/800/ntk.pickle", "rb"))
ntk_change = pickle.load(open("./data/800/ntk_change.pickle", "rb"))
region = pickle.load(open("./data/800/regions.pickle", "rb"))
region_change = pickle.load(open("./data/800/regions_change.pickle", "rb"))
mse = pickle.load(open("./data/800/mse.pickle", "rb"))
mse_change = pickle.load(open("./data/800/mse_change.pickle", "rb"))
accuracy = pickle.load(open("./acc.pickle", "rb"))

del accuracy[120]
del accuracy[2796]

combine = [-ntk[i]+region[i] for i in range(len(ntk))]
start = 0

ntk.extend(pickle.load(open("./data/2700/ntk.pickle", "rb")))
ntk_change.extend(pickle.load(open("./data/2700/ntk_change.pickle", "rb")))
region.extend(pickle.load(open("./data/2700/regions.pickle", "rb")))
region_change.extend(pickle.load(open("./data/2700/regions_change.pickle", "rb")))
mse.extend(pickle.load(open("./data/2700/mse.pickle", "rb")))
mse_change.extend(pickle.load(open("./data/2700/mse_change.pickle", "rb")))


ntk.extend(pickle.load(open("./data/3300/ntk.pickle", "rb")))
ntk_change.extend(pickle.load(open("./data/3300/ntk_change.pickle", "rb")))
region.extend(pickle.load(open("./data/3300/regions.pickle", "rb")))
region_change.extend(pickle.load(open("./data/3300/regions_change.pickle", "rb")))
mse.extend(pickle.load(open("./data/3300/mse.pickle", "rb")))
mse_change.extend(pickle.load(open("./data/3300/mse_change.pickle", "rb")))

print(len(ntk))

print("="*100)
print("Latency SRCC between ntk and accuracy: ", stats.spearmanr(ntk, accuracy[start:start+len(ntk)]))
print("Latency SRCC between ntk_change and accuracy: ", stats.spearmanr(ntk_change, accuracy[start:start+len(ntk)]))
print("Latency SRCC between regions and accuracy: ", stats.spearmanr(region, accuracy[start:start+len(region)]))
print("Latency SRCC between regions_change and accuracy: ", stats.spearmanr(region_change, accuracy[start:start+len(region)]))
print("Latency SRCC between mse and accuracy: ", stats.spearmanr(mse, accuracy[start:start+len(mse)]))
print("Latency SRCC between mse_change and accuracy: ", stats.spearmanr(mse_change, accuracy[start:start+len(mse)]))