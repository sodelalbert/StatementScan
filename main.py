from pathlib import Path

from bank_statement import IngBankStatement
from categories import expense_categories

ing_bs = IngBankStatement(Path("data/2024.csv"), expense_categories)

print(ing_bs.bank_statement_csv_path)
print(ing_bs.expanse_category)
