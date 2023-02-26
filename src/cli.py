import cmd


class MyCLI(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = "stranger"
        else:
            name = args
        print(f"Hello, {name}")

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == "__main__":
    prompt = MyCLI()
    prompt.cmdloop("Starting cli...")
