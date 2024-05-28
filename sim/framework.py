from sim.board import Board


class Framework:
    def __init__(self, board) -> None:
        self.board = board

    def simulate(self, SF, DF, update_rule, num_steps: int) -> list[Board]:
        return [self.board]
