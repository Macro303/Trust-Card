# Trust Card
[![Version](https://img.shields.io/github/tag-pre/Macro303/Trust-Card.svg?label=version&style=flat-square)](https://github.com/Macro303/Trust-Card/releases)
[![Issues](https://img.shields.io/github/issues/Macro303/Trust-Card.svg?style=flat-square)](https://github.com/Macro303/Trust-Card/issues)
[![Contributors](https://img.shields.io/github/contributors/Macro303/Trust-Card.svg?style=flat-square)](https://github.com/Macro303/Trust-Card/graphs/contributors)
[![Visits](https://badges.pufler.dev/visits/Macro303/Trust-Card?style=flat-square)](https://badges.pufler.dev)
[![License](https://img.shields.io/github/license/Macro303/Trust-Card.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Simple script to help you manage and use your Trust/Challenge cards

## Built Using
 - [Python: 3.9.0](https://www.python.org/)
 - [Colorama: 0.4.4](https://pypi.org/project/colorama/)
 - [PyYaml: 5.3.1](https://pypi.org/project/PyYaml/)
 - [PyInstaller: 4.0](https://pypi.org/project/PyInstaller/)

## Execution
 1. Clone repo
 2. Execute `python setup.py install` to install dependencies
 3. Execute `python trust-card.py`
 
## Release
 1. Clone repo
 2. Execute `python setup.py install` to install dependencies
 4. Execute `pyinstaller --onefile trust-card.py` to create the executable
 5. Navigate to the **dist** folder to find the OS specific executable
 
## Notes
 - A **cards** folder will be created if it doesn't exist
 - Store all your cards inside the **cards** folder as _yaml_ files, use the _default.yaml_ as an example
 - For each _yaml_ file in the cards folder Trust Card will try and load it as usable card
 - If you have more than one card, you will be asked on startup to select your card
