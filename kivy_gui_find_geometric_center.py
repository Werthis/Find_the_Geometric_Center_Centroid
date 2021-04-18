import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty

import find_geometric_center as find_geo

class GeometricCenterGrid(Widget):
    arabic_number = ObjectProperty(None)
    geometric_number = StringProperty()

    def __init__(self, backend, *args, **kwargs):
        super(GeometricCenterGrid, self).__init__(*args, **kwargs)
        self._backend = backend
        self.geometric_number = 'Here comes your number!'

    def get_number_from_user(self):
        self.number_to_convert = self.arabic_number.text
        return self.number_to_convert
    
    def request(self):
        self.get_number_from_user()
        number_to_convert = self._backend.gui_cumunication(self.number_to_convert)
        self.geometric_number = str(number_to_convert)
        self.arabic_number.text = ''

class GeometricCenterApp(App):

    def __init__(self, backend):
        super(GeometricCenterApp, self).__init__()
        self._backend = backend

    def build(self):
        return GeometricCenterGrid(self._backend)

    def start_app(self):
        GeometricCenterApp(self._backend).run()                


if __name__ == '__main__':
    list_of_points = [(1, 11), (2, 2), (5, 1), (1, 1)]
    backend = find_geo.GeometricCenter(list_of_points)
    app = GeometricCenterApp(backend)
    app.start_app()
