# add your code here
# Import Pandas and zip file
import pandas as pd
import zipfile

# Read the zip file
with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
   df = pd.read_csv(zip_ref.open('winemag-data-130k-v2.csv'))

# Group the data by country & calculate the number of reviews and the average points for each country
summary = df.groupby('country')['points'].agg(['count', 'mean']).rename(columns={'count': 'reviews', 'mean': 'points'})

# Round the average points to 1 decimal point
summary['points'] = summary['points'].round(1)

# Write the summary data to a new CSV file.
summary.to_csv('data/reviews-per-country.csv', index=True)
