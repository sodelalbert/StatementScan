# from dataclasses import dataclass, field
# from typing import Optional
#
# import pandas as pd
#
#
# @dataclass
# class ExpenseCategory:
#     name: str
#     filter: str = field(default=str, repr=False)
#     sum: Optional[float] = field(default=float)
#     data_frame: Optional[pd.DataFrame] = field(default=None, repr=False)
#
#
# expense_category_list = [
#     ExpenseCategory(
#         name="Zakupy spożywcze",
#         filter="LIDL|BIED|ZAB|PIEKARNIA|Zygula|Piekarstwo|CARREFOUR|FAMILIJNA|CENTRUM WINA|NETTO|AUCHAN",
#     ),
#     ExpenseCategory(name="Kosmetyki", filter="ROSSMANN|notino"),
#     ExpenseCategory(
#         name="Restauracje",
#         filter="PIAZZA|COCKPEAT|CHLEBOTEKA|WHISKEYINTHEJAR|TUTTI|NEWPORT CAFE|SHRIMP HOUSE",
#     ),
#     ExpenseCategory(name="Zdrowie", filter="APTEKA|LUX MED|SUPER-PHARM"),
#     ExpenseCategory(
#         name="Transport",
#         filter="SHELL|Myjnia|ORLEN|WROCLAVIA PARKING|Taxi|APCOA|Autopay|STACJA PALIW|CIRCLE K",
#     ),
# ]
from typing import Dict, Set

expense_categories: Dict[str, Set[str]] = {
    "Zakupy spożywcze": {"LIDL", "BIED", "ZAB", "PIEKARNIA", "Zygula", "Piekarstwo",
                         "CARREFOUR", "FAMILIJNA", "CENTRUM WINA", "NETTO", "AUCHAN"},
    "Kosmetyki": {"ROSSMANN", "notino"},
    "Restauracje": {"PIAZZA", "COCKPEAT", "CHLEBOTEKA", "WHISKEYINTHEJAR", "TUTTI",
                    "NEWPORT CAFE", "SHRIMP HOUSE"},
    "Zdrowie": {"APTEKA", "LUX MED", "SUPER-PHARM"},
    "Transport": {"SHELL", "Myjnia", "ORLEN", "WROCLAVIA PARKING", "Taxi", "APCOA",
                  "Autopay", "STACJA PALIW", "CIRCLE K"},
}
