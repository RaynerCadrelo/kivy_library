from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, ColorProperty
from kivy.metrics import dp


class LevelCircle(RelativeLayout):
    level = NumericProperty(0)
    level_stop = NumericProperty(100)
    level_color = ColorProperty((0.1, 0.1, 1))
    level_stop_color = ColorProperty((0.5, 0.5, 0.5))
    bg_level_color = ColorProperty((0.9, 0.9, .9))
    bg_color = ColorProperty((1, 1, 1))
    width_line = NumericProperty(dp(5))

    # levelcircle.levelcircle.PrimayLabel object.
    _primary_label = ObjectProperty()
    # levelcircle.levelcircle.SecondaryLabel object.
    _secondary_label = ObjectProperty()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, PrimaryLabel):
            self._primary_label = widget
        elif isinstance(widget, SecondaryLabel):
            self._secondary_label = widget
            widget.y = self._primary_label.y - widget.height  # posicioning secondary label
        if isinstance(widget, (PrimaryLabel, SecondaryLabel)):
            return super().add_widget(widget)
        

class PrimaryLabel(Label):
    pass


class SecondaryLabel(Label):
    pass
