# Read the data from the data source
# save it in the data/raw for further process
import os
import yaml
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [column.replace(' ', '_') for column in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path, sep=',',index=False, header=new_cols)
    print(df.head())
    return df
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    print(parsed_args.config)
    load_and_save(config_path=parsed_args.config)