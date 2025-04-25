from pathlib import Path
from tabulate import tabulate
import pandas as pd


def print_df(df: pd.DataFrame, lines: int = None) -> None:
    """
    Helper funciton to print in readable way dataframes ffor debug purposes.
    """
    if lines is not None:
        print(tabulate(df.head(lines), headers="keys", tablefmt="psql"))
    else:
        print(tabulate(df, headers="keys", tablefmt="psql"))


def get_ing_header_row_index(path: Path, ing_encoding: str) -> int:
    """
    Find Header Row in ING bank statemtnt. This method is used as import
    offset to craeted Pandas DataFrame. Offset should be specified as index
    of NON EMPTY row containing column names.
    """
    header_row_index: int = 0

    with open(path, "r", encoding=ing_encoding) as fp:
        non_empty_index = 0

        for _, line in enumerate(fp.readlines()):
            if line.strip():
                # To find header row use arbitrary column names.
                if (
                    "Data transakcji" in line
                    and "Kwota" in line
                    and "Dane kontrahenta" in line
                ):
                    header_row_index = non_empty_index
                    break
                non_empty_index += 1

    if header_row_index == 0:
        raise ValueError("Header Row not found in the file")

    return header_row_index
