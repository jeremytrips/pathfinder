from kivy.properties import BooleanProperty, NumericProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


from Plot import Plot


class MazeGrid(GridLayout):
    multiple_select = BooleanProperty(False)

    number_of_cols = NumericProperty(5)
    number_of_rows = NumericProperty(5)

    has_start = BooleanProperty(False)
    has_end = BooleanProperty(False)

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)

    def __init__(self, **kwargs):
        Window.bind(mouse_pos=self.is_hovered)
        super(MazeGrid, self).__init__(**kwargs)

    def generate_maze(self, x, y):
        self.clear_widgets()
        self.number_of_cols = x
        self.number_of_rows = y
        for x in range(self.number_of_cols):
            for y in range(self.number_of_rows):
                print(f"{x}/{self.number_of_cols}, {y}/{self.number_of_rows}")
                self.add_widget(Plot())

    def is_hovered(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            return
        self.border_point = pos
        self.hovered = inside
