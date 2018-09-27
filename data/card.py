#! ENV/Scripts/python

from typing import List, Dict, Any, Optional

class Card:
	def __init__(self, name: str, serial: int, table: List[str]):
		self.name = name
		self.serial = serial
		self.table = table
		
	def get_entry(self, row: int, col: int) -> str:
		try:
			return str(self.table[row][col])
		except IndexError as err:
			return str(None)
		
	def to_map(self) -> Dict[str, Any]:
		return {"Name": self.name, "Serial": self.serial, "Table": self.table}
		