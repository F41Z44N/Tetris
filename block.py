from colors import Colors
import pygame
from position import Position
import copy

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, is_shadow=False):
        shadow_color = (50, 50, 50)
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 11, tile.row * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
            color_to_draw = shadow_color if is_shadow else self.colors[self.id]
            pygame.draw.rect(screen, color_to_draw, tile_rect)

    def copy(self):
        new_block = Block(self.id)
        new_block.cells = copy.deepcopy(self.cells)
        new_block.rotation_state = self.rotation_state
        new_block.row_offset = self.row_offset
        new_block.column_offset = self.column_offset
        return new_block