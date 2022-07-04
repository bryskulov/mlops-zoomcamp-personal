import pickle
import argparse
from pickletools import float8

import pandas as pd


def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df


def df_transform(df, year, month):
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    dicts = df[categorical].to_dict(orient='records')
    return dicts


def df_predict(dicts, dv, lr):
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)
    return y_pred


def save_results(df, y_pred, output_file):
    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred

    df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Computes ride duration.")
    parser.add_argument("year", help="Year of trip data", default=None, type=int)
    parser.add_argument("month", help="Month of trip data", default=None, type=int)
    args = parser.parse_args()

    with open('model.bin', 'rb') as f_in:
        dv, lr = pickle.load(f_in)

    categorical = ['PUlocationID', 'DOlocationID']

    input_file = f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{args.year:04d}-{args.month:02d}.parquet'
    output_file = f'output/fhv_tripdata_{args.year:04d}-{args.month:02d}.parquet'

    df = read_data(input_file)
    dicts = df_transform(df, args.year, args.month)
    y_pred = df_predict(dicts, dv, lr)
    print(y_pred.mean())
    save_results(df, y_pred, output_file)
