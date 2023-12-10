# add your code here
# Import Pandas and zip file
import pandas as pd
import zipfile

# Read the zip file
with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
   df = pd.read_csv(zip_ref.open('winemag-data-130k-v2.csv'))

