# Trust Card
![Version](https://img.shields.io/github/tag/Macro303/Trust-Card.svg?label=version)
![Issues](https://img.shields.io/github/issues/Macro303/Trust-Card.svg?label=issues)
![Contributors](https://img.shields.io/github/contributors/Macro303/Trust-Card.svg?label=contributors)
![License](https://img.shields.io/github/license/Macro303/Trust-Card.svg?=label=license)

_Description_ **[WIP]**

## Dependencies
 - Python 3.7
 - PyYaml >= 4.0.0

## Execution
 1. Clone repo
 2. Execute `python setup.py install` to install dependencies
 3. Execute `python trust-card.py`
 
## Release
 1. Clone repo
 2. Execute `python setup.py install` to install dependencies
 3. Execute `pip install pyinstaller`
 4. Execute `pyinstaller --onefile trust-card.py` to create the executable
 5. Navigate to the **dist** folder to find the OS specific executable
 
## Usage
 - A **cards** folder will be created if it doesn't exist
 - Store all your cards inside the **cards** folder as _yaml_ files, use the _default.yaml_ as an example
 - For each _yaml_ file in the cards folder Trust Card will try and load it as usable card
 - If you have more than one card, you will be asked on startup to select your card
