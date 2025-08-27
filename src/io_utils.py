import os
from dotenv import load_dotenv
from pathlib import Path

# loads pairs from .env into session environment variables
load_dotenv()

# saves project_root from .env as a path object
PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT"))

DATA_RAW = PROJECT_ROOT / "data_raw"



'''
c = Census(CENSUS_API_KEY)
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

rent_to_income_raw = c.acs1.get(
    variables,
    {'for': 'metropolitan statistical area/micropolitan statistical area:*'},
    year=2023
)
'''

def fetch_census_table(year):


# what i need:
# 1. 