#!/usr/bin/env python3

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
		return super().__str__()

	def __str__(self) -> str:
		return f"{self.__name__}[name={self.name}, serial={self.serial}, table={self.table}]"
