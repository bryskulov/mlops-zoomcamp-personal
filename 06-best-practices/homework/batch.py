#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pickle
import pandas as pd

TEST_RUN = os.getenv('TEST_RUN', 'False')
S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL', 'http://localhost:4566')
LOCALSTACK_OPTIONS = {
'client_kwargs': {
    'endpoint_url': S3_ENDPOINT_URL
    }
}


def get_input_path(year, month):
    default_input_pattern = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/nyc-tlc/fhv/fhv_tripdata_{year:04d}-{month:02d}.parquet'
    input_pattern = os.getenv('INPUT_FILE_PATTERN', default_input_pattern)
    return input_pattern.format(year=year, month=month)


def get_output_path(year, month):
    default_output_pattern = 's3://nyc-duration/taxi_type=fhv/year={year:04d}/month={month:02d}/predictions.parquet'
    output_pattern = os.getenv('OUTPUT_FILE_PATTERN', default_output_pattern)
    return output_pattern.format(year=year, month=month)


def read_data(filename):
    if TEST_RUN == 'True':
        df = pd.read_parquet('s3://nyc-duration/file.parquet', storage_options=LOCALSTACK_OPTIONS)
        return df
    df = pd.read_parquet(filename)
    return df


def save_data(df_result, output_file):
    if TEST_RUN == 'True':
        df_result.to_parquet(
            's3://nyc-duration/output_file.parquet',
            engine='pyarrow',
            compression=None,
            index=False,
            storage_options=LOCALSTACK_OPTIONS
        )

    df_result.to_parquet(
        output_file, 
        engine='pyarrow', 
        index=False
    )
    

def prepare_data(df, categorical):
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    return df


def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])

    input_file = get_input_path(year, month)
    output_file = get_output_path(year, month)
    
    with open('model.bin', 'rb') as f_in:
        dv, lr = pickle.load(f_in)
    
    
    categorical = ['PUlocationID', 'DOlocationID']

    df = read_data(input_file)
    df = prepare_data(df, categorical)
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)

    print('predicted mean duration:', y_pred.mean())


    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred

    save_data(df_result, output_file=output_file)


if __name__=="__main__":
    main()