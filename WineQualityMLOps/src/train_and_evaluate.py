# load train and test
# train algo
# save the metrics and params

import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json

def eval_metrics(actual, pred):
    rmse =  np.round(np.sqrt(mean_squared_error(actual, pred)),3),
    mae =   np.round(mean_absolute_error(actual, pred),3),
    r2  =   np.round(r2_score(actual, pred),3)
    return rmse, mae , r2

def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path =  config['split_data']['train_path']
    test_data_path  =  config['split_data']['test_path']
    random_state    =  config['base']['random_state']
    model_dir       =  config['model_dir']

    alpha = config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio = config['estimators']['ElasticNet']['params']['l1_ratio']

    target = config['base']['target_col']

    train = pd.read_csv(train_data_path, sep=',', encoding='utf-8')
    test = pd.read_csv(test_data_path, sep=',', encoding='utf-8')

    train_y = train[target]
    train_X = train.drop(target, axis=1)

    test_y = test[target]
    test_X = test.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha,
                    l1_ratio=l1_ratio,
                    random_state=random_state
                    )
    lr.fit(train_X, train_y)
    predict = lr.predict(test_X)
    lr.score(test_X, test_y)
    (rmse, mae, r2) = eval_metrics(test_y, predict)

    print(f'RMSE: {rmse}')
    print(f' MAE: {mae}')
    print(f'  R2: {r2}')

    scores_file  =  config['reports']['scores']
    params_file =  config['reports']['params']

    with open(scores_file,'w') as f:
        scores = {
            'RMSE': rmse,
            'MAE' : mae,
            'R2'  : r2
        }
        json.dump(scores, f, indent=4)

    with open(params_file,'w') as f:
        params = {
            'alpha': alpha,
            'l1_ratio': l1_ratio
        }
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir,'model.joblib')

    joblib.dump(lr, model_path)

    





if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args =  args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
