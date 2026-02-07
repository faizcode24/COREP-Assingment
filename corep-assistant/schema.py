from pydantic import BaseModel
from typing import List

class CorepField(BaseModel):
    row: str
    column: str
    label: str
    value: float
    justification: List[str]

class CorepReport(BaseModel):
    template: str
    fields: List[CorepField]

    def validate_report(self):
        errors = []
        total = sum(f.value for f in self.fields)
        if total < 0:
            errors.append("CET1 capital cannot be negative")

        for f in self.fields:
            if "deduction" in f.label.lower() and f.value > 0:
                errors.append(f"Row {f.row} must be negative")

        return errors
