from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, ListProperty, ObjectProperty
from kivy.core.window import Window

from Plot.color_helper import Color


class Plot(ButtonBehavior, Widget):
    is_wall = BooleanProperty(False)
    plot_color = ListProperty(Color.IS_NOT_WALL.value)

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)

    def __init__(self, **kwargs):
        Window.bind(mouse_pos=self.is_hovered)
        Window.bind(on_touch_down=self.set_selection_type)
        Window.bind(on_touch_up=self.set_selection_type)
        super(Plot, self).__init__(**kwargs)

    def set_is_wall(self, *args):
        print(args)
        self.is_wall = not self.is_wall
        if self.is_wall:
            self.plot_color = Color.IS_WALL.value
        else:
            self.plot_color = Color.IS_NOT_WALL.value

    def is_hovered(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            if self.parent.multiple_select:
                self.set_is_wall()
            else:
                self.plot_color = Color.IS_HOVERED.value
        else:
            if self.is_wall:
                self.plot_color = Color.IS_WALL.value
            else:
                self.plot_color = Color.IS_NOT_WALL.value

    def set_selection_type(self, *args):
        click_info = args[0]
        try:
            if self.parent.hovered and click_info.button == "left":

                self.parent.multiple_select = not self.parent.multiple_select
        except AttributeError:
            pass
