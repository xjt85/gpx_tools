import gpxpy
import gpxpy.gpx
import math
import csv
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from pandas.io.json import json_normalize
from datetime import datetime

with open("300км.gpx", "r", encoding="utf-8") as file:
    gpx = gpxpy.parse(file)
data = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            data.append([float(point.latitude), float(point.longitude), float(point.elevation)])


def get_track_distance(data):
    result = 0
    for i in range(len(data) - 1):

        x_diff = round(abs(data[i][0] - data[i + 1][0]) * 111300 * math.cos(data[i][0] / 180 * 3.14), 2)
        y_diff = round(abs(data[i][1] - data[i + 1][1]) * 111000, 2)
        z_diff = round(abs(data[i][2] - data[i + 1][2]), 2)
        # print(f'{x_diff}, {y_diff}, {z_diff}')
        result += math.sqrt(pow(x_diff, 2) + pow(y_diff, 2) + pow(z_diff, 2))
    return round(result, 2)

print(f'Длина трека: {get_track_distance(data)}')

# with open('result.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
#     for row in data:
#         writer.writerow(row)







# with open('../input/strava-dataset-17-06-2022-1321/response.json', 'r', encoding='utf-8') as f:
#     my_dataset = json.load(f)

# df = pd.json_normalize(my_dataset)

# df = df[df['type'] == 'Ride']

# df['start_date_local'] = pd.to_datetime(df['start_date_local'])
# df['start_time'] = df['start_date_local'].dt.time
# df = df.assign(avg_move_spd_kmh=df['average_speed'] * 3.6)
# df = df.assign(avg_total_spd_kmh=df['distance'] / df['elapsed_time'] * 3.6)
# df = df.assign(avg_elev_perc=df['total_elevation_gain'] / df['distance'] * 100)
# df = df.assign(dist_km=df['distance'] / 1000)
# df = df.assign(start_date_r=df.start_date_local.dt.strftime('%d.%m.%Y'))
# df = df.assign(start_my=df.start_date_local.dt.strftime('%Y.%m'))
# df = df.assign(start_time_r=df.start_date_local.dt.strftime('%H:%M'))
# df = df.assign(month=df.start_date_local.dt.month)
# df = df.assign(weekday=df.start_date_local.dt.weekday)
# df = df.fillna(0)
# df['gear_id'] = df['gear_id'].replace(to_replace='b7149139', value='Corratec Corones')
# df['gear_id'] = df['gear_id'].replace(to_replace='b6130097', value='GT Agressor')
# df['gear_id'] = df['gear_id'].replace(to_replace='b8541718', value='Nishiki')
# df['gear_id'] = df['gear_id'].replace(to_replace='b6856164', value='ХВЗ')

# # ------------------------------- вывод данных ------------------------------

# # display(pd.pivot_table(df, index=['id']))

# print(f"Пробег на велосипеде всего: {df['dist_km'].sum().round(1)} км")

# print("")

# print(f"Средняя скорость (только в движении): {df['avg_move_spd_kmh'].mean().round(1)} км/ч")
# print("...в том числе по велосипедам:")
# display(df.groupby('gear_id').agg({'avg_move_spd_kmh':'mean', 'dist_km':'sum'})\
#       .sort_values(by='avg_move_spd_kmh', axis=0, ascending=False)\
#       .rename(columns={'gear_id':'Велосипед', 'avg_move_spd_kmh':'V движ.ср., км/ч','dist_km':'Общий пробег, км'}))

# print("")

# print(f"Средняя скорость (с учетом стоянок): {df['avg_total_spd_kmh'].mean().round(1)} км/ч")
# print("...в том числе по велосипедам:")
# display(df.groupby('gear_id').agg({'avg_total_spd_kmh':'mean', 'dist_km':'sum'})\
#       .sort_values(by='avg_total_spd_kmh', axis=0, ascending=False)\
#       .rename(columns={'gear_id':'Велосипед', 'avg_total_spd_kmh':'V полн. ср., км/ч','dist_km':'Общий пробег, км'}))

# print("")

# print(f"Средний набор высоты: {df['avg_elev_perc'].mean().round(2)} %")
# print("...в том числе по велосипедам:")
# display(df.groupby(['gear_id'])[['gear_id', 'avg_elev_perc']].mean()\
#       .sort_values(by='avg_elev_perc', axis=0, ascending=False)\
#       .rename(columns={'gear_id':'Велосипед', 'avg_elev_perc':'Средн. набор, %'})\
#       .style.format(precision=2))

# print("")

# print(f"Кол-во поездок по дням недели:")
# display(df.groupby(['weekday']).agg({'weekday':'count', 'dist_km':'sum'})\
#       .rename(columns={'weekday':'Кол-во заездов', 'dist_km':'Дистанция, км'})\
#       .style.format(precision=1).background_gradient(cmap='Blues'))

# print("")

# print(f"Пробег по месяцам года:")
# df_moy = df.groupby(['month']).agg({'month':'count', 'dist_km':'sum'})\
#         .rename({'month':'Месяц', 'dist_km':'дистанция, км'})\
        
# display(df_moy.style.format(precision=1).background_gradient(cmap='Blues'))

# df_moy[['month', 'dist_km']].plot(kind="pie", label="", subplots=True)

# print("")

# print(f"Показатели за все время, по месяцам:")
# display(df.groupby(['start_my']).agg({'dist_km':'sum', 'avg_move_spd_kmh':'mean', 'avg_total_spd_kmh':'mean', 'avg_elev_perc':'mean'})\
#         .rename(columns={'start_my':'Месяц', 'dist_km':'Дистанция, км', 'avg_move_spd_kmh':'Vср.движ., км/ч', 'avg_total_spd_kmh':'Vср.полн., км/ч', 'avg_elev_perc':'Средн. набор, %'})\
#         .style.format(precision=1).background_gradient(cmap='Blues'))
              
# print("")

# print(f"Последние {DISPL_COUNT} тренировок:")
# display(df[['name', 'start_date_r', 'start_time_r', 'dist_km', 'avg_move_spd_kmh', 'avg_total_spd_kmh', 'avg_elev_perc']]\
#           .head(DISPL_COUNT)\
#           .rename(columns={'name':'Название', 'start_date_r':'Дата','start_time_r':'Время','dist_km':'Дистанция, км',\
#                  'avg_move_spd_kmh':'V движ.ср., км/ч','avg_total_spd_kmh':'V полн.ср., км/ч','avg_elev_perc':'Средн. набор, %'})\
#           .style.format(precision=1))