class Color:
    def __init__(self, color) -> None:
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def ancho(self, color):
        self._color = color

    def __str__(self) -> str:
        return f'Color: {self._color}'
