from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Set

import pandas as pd

from transaction_data_loader import IngTransactionDataLoader


class BankStatement(ABC):
    def __init__(self, bank_statement_csv_path: Path,
                 expanse_category: Dict[str, Set[str]]):
        """
        Bank Statement Data Provider - Abstract Class which will be implemented for specific Bank Statement
        """
        # Bank Statement input file parameters
        self.bank_statement_csv_path: Path = bank_statement_csv_path
        self.expanse_category: Dict[str, Set[str]] = expanse_category

        # Transactions DataFrame
        self.transactions_df: pd.DataFrame

    @abstractmethod
    def save_transactions_csv(self, path: Path):
        """
        Save Transactions to csv file
        """
        pass


class IngBankStatement(BankStatement):
    def save_transactions_csv(self, path: Path):
        pass

    def __init__(self, bank_statement_csv_path: Path,
                 expanse_category: Dict[str, Set[str]]):
        super().__init__(bank_statement_csv_path, expanse_category)

        self.transactions_df = IngTransactionDataLoader(
            bank_statement_csv_path).load_raw_transactions()

    def save_transactions(self, path: Path):
        pass


class MillenniumBankStatement(BankStatement):
    def __init__(self, bank_statement_csv_path: Path,
                 expanse_category: Dict[str, Set[str]]):
        super().__init__(bank_statement_csv_path, expanse_category)

    def save_transactions(self, path: Path):
        pass
