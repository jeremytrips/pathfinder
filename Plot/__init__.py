from kivy.lang import Builder
from .plot import Plot

print(f"Loading {__name__}")
Builder.load_file('Plot/plot.kv')
print(f"{__name__} loaded")