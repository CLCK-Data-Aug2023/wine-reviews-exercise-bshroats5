import pandas as pd
import zipfile

with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as z:
   with z.open('winemag-data-130k-v2.csv') as f:
       df = pd.read_csv(f)
summary = df.groupby('country').agg({'points': ['count', 'mean']})
summary.columns = ['count', 'points']
summary['points'] = summary['points'].round(1)
summary.to_csv('data/reviews-per-country.csv', index=True)