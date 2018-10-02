#!/usr/bin/env python3

from enum import Enum, unique

from colorama import init

init(autoreset=True, convert=True)


@unique
class Colour(Enum):
	RESET = 1
	BLACK = 2
	RED = 3
	GREEN = 4
	YELLOW = 5
	BLUE = 6
	MAGENTA = 7
	CYAN = 8
	WHITE = 9

	def get_ansi(self) -> str:
		if self.value == 2:
			return "\u001B[30m"
		if self.value == 3:
			return "\u001B[31m"
		if self.value == 4:
			return "\u001B[32m"
		if self.value == 5:
			return "\u001B[33m"
		if self.value == 6:
			return "\u001B[34m"
		if self.value == 7:
			return "\u001B[35m"
		if self.value == 8:
			return "\u001B[36m"
		if self.value == 9:
			return "\u001B[37m"
		return "\u001B[0m"


class Console:
	heading = Colour.CYAN
	highlight = Colour.MAGENTA
	error = Colour.RED
	warning = Colour.YELLOW
	standard = Colour.WHITE
	input_colour = Colour.GREEN
	ignore = Colour.BLUE

	@classmethod
	def display_heading(cls, title: str):
		size = len(title) + 4
		cls.__colour_console("=" * size, Console.heading)
		cls.__colour_console(f"  {title}  ", Console.heading)
		cls.__colour_console("=" * size, Console.heading)

	@classmethod
	def display_subheading(cls, title: str):
		cls.__colour_console(title, Console.heading)

	@classmethod
	def display_old_new(cls, old: str, new: str):
		cls.__colour_console(old, Console.standard, False)
		cls.__colour_console(" --> ", Console.highlight, False)
		cls.display(new)

	@classmethod
	def display(cls, text: str):
		cls.__colour_console(text, Console.standard)

	@classmethod
	def display_highlight(cls, text: str):
		cls.__colour_console(text, Console.highlight)

	@classmethod
	def display_ignored(cls, text: str):
		cls.__colour_console(text, Console.ignore)

	@classmethod
	def display_error(cls, descriptor: str, err: BaseException):
		cls.__colour_console(descriptor + ": ", Console.error, False)
		cls.display_warning(str(err))

	@classmethod
	def display_warning(cls, text: str):
		cls.__colour_console(text, Console.warning)

	@classmethod
	def display_item_value(cls, item: str, value: str):
		cls.__colour_console(item + ": ", Console.highlight, False)
		cls.display(value)

	@classmethod
	def display_prompt(cls, prompt: str) -> str:
		cls.__colour_console(prompt, Console.input_colour)
		entry = input(Console.input_colour.get_ansi() + ">> ")
		print("", end="")
		return entry

	@classmethod
	def display_menu(cls, heading: str, items, exit_text=None) -> int:
		cls.display_heading(heading)
		if len(items) == 0:
			return 0
		for count in range(0, len(items)):
			cls.display_item_value(str(count + 1), items[count])
		if exit_text is not None:
			cls.display_item_value("0", exit_text)
		try:
			return int(cls.display_prompt("Option"))
		except ValueError as err:
			cls.display_error("Invalid Number", err)
			return 0

	@staticmethod
	def __colour_console(text: str, colour, new_line=True):
		print(colour.get_ansi() + str(text), end="\n" if new_line else "")
