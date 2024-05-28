class Agent:
    def __init__(self, pos: tuple[int]) -> None:
        self.pos = pos
        self.symbol = "A"

    def __str__(self):
        return f"Agent: {self.pos}"


class Door:
    def __init__(self, pos: tuple[int]) -> None:
        self.pos = pos
        self.symbol = "D"

    def __str__(self):
        return f"Door: {self.pos}"


class Obstacle:
    def __init__(self, pos: tuple[int]) -> None:
        self.pos = pos
        self.symbol = "O"

    def __str__(self):
        return f"Obstacle: {self.pos}"


class Spawner:
    def __init__(self, pos: tuple[int]) -> None:
        self.pos = pos
        self.symbol = "S"

    def __str__(self):
        return f"Spawner: {self.pos}"


class Wall:
    def __init__(self, pos: tuple[int]) -> None:
        self.pos = pos
        self.symbol = "W"

    def __str__(self):
        return f"Wall: {self.pos}"
