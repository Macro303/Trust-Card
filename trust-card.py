#! ENV/Scripts/python

from typing import List, Dict, Any, Optional
import yaml
import os
from data import *

location = "cards\\"
if not os.path.isdir(location):
	os.mkdir(location)

def select_card() -> str:
	found = []
	(_, _, files) = next(os.walk(location))
	for file in files:
		if file[-5:] == ".yaml":
			found.append(file[:-5])
	length = len(found)
	if length < 1:
		return "Default"
	elif length == 1:
		return found[0]
	return found[Console.display_menu(text = "Select Card", items = found) - 1]

def get_card(filename: str) -> Card:
	card = Card(name = "default", serial = 12345, table = ["X" * 10] * 5)
	file = location + filename + ".yaml"
	if os.path.exists(file):
		data = read_yaml(location = file)
		card = Card(name = data["Name"], serial = data["Serial"], table = data["Table"])
	else:
		write_yaml(data = card.to_map(), location = file)
	return card

def write_yaml(data, location):
	with open(location, 'w') as outfile:
		yaml.dump(data, outfile, default_flow_style = False)

def read_yaml(location):
	data_loaded = {}
	with open(location, 'r') as stream:
		data_loaded = yaml.safe_load(stream)
	return data_loaded
	
def get_locations() -> List[str]:
	entry = Console.display_prompt(text = "Enter Locations").upper()
	return [entry[i:i + 2] for i in range(0, len(entry), 2)]

def read_card(card: Card, location: str) -> str:
	try:
		row = int(location[1:]) - 1
		col = ord(location[:1].lower()) - 97
		return card.get_entry(row = row, col = col)
	except ValueError as err:
		Console.display_error(descriptor = "Invalid Location", err = err)
		return str(None)
	
def main():
	card = get_card(filename = select_card())
	Console.display_heading(text = f"{card.name} ({card.serial})")
	locations = get_locations()
	entry = ""
	for location in locations:
		entry += read_card(card = card, location = location)
	Console.display(text = entry)
	input("<Enter> To Exit")

if __name__ == "__main__":
	main()
