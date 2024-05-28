from sim.objects import Wall, Agent, Door, Obstacle, Spawner


class Board:
    def __init__(self) -> None:
        self._objects = {}
        self._is_architecture_baked = False
        self._is_populated = False

    def add(self, obj):
        if self._is_populated:
            print("Already populated")
            return

        if self._is_architecture_baked:
            if not isinstance(obj, Agent):
                print("Architecture already baked")
                return
            if obj.pos not in self._objects:
                print(f"{obj.pos} is not available for agents (not on Board)")
                return

            if any(isinstance(item, Wall) for item in self._objects[obj.pos]):
                print(f"{obj.pos} is not available for agents (Wall)")
                return

            if any(isinstance(item, Obstacle) for item in self._objects[obj.pos]):
                print(f"{obj.pos} is not available for agents (Obstacle)")
                return

        else:
            if isinstance(obj, Agent):
                print("Architecture not baked jet")
                return

        if obj.pos in self._objects:
            self._objects[obj.pos].append(obj)
        else:
            self._objects[obj.pos] = [obj]

    def get_objects(self):
        return self._objects

    def bake_architecture(self):
        max_x, max_y, min_x, min_y = 0, 0, 0, 0

        for obj_pos in self._objects:

            x, y = obj_pos

            if any(isinstance(item, Wall) for item in self._objects[obj_pos]):

                if x > max_x:
                    max_x = x

                if y > max_y:
                    max_y = y

                if x < min_x:
                    min_x = x

                if y < min_y:
                    min_y = y

            else:

                if x > max_x:
                    max_x = x+1

                if y > max_y:
                    max_y = y+1

                if x < min_x:
                    min_x = x-1

                if y < min_y:
                    min_y = y-1

        string = ""

        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if (x, y) not in self._objects:
                    self._objects[(x, y)] = []

                cell = self._objects[(x, y)]

                if len(cell) == 0 and (x in [max_x, min_x] or y in [max_y, min_y]):
                    cell.append(Wall((x, y)))

                if len(cell) == 0:
                    string += " "

                elif len(cell) == 1:
                    string += cell[0].symbol

                else:
                    string += str(len(cell))

            string += "\n"

        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y

        self._architecture_str = string
        self._is_architecture_baked = True

    def populate(self):
        if not self._is_architecture_baked:
            print("Architecture not baked jet")
            return

        max_x = self.max_x
        min_x = self.min_x
        max_y = self.max_y
        min_y = self.min_y

        string = ""

        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):

                cell = self._objects[(x, y)]

                if len(cell) == 0:
                    string += " "

                elif len(cell) == 1:
                    string += cell[0].symbol

                else:
                    string += str(len(cell))

            string += "\n"

        self._populated_str = string
        self._is_populated = True

        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if len(self._objects[(x, y)]) == 0:
                    del self._objects[(x, y)]

    def __str__(self):
        if self._is_populated:
            return self._populated_str
        elif self._is_architecture_baked:
            return self._architecture_str
        else:
            return "Architecture not baked jet"
