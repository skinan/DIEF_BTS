import os
import numpy as np
import pandas as pd
import tqdm
import scipy
import pickle

def load_X(pathData):
    n_ts = 0
    for ifilename in os.listdir(pathData):
        if ifilename[-4:] != '.pkl':
            continue
        n_ts += 1
    # load the data
    l_dir = os.listdir(pathData)
    for ii in tqdm(range(n_ts)):
        ifilename = l_dir[ii]
        if ifilename[-4:] != '.pkl':
            continue
        with open(pathData+ifilename, 'rb') as f:
            idata = pickle.load(f)