class ConsolePrinter:
    @staticmethod
    def print_blue(text):
        print(f"\033[94m{text}\033[0m")

    @staticmethod
    def print_red(text):
        print(f"\033[91m{text}\033[0m")

    @staticmethod
    def print_orange(text):
        print(f"\033[93m{text}\033[0m")

    @staticmethod
    def print_purple(text):
        print(f"\033[95m{text}\033[0m")

    @staticmethod
    def print_green(text):
        print(f"\033[92m{text}\033[0m")

    @staticmethod
    def print_bold(text):
        print(f"\033[1m{text}\033[0m")

    @staticmethod
    def print(text):
        print(text)

    @staticmethod
    def print_underline(text):
        print(f"\033[4m{text}\033[0m")
