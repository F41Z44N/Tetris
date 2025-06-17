class Colors:
    dark_grey = (26, 31, 40) # empty space

    green = (47, 230, 23) # L block
    red = (232, 18, 18) # J block
    orange = (226, 116, 17) # I block
    yellow = (237, 234, 4) # Square
    purple = (166, 0, 247) # S block
    cyan = (21, 204, 209) # T or W block
    blue = (13, 64, 216) # Z block

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
