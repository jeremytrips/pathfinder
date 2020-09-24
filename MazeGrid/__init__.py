from kivy.lang import Builder
from .maze_grid import MazeGrid

print(f"Loading {__name__}")
Builder.load_file('MazeGrid/maze_grid.kv')
print(f"{__name__} loaded")