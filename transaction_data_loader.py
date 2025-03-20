from abc import ABC, abstractmethod
from pathlib import Path

import pandas as df


class TransactionDataLoader(ABC):
    def __init__(self, bank_statement_csv: Path):
        self.bank_statement_csv: Path = bank_statement_csv

    @abstractmethod
    def get_transactions(self):
        pass


class IngTransactionDataLoader(TransactionDataLoader):
    def __init__(self, bank_statement_csv: Path):
        super().__init__(bank_statement_csv)

    def load_raw_transactions(self) -> df.DataFrame:
        return df.read_csv(self.bank_statement_csv, sep=";", encoding="cp1250")

    def get_transactions(self):
        pass
