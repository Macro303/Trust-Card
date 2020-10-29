from typing import List, Dict, Any


class Card:
    def __init__(self, name: str, serial: int, table: List[str]):
        self.name = name
        self.serial = serial
        self.table = table

    def get_entry(self, row: int, col: int) -> str:
        try:
            return str(self.table[row][col])
        except IndexError:
            return str(None)

    def to_map(self) -> Dict[str, Any]:
        return {"Name": self.name, "Serial": self.serial, "Table": self.table}

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        fields = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                value = f"'{value}'"
            fields.append(f"{key}={value}")
        return f"{type(self).__name__}[{', '.join(fields)}]"
