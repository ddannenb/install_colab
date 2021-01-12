class AnApi:
    def __init__(self, echo: str):
        self.echo = echo

    def do_something(self, doit: bool):
        if doit:
            print(f"Hello {self.echo}")
        else:
            print("I am not doing anything")