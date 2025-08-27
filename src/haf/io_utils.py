import os
from dotenv import load_dotenv
from pathlib import Path
from census import Census # delete this later maybe?
import pandas as pd


def fetch_census_table(
	api_key: str,
	vars: list,
	geo: str,
	year: int,
	file_path: Path
) -> None:

	if file_path.exists(): # raw CSV already exists, do nothing
		print(f"Data already exists at {file_path} -- nothing changed")

	else: # fetch census table and save to path
		c = Census(api_key)
		data = c.acs1.get(vars, {'for': geo}, year)

		df = pd.DataFrame(data)				# census table -> pandas dataframe
		df.to_csv(file_path, index=False)	# pandas dataframe -> raw CSV
		print(f"Data table successfully saved at {file_path}")



def check_table(
	file_path: Path
) -> pd.DataFrame:

	df = pd.read_csv(file_path)
	return df
