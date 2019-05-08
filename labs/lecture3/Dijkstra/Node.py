class Node:
    """
    class includes:
        1. Coordinate x and y
        2. Double weight
        3. int "name"
    """

    def __init__(self, x=0, y=0, weight=1, name=0):
        self.x = x                  # Coordinate x
        self.y = y                  # Coordinate y
        self.weight = weight        # weight
        self.name = name            # name
