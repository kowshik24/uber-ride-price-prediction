import pickle
import numpy as np
import pandas as pd
import xgboost as xgb

from scripts.data_preprocessor import preprocess_data


def make_single_prediction(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
    # load the model
    model = pickle.load(open('./models/model_xgb.pkl', 'rb'))

    # make a prediction
    data = {'pickup_datetime':pickup_datetime, 'pickup_longitude':pickup_longitude, 'pickup_latitude':pickup_latitude, 'dropoff_longitude':dropoff_longitude, 'dropoff_latitude':dropoff_latitude, 'passenger_count':passenger_count}
    df = pd.DataFrame(data, index=[0])

    # preprocess the data
    df = preprocess_data(df)

    # make prediction
    prediction = model.predict(df)
    return prediction[0]


if __name__ == '__main__':
    pickup_datetime = '2012-04-21 08:30:00'
    pickup_longitude = -73.987130
    pickup_latitude = 40.732029
    dropoff_longitude = -73.991875
    dropoff_latitude = 40.74942
    passenger_count = 1

    prediction = make_single_prediction(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count)
    print(prediction)
