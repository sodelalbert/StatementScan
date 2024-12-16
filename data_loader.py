from pathlib import Path

import pandas as pd  # type: ignore
from tabulate import tabulate  # type: ignore


class TransactionDataLoader:
    """
    Data Provider for Transaction Data from CSV File generated from ING Bank Account

    Millennium and ING are connected together to simplify data loading
    Mark necessary accounts and import as CSV form ING Webpage
    """

    def __init__(self, path: Path):
        self.path: Path = path
        self._encoding: str = "cp1250"
        self._sep: str = ";"
        self._header_index: int = self._get_header_row_index(path)

    def _get_header_row_index(self, path: Path) -> int:
        """
        Find Header Row in the CSV File (only non-empty rows are considered)

        If this calculates header row right, data frame will be loaded incorrectly.

        """
        header_row_index: int = 0

        with open(path, 'r', encoding=self._encoding) as fp:
            non_empty_index = 0

            for _, line in enumerate(fp.readlines()):
                if line.strip():
                    if "Data transakcji" in line and "Kwota" in line and "Dane kontrahenta" in line:  # Arbitrary check
                        header_row_index = non_empty_index
                        break
                    non_empty_index += 1

        if header_row_index == 0:
            raise ValueError("Header Row not found in the file")

        return header_row_index

    def get_data(self) -> pd.DataFrame:

        df = pd.read_csv(self.path,
                         encoding=self._encoding,
                         sep=self._sep,
                         header=self._header_index,
                         )

        df.drop(df.tail(1).index, inplace=True)  # drop last row

        # Set Data Types for Columns
        float_columns = ['Kwota transakcji (waluta rachunku)',
                         "Kwota blokady/zwolnienie blokady",
                         'Saldo po transakcji']
        for col in float_columns:
            df[col] = df[col].str.replace(',', '.').astype(float)

        # Set coherent column meaning for Millennium and ING
        df['Dane kontrahenta'] = df.apply(
            lambda row: row['Tytuł'] if row['Dane kontrahenta'] == '  ' else row[
                'Dane kontrahenta'], axis=1)

        return df
