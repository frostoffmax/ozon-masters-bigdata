#!/opt/conda/envs/dsenv/bin/python

from model import fields
import sys
import os
import logging
from joblib import load
import pandas as pd

sys.path.append('.')

#
# Init the logger
#
logging.basicConfig(level=logging.DEBUG)
logging.info("CURRENT_DIR {}".format(os.getcwd()))
logging.info("SCRIPT CALLED AS {}".format(sys.argv[0]))
logging.info("ARGS {}".format(sys.argv[1:]))

# load the model
model = load("0.joblib")

# read and infere
read_opts = dict(
    sep=',', names=fields, index_col=False, header=None,
    iterator=True, chunksize=100
)

for df in pd.read_csv(sys.stdin, **read_opts):
    pred = model.predict(df)
    out = zip(df.doc_id, pred)
    print("\n".join(["{0},{1}".format(*i) for i in out]))
