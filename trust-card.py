from pathlib import Path
from typing import List, Dict, Any

import yaml

from data import *

LOCATION = Path(__file__).resolve().parent.joinpath('cards')
if not LOCATION.exists():
    LOCATION.mkdir()
DEFAULT = Card(name='Default', serial=12345, table=["X" * 10] * 5)


def select_card() -> Card:
    files = [temp for temp in LOCATION.iterdir() if temp.is_file() and temp.name.endswith('.yaml')]
    found = [get_card(temp) for temp in files]
    if len(found) == 1:
        return found[0]
    elif len(found) > 1:
        return found[Console.display_menu(heading='Select Card', items=[x.name for x in found]) - 1]
    write_yaml(data=DEFAULT.to_map(), file=LOCATION.joinpath('Default.yaml'))
    return DEFAULT


def get_card(file: Path) -> Card:
    data = read_yaml(file=file)
    return Card(name=data['Name'], serial=data['Serial'], table=data['Table'])


def write_yaml(data: Dict[str, Any], file: Path):
    with open(file, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def read_yaml(file: Path) -> Dict[str, Any]:
    with open(file, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded or {}


def input_selections() -> List[str]:
    entry = Console.display_prompt(prompt='Enter the Challenge Co-ordinates').upper()
    return [entry[i:i + 2] for i in range(0, len(entry), 2)]


def read_card(selected: Card, location: str) -> str:
    try:
        row = int(location[1:]) - 1
        col = ord(location[:1].lower()) - 97
        return selected.get_entry(row=row, col=col)
    except ValueError as err:
        Console.display_error(message='Invalid Co-ordinates', err=err)
        return str(None)


def main():
    selected = select_card()
    Console.display_heading(heading=f"{selected.name} ({selected.serial})")
    locations = input_selections()
    entry = ''
    for location in locations:
        entry += read_card(selected=selected, location=location)
    Console.display(text=f"Challenge Response: {entry}")
    input('<Enter> To Exit')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
