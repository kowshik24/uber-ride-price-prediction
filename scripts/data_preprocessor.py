import pandas as pd
import numpy as np
import datetime as dt
from geopy.distance import geodesic


def calculate_distance(x):
    return geodesic((x['pickup_latitude'], x['pickup_longitude']), (x['dropoff_latitude'], x['dropoff_longitude'])).km


def preprocess_data(df):
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['distance'] = df.apply(lambda x: calculate_distance(x), axis=1)
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day'] = df['pickup_datetime'].dt.day
    df['month'] = df['pickup_datetime'].dt.month
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x > 4 else 0)
    df['is_rush_hour'] = df['hour'].apply(lambda x: 1 if x in [7,8,9,16,17,18] else 0)
    df.drop(['pickup_datetime'],axis=1,inplace=True)
    return df

if __name__ == '__main__':
    pickup_datetime = '2012-04-21 08:30:00'
    pickup_longitude = -73.987130
    pickup_latitude = 40.732029
    dropoff_longitude = -73.991875
    dropoff_latitude = 40.74942
    passenger_count = 1

    # need to make this: pickup_longitude	pickup_latitude	dropoff_longitude	dropoff_latitude	passenger_count	distance	hour	day	month	day_of_week	is_weekend	is_rush_hour
    data = {'pickup_datetime':pickup_datetime, 'pickup_longitude':pickup_longitude, 'pickup_latitude':pickup_latitude, 'dropoff_longitude':dropoff_longitude, 'dropoff_latitude':dropoff_latitude, 'passenger_count':passenger_count}
    df = pd.DataFrame(data, index=[0])

    df = preprocess_data(df)
    print(df)