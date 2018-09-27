#! ENV/Scripts/python

from typing import List, Dict, Any, Optional

class Console:
	@classmethod
	def display_heading(cls, text: str):
		size = len(text) + 4
		print("=" * size)
		print(f"  {text}  ")
		print("=" * size)

	@classmethod
	def display_subheading(cls, text: str):
		print(f"  {text}  ")

	@classmethod
	def display(cls, text: str):
		print(text)

	@classmethod
	def display_error(cls, descriptor: str, err: str):
		print(f"{descriptor}: {err}")

	@classmethod
	def display_warning(cls, text: str):
		print(text)

	@classmethod
	def display_item_value(cls, item: str, value: str):
		print(f"{item}: {value}")

	@classmethod
	def display_prompt(cls, text: str) -> str:
		print(text)
		return input(">> ")

	@classmethod
	def display_menu(cls, text: str, items: List[str], exit_text = None, use_subheading = True) -> int:
		if use_subheading:
			cls.display_subheading(text = text)
		else:
			cls.display_heading(text = text)
		if len(items) == 0:
			return 0
		for count in range(0, len(items)):
			cls.display_item_value(item = str(count + 1), value = items[count])
		if exit_text is not None:
			cls.display_item_value(item = "0", value = exit_text)
		try:
			return int(cls.display_prompt(text = "Option"))
		except ValueError as err:
			cls.display_error(descriptor = "Invalid Number", err = err)
			return 0
