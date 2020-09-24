from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window

import Plot
import MazeLayout
import MazeGrid

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MazeApp(App):
    title = "Maze"



if __name__ == "__main__":
    MazeApp().run()
