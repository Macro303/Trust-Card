from enum import Enum, unique
from typing import Optional, List

from colorama import init, Style, Fore

init(autoreset=True, convert=True)


@unique
class Colour(Enum):
    BLACK = Style.NORMAL, Fore.BLACK,
    RED = Style.NORMAL, Fore.RED,
    GREEN = Style.NORMAL, Fore.GREEN,
    YELLOW = Style.NORMAL, Fore.YELLOW,
    BLUE = Style.NORMAL, Fore.BLUE,
    MAGENTA = Style.NORMAL, Fore.MAGENTA,
    CYAN = Style.NORMAL, Fore.CYAN,
    WHITE = Style.NORMAL, Fore.WHITE,
    BRIGHT_BLACK = Style.BRIGHT, Fore.BLACK,
    BRIGHT_RED = Style.BRIGHT, Fore.RED,
    BRIGHT_GREEN = Style.BRIGHT, Fore.GREEN,
    BRIGHT_YELLOW = Style.BRIGHT, Fore.YELLOW,
    BRIGHT_BLUE = Style.BRIGHT, Fore.BLUE,
    BRIGHT_MAGENTA = Style.BRIGHT, Fore.MAGENTA,
    BRIGHT_CYAN = Style.BRIGHT, Fore.CYAN,
    BRIGHT_WHITE = Style.BRIGHT, Fore.WHITE

    def __init__(self, style: Style, fore: Fore):
        self.__style = style
        self.__fore = fore

        self.style = style + fore

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.name})"


class Console:
    @classmethod
    def display_heading(cls, heading: str):
        size = len(heading) + 4
        cls.__coloured_print(text='=' * size, colour=Colour.BRIGHT_CYAN)
        cls.__coloured_print(text=f"  {heading}  ", colour=Colour.BRIGHT_CYAN)
        cls.__coloured_print(text='=' * size, colour=Colour.BRIGHT_CYAN)

    @classmethod
    def display(cls, text: str):
        cls.__coloured_print(text=text)

    @classmethod
    def display_error(cls, message: str, err: BaseException):
        cls.__coloured_print(text=f"{message}: ", colour=Colour.BRIGHT_RED, end='')
        cls.__coloured_print(text=str(err), colour=Colour.BRIGHT_YELLOW)

    @classmethod
    def display_item_value(cls, item: str, value: str):
        cls.__coloured_print(text=f"{item}: ", colour=Colour.BRIGHT_BLUE, end='')
        cls.__coloured_print(text=value)

    @classmethod
    def display_prompt(cls, prompt: Optional[str] = None) -> str:
        prompt = f"{prompt}\n>> " if prompt else '>> '
        cls.__coloured_print(text=prompt, colour=Colour.BRIGHT_BLUE, end='')
        return input()

    @classmethod
    def display_menu(cls, heading: str, items: List[str], exit_text: str = None) -> int:
        cls.display_heading(heading=heading)
        if len(items) == 0:
            return 0
        for count in range(0, len(items)):
            cls.display_item_value(item=str(count + 1), value=items[count])
        if exit_text is not None:
            cls.display_item_value(item="0", value=exit_text)
        try:
            return int(cls.display_prompt())
        except ValueError as err:
            cls.display_error(message="Invalid Number", err=err)
            return 0

    @classmethod
    def __coloured_print(cls, text: str, colour: Colour = Colour.BRIGHT_WHITE, end: Optional[str] = None):
        print(f"{colour.style}{text}{Style.RESET_ALL}", end=end)
