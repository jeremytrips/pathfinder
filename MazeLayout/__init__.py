from kivy.lang import Builder
from .maze_layout import MazeLayout

print(f"Loading {__name__}")
Builder.load_file('MazeLayout/maze_layout.kv')
print(f"{__name__} loaded")
