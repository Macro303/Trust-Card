#!/usr/bin/env python3

import os
from typing import List, Dict, Any

import yaml

from data import *

LOCATION = "cards"
if not os.path.isdir(LOCATION):
	os.mkdir(LOCATION)
DEFAULT = Card(name="Default", serial=12345, table=["X" * 10] * 5)


def select_card() -> Card:
	found = []
	(_, _, files) = next(os.walk(LOCATION))
	for file in files:
		if file[-5:] == ".yaml":
			found.append(get_card(file[:-5]))
	length = len(found)
	if length > 1:
		return found[Console.display_menu(heading="Select Card", items=[x.name for x in found]) - 1]
	elif length == 1:
		return found[0]
	write_yaml(data=DEFAULT.to_map(), file=os.path.join(LOCATION, "Default.yaml"))
	return DEFAULT


def get_card(filename: str) -> Card:
	file = os.path.join(LOCATION, filename + ".yaml")
	if os.path.exists(file):
		data = read_yaml(file=file)
		return Card(name=data["Name"], serial=data["Serial"], table=data["Table"])
	else:
		write_yaml(data=DEFAULT.to_map(), file=file)
	return DEFAULT


def write_yaml(data: Dict[str, Any], file):
	with open(file, 'w') as outfile:
		yaml.dump(data, outfile, default_flow_style=False)


def read_yaml(file) -> Dict[str, Any]:
	with open(file, 'r') as stream:
		data_loaded = yaml.safe_load(stream)
	return data_loaded


def input_selections() -> List[str]:
	entry = Console.display_prompt(prompt="Enter the Challenge Co-ordinates").upper()
	return [entry[i:i + 2] for i in range(0, len(entry), 2)]


def read_card(selected: Card, location: str) -> str:
	try:
		row = int(location[1:]) - 1
		col = ord(location[:1].lower()) - 97
		return selected.get_entry(row=row, col=col)
	except ValueError as err:
		Console.display_error(descriptor="Invalid Co-ordinates", err=err)
		return str(None)


def main():
	selected = select_card()
	Console.display_heading(title=f"{selected.name} ({selected.serial})")
	locations = input_selections()
	entry = ""
	for location in locations:
		entry += read_card(selected=selected, location=location)
	Console.display(text=f"Challenge Response: {entry}")
	input("<Enter> To Exit")


if __name__ == "__main__":
	main()
