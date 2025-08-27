import os
from dotenv import load_dotenv
from pathlib import Path
from census import Census # delete this later maybe?
import pandas as pd

# loads pairs from .env into session environment variables
load_dotenv()

CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

# saves project_root from .env as a path object
PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT"))

# DATA_RAW = PROJECT_ROOT / "data_raw"


'''
rent_to_income_raw = c.acs1.get(
    variables,
    {'for': 'metropolitan statistical area/micropolitan statistical area:*'},
    year=2023
)
'''

# eventually this goes into notebook: REMOVE BELOW
variables = (
    "NAME",
    "B25070_001E",  # Total
    "B25070_002E",  # Less than 10.0
    "B25070_003E",  # 10.0 to 14.9
    "B25070_004E",  # 15.0 to 19.9
    "B25070_005E",  # 20.0 to 24.9
    "B25070_006E",  # 25.0 to 29.9
    "B25070_007E",  # 30.0 to 34.9
    "B25070_008E",  # 35.0 to 39.9
    "B25070_009E",  # 40.0 to 49.9
    "B25070_010E",  # 50.0 or more
    "B25070_011E"   # Not computed
)
geography = "metropolitan statistical area/micropolitan statistical area:*"
c = Census(CENSUS_API_KEY)
# REMOVE ABOVE

def fetch_census_table(var_table, geo, year):

	file_path = PROJECT_ROOT / "data_raw" / f"B25070_{year}.csv"
	print(file_path)

	if file_path.exists():
		print("file exists")
	else: # fetch census data and save
		data = c.acs1.get(var_table, {'for': geo}, year)
		df = pd.DataFrame(data)
		print(df.head())
		df.to_csv(file_path)

		
def test_function():
	print("test function!")


fetch_census_table(variables, geography, 2016)


'''
NEXT STEPS:

write function for fetch_census_table
check if file exists first:
	/data_raw/B25070_(year).csv
if it does exist, then nothing needs to be done, print something
if it does not exist, then execute the fetch
in the main notebook file, run fetch_census_table for each year

for example:
for years 2015 - 2023:
	fetch_census_table(year)
'''