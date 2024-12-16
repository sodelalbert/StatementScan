from pathlib import Path

import pandas as pd  # type: ignore
from tabulate import tabulate  # type: ignore

"""
Millennium and ING are connected together to simplify data loading
Mark necessary accounts and import as CSV form ING Webpage


1. Load Data Transaction List (ING, Millennium) 
2. Sanitize Data - common Data Structure
3. Analyze data with custom criteria 

"""

csv_import = Path("Lista_transakcji_nr_0202026071_161224_ING_MILL.csv")


class TransactionDataProvider:
    """
    Data Provider for Transaction Data from CSV File generated from ING Bank Account

    Millennium and ING are connected together to simplify data loading
    Mark necessary accounts and import as CSV form ING Webpage
    """

    def __init__(self, path: Path):
        self.path: Path = path
        self._encoding: str = "cp1250"
        self._sep: str = ";"
        self._header: int = self._determine_header_row(path)

        self.df = self.load_data()

    def _determine_header_row(self, path: Path) -> int:
        """
        Find Header Row in the CSV File (only non-empty rows are considered)

        If this calculare header row right, data frame will be loaded incorrectly.

        """
        header_row_index: int = 0

        with open(path, 'r', encoding=self._encoding) as fp:
            non_empty_index = 0

            for _, line in enumerate(fp.readlines()):
                if line.strip():
                    if "Data transakcji" in line and "Kwota" in line and "Dane kontrahenta" in line:
                        header_row_index = non_empty_index
                        break
                    non_empty_index += 1

        if header_row_index == 0:
            raise ValueError("Header Row not found in the file")

        return header_row_index

    def load_data(self) -> pd.DataFrame:
        """

        :return:
        """
        df = pd.read_csv(csv_import,
                         encoding=self._encoding,
                         sep=self._sep,
                         header=self._header,
                         # usecols=[0, 2, 3, 5, 8, 9, 15],
                         )

        df.drop(df.tail(1).index, inplace=True)  # drop last row
        df.fillna("", inplace=True)  # fill NaN with empty string

        return df


tdp = TransactionDataProvider(csv_import)
df = tdp.df

print(tabulate(df.head(10), headers='keys'))

# Data types should be justed as well

# Filtering Example

filtered = df[df["Data transakcji"].str.contains("2024-12-01|2024-12-16") == True]
filtered = df[df["Tytuł"].str.contains("włas|Swoje") == True]

print(tabulate(filtered.head(10), headers='keys'))
