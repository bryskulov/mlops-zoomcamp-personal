import os
from datetime import datetime

import pandas as pd

LOCALSTACK_OPTIONS = {
'client_kwargs': {
    'endpoint_url': 'http://localhost:4566'
    }
}

test_dataframe = pd.read_pickle("test_dataframe.pkl")
test_dataframe.to_parquet(
    's3://nyc-duration/file.parquet',
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=LOCALSTACK_OPTIONS
)

os.system("python batch.py 2021 1")