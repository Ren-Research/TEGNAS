#!/usr/bin/env python3

import pickle

ntk = pickle.load(open("./data/ntk.pickle", "rb"))
print(len(ntk))