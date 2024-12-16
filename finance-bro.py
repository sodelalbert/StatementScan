from pathlib import Path

import pandas as pd  # type: ignore
from tabulate import tabulate  # type: ignore

from data_loader import TransactionDataLoader

"""
Task List
1. Load Data Transaction List (ING, Millennium)  | Done
2. Map to correct data Types | Skipped
2. Sanitize Data - common Data Structure
3. Analyze data with custom criteria 

"""

csv_import = Path("Lista_transakcji_nr_0202026071_161224_ING_MILL.csv")

df = TransactionDataLoader(csv_import).get_data()

filtered = df[df['Dane kontrahenta'].str.contains("ZABKA|LIDL|BIEDRONKA") == True]
print(tabulate(filtered.head(10), headers='keys'))
pass

# df = tdl.filter_columns(
#     ['Data transakcji',
#      'Dane kontrahenta',
#      'Tytuł',
#      'Kwota transakcji (waluta rachunku)',
#      'Bank'],
#     exclude_blank_columns=['Data transakcji'])

print(tabulate(df.head(20), headers='keys'))
dict_df = df.to_dict()
pass
# Filtering Example

filtered = df[df["Data transakcji"].str.contains("2024-12-01|2024-12-16") == True]
filtered = df[df["Tytuł"].str.contains("ZABKA|LIDL|BIEDRONKA") == True]
print(tabulate(filtered.head(10), headers='keys'))

pass
