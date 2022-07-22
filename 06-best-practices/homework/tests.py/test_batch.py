from datetime import datetime

import pandas as pd

import batch

def dt(hour, minute, second=0):
    return datetime(2021, 1, 1, hour, minute, second)

def test_prepare_data():

    df = pd.read_pickle("test_dataframe.pkl")

    categorical = ['PUlocationID', 'DOlocationID']
    actual_df = batch.prepare_data(df, categorical=categorical)

    expected_df = pd.DataFrame(data={
        'PUlocationID': [str(-1), str(1)],
        'DOlocationID': [str(-1), str(1)],
        'pickup_datetime': [dt(1, 2), dt(1, 2)],
        'dropOff_datetime': [dt(1, 10), dt(1, 10)],
        'duration': [8.0, 8.0]},
    )

    pd.testing.assert_frame_equal(actual_df, expected_df, rtol=1e-05)