import pandas as pd

from dataclasses import dataclass, field
from pathlib import Path
from tabulate import tabulate
from typing import Optional


def print_df(df: pd.DataFrame, lines: int = None) -> None:
    if lines is not None:
        print(tabulate(df.head(lines), headers="keys", tablefmt="psql"))
    else:
        print(tabulate(df, headers="keys", tablefmt="psql"))


@dataclass
class ExpenseCategory:
    name: str
    filter: str = field(default=str, repr=False)
    sum: Optional[float] = field(default=float)
    data_frame: Optional[pd.DataFrame] = field(default=None, repr=False)


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

        with open(path, "r", encoding=self._encoding) as fp:
            non_empty_index = 0

            for _, line in enumerate(fp.readlines()):
                if line.strip():
                    if (
                        "Data transakcji" in line
                        and "Kwota" in line
                        and "Dane kontrahenta" in line
                    ):  # Arbitrary check
                        header_row_index = non_empty_index
                        break
                    non_empty_index += 1

        if header_row_index == 0:
            raise ValueError("Header Row not found in the file")

        return header_row_index

    def get_data(self) -> pd.DataFrame:

        df = pd.read_csv(
            self.path,
            encoding=self._encoding,
            sep=self._sep,
            header=self._header_index,
        )

        # Drop last row
        df.drop(df.tail(1).index, inplace=True)

        # Set Data Types for Columns
        float_columns = [
            "Kwota transakcji (waluta rachunku)",
            "Kwota blokady/zwolnienie blokady",
            "Saldo po transakcji",
        ]
        for col in float_columns:
            df[col] = df[col].str.replace(",", ".").astype(float)

        # Set coherent column meaning for Millennium and ING by copying data from 'Tytuł' to 'Dane kontrahenta'
        df["Dane kontrahenta"] = df.apply(
            lambda row: (
                row["Tytuł"]
                if row["Dane kontrahenta"] == "  "
                else row["Dane kontrahenta"]
            ),
            axis=1,
        )

        # If Data transakcji is  empty, fill it with Data księgowania
        df.loc[
            df["Kwota transakcji (waluta rachunku)"].isna(),
            "Kwota transakcji (waluta rachunku)",
        ] = df["Kwota blokady/zwolnienie blokady"]

        # For all blocked transactions fill the Kwota transakcji with tha blocked amount.
        df.loc[df["Data transakcji"].isna(), "Data transakcji"] = df["Data księgowania"]

        return df
