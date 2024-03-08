import argparse

class Arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = "Umbrella",
            description = "🌂 Scan website vulnerabilities",
            epilog = "If you need more help: https://github.com/Neotoxic-off"
        )
        self.args = None

        self.__load__()

    def __load__(self):
        self.parser.add_argument(
            "-w",
            "--website",
            action = "store",
            type = str,
            required = True
        )

        self.args = self.parser.parse_args()

    def get(self, arg):
        return (getattr(self.args, arg, None))
