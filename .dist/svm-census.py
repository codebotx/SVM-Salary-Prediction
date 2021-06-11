import pandas as pd
import numpy as np

original_data=pd.read_csv(
	"adult.csv",
	names=[

"Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Marital Status",
"Occupation", "Relationship", "Race", "Gender", "Capital Gain", "Capital Loss",
"Hours per week", "Country", "Target"],
sep=r'\s*, \s*',
engine='python',
na_values="?")
print(original_data.head())