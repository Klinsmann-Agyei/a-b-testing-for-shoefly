import codecademylib
import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
print(ad_clicks.groupby('utm_source').user_id.count().reset_index())
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())
ad_clicks.groupby('experimental_group').user_id.count().reset_index().pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
a_click_pivot = a_clicks.groupby('is_click', 'day').user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()
a_click_pivot['percent_clicked'] = a_click_pivot[True]/(a_click_pivot[True] + a_click_pivot[False])

b_click_pivot = b_clicks.groupby('is_click', 'day').user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()
b_click_pivot['percent_clicked'] = b_click_pivot[True]/(b_click_pivot[True] + b_click_pivot[False])
