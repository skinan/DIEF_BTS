This repo is under construction.

# Building Timeseries Dataset

![gray concrete building covered trees](danist-soh-dqXiw7nCb9Q-unsplash.jpg)

Photo by <a href="https://unsplash.com/@danist07?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Danist Soh</a> on <a href="https://unsplash.com/photos/gray-concrete-building-covered-trees-dqXiw7nCb9Q?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

This is the primary repo to access the dataset.

This is part of the NSW, Australia Digital Infrastructure Energy Flexibility (DIEF) project: https://research.csiro.au/dch/projects/nsw-dief/ 

# Abstract

Buildings play a crucial role in human well-being, influencing occupant comfort, health, and safety. Additionally, they contribute significantly to global energy consumption, accounting for one-third of total energy usage, and carbon emissions. Optimizing building performance presents a vital opportunity to combat climate change and promote human flourishing.
However, research in building analytics has been hampered by the lack of publicly available datasets. Existing datasets are often limited in scope or based on simulations. In this paper, we introduce the first real-world dataset addressing this gap. Our dataset covers three buildings over a three-year period, comprising more than ten thousand timeseries data points with hundreds of unique ontologies. Moreover, the metadata is standardized using the BRICK schema.
To demonstrate the utility of this dataset, we performed benchmarks on two tasks: timeseries ontology classification and zero-shot forecasting.
These tasks represent an essential initial step in ensuring that analytics solutions developed for one building / on public datasets, will maintain performance on new buildings without re-training.

# Dataset

## Access

https://figshare.com/s/b73df11bb4979e46267e

DOI: 10.6084/m9.figshare.25912180

Note that, as of now, only the training data are made publicly available as we are planning to host a competition using this dataset.

## Files description

List of files available now:
* `train.zip` is the raw time series data. This is a zip of a folder of [`pickle`](https://docs.python.org/3/library/pickle.html) file. Inside each pickle file is a NumPy array with dimension [2,n] where `n` is the number of timesteps. The first row is the timestamp and the second row is the value.
* `Site_B.ttl` is the turtle file that contains the metadata of Site B using the [Brick schema](https://brickschema.org).
* `mapper_TrainOnly.csv` contains the information that maps the timeseries filenames in `train.zip` to the `StreamID` in `Site_B.ttl`. Some buildings in `train.zip` are from Site A and the brick schema is not yet made available. This is on purpose.
* `train_X.zip` and `train_Y.csv` are generated from `train.zip` using the function in the `xySplit.py` file.
* `train_Y.csv` see above.


List of files that will be made available after the competitions:
* `test.zip`
* `Site_A.ttl`
* `Site_C.ttl`
* `mapper.csv`

# Code

The `20240530_class_code` folder contains the code to reproduce the classifications results.
Here is a short description of each file:

* `requirement.txt` **is coming**, but all the information are already available in `e12_pbs_py.sh.o116050675`.
* `xySplit.py` Use this to split `train.zip` to `train_X.zip` and `train_Y.csv`.
* `e05_naieve_02.ipynb` Run this notebok to get the naieve results.
* `e07_02_LR.ipynb` Run this notebook to get the Logistic Regression results.
* `e08_02_RF.ipynb` Run thus notebook to get the Random Forest results.
* `e09_01_XGBoost.ipynb` Run this notebook to get the XGBoost results.
* `thuml_tslib_dief` This folder contains the **modified** library from Tsinghua University Machine Learning Group's library: https://github.com/thuml/Time-Series-Library
* `e12_pbs_py.sh` This is the setup to run the `Transformer` model.
* `e12_pbs_py.sh.o116050675` This is the output of the above setup. It contains detailed information about installed Python packages, their version, as well as the hardware specifications.
* `e13_pbs_py.sh` `DLinear`
* `e15_pbs_py.sh` `PatchTST`
* `e17_pbs_py.sh` `Informer`

