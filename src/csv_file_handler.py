import csv
from typing import List, Dict


class CSVFileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def write_row(self, row: Dict):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())
            writer.writerow(row)

    def read_all_rows(self) -> List[Dict]:
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
