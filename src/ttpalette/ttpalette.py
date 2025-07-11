class Color:
    """
    A class to represent ANSI color codes for text foreground.

    Attributes:
    - BLACK: ANSI escape code for black text
    - RED: ANSI escape code for red text
    - GREEN: ANSI escape code for green text
    - YELLOW: ANSI escape code for yellow text
    - BLUE: ANSI escape code for blue text
    - MAGENTA: ANSI escape code for magenta text
    - CYAN: ANSI escape code for cyan text
    - WHITE: ANSI escape code for white text
    - RESET: ANSI escape code to reset text color to default

    Methods:
    - custom(id): Returns a custom ANSI escape code based on the given color ID.
    - list_custom_colors(): Prints a list of custom colors with their IDs.
    """

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    
    def custom(id):
        """
        Returns a custom ANSI escape code based on the given color ID.

        Parameters:
        - id (int): The color ID.

        Returns:
        - str: ANSI escape code for the custom color.
        """
        return f'\033[38;5;{id}m'

    def list_custom_colors(self):
        """
        Prints a list of custom colors with their IDs.
        """
        for i in range(0, 256):
            print(f"\033[38;5;{i}m{int(i)}{Color.RESET}")


class BackColor:
    """
    A class to represent ANSI color codes for background colors.

    Attributes:
    - BLACK: ANSI escape code for black background
    - RED: ANSI escape code for red background
    - GREEN: ANSI escape code for green background
    - YELLOW: ANSI escape code for yellow background
    - BLUE: ANSI escape code for blue background
    - MAGENTA: ANSI escape code for magenta background
    - CYAN: ANSI escape code for cyan background
    - WHITE: ANSI escape code for white background
    - RESET: ANSI escape code to reset background color to default

    Methods:
    - custom(id): Returns a custom ANSI escape code based on the given color ID.
    - list_custom_colors(): Prints a list of custom background colors with their IDs.
    """

    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[0m'
    
    def custom(id):
        """
        Returns a custom ANSI escape code based on the given color ID.

        Parameters:
        - id (int): The color ID.

        Returns:
        - str: ANSI escape code for the custom color.
        """
        return f'\033[48;5;{id}m'
    
    def list_custom_colors(self):
        """
        Prints a list of custom background colors with their IDs.
        """
        for i in range(0, 256):
            print(f"{int(i)} \033[48;5;{i}m     {BackColor.RESET}")


