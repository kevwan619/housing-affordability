import pandas as pd



_RENAMED_COLUMNS = {
    "NAME": "msa_name",
    "B25070_001E": "total_households_raw",
    "B25070_002E": "less_than_100",
    "B25070_003E": "100_to_149",
    "B25070_004E": "150_to_199",
    "B25070_005E": "200_to_249",
    "B25070_006E": "250_to_299",
    "B25070_007E": "300_to_349",
    "B25070_008E": "350_to_399",
    "B25070_009E": "400_to_499",
    "B25070_010E": "500_or_more",
    "B25070_011E": "households_not_computed",
    "metropolitan statistical area/micropolitan statistical area": "msa_code"
}




def rename_columns(
	df: pd.DataFrame
) -> pd.DataFrame:

	df = df.rename(columns=_RENAMED_COLUMNS, inplace=False)
	return df



def cast_msa_codes(		# msa_code: int -> str, for subsequent filtering purposes
	df: pd.DataFrame
) -> pd.DataFrame:

	df["msa_code"] = df["msa_code"].astype(str)
	return df



def compute_total(		# compute real total households, delete obfuscated columns
	df: pd.DataFrame
) -> pd.DataFrame:

	df["total_households"] = df["total_households_raw"] - df["households_not_computed"]
	df = df.drop(columns=["total_households_raw", "households_not_computed"], inplace=False)
	return df



def filter_msas(		# filter dataframe to specified list of MSA codes (list defined in notebook)
	df: pd.DataFrame,
	target_msa_codes: list
) -> pd.DataFrame:

	df = df[df["msa_code"].isin(target_msa_codes)]
	return df



def clean_census_data(	# bundles all processes done on a single year's table
	df: pd.DataFrame,
	year: int,
	msa_codes: list
) -> pd.DataFrame:

	df = rename_columns(df)
	df = compute_total(df)
	df = filter_msas(df, msa_codes)
	df["year"] = year

	return df
