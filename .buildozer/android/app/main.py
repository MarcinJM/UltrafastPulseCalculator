from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from numpad import Numpad
from power import PowerConversion
from pulse_interface import PulseInterface, Pulse



class MenuButton(Button):
    app = ObjectProperty(None)



         
class AppScreen(FloatLayout):
    app = ObjectProperty(None)


class BandwidthConversionScreen(BoxLayout,AppScreen):
    def __init__(self,**kwargs):
        super(BandwidthConversionScreen, self).__init__(**kwargs)        
        self.orientation = 'vertical'
        self.numpad = Numpad(size_hint=(1,0.4))
        self.pulse = Pulse()
        self.pulse_interface = PulseInterface(numpad = self.numpad,\
                             pulse = self.pulse, size_hint = (1,0.4))
        
        self.menu_button = MenuButton(app = self.app,size_hint=(1,0.1))
        self.add_widget(self.pulse_interface)
        self.add_widget(self.numpad)
        self.add_widget(self.menu_button)   


class PowerConversionScreen(BoxLayout,AppScreen):
    def __init__(self,**kwargs):
        super(PowerConversionScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.numpad = Numpad(size_hint=(1,0.5))
        self.power_conversion = PowerConversion(numpad =self.numpad,size_hint=(1,0.4))
        self.menu_button = MenuButton(app = self.app,size_hint=(1,0.1))
        self.add_widget(self.power_conversion)
        self.add_widget(self.numpad)
        self.add_widget(self.menu_button)
        


class NLSScreen(BoxLayout,AppScreen):
    def __init__(self,**kwargs):
        super(NLSScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'         
        self.menu_button = MenuButton(app = self.app,size_hint=(1,0.1))       
        self.add_widget(self.menu_button)
        

class MainMenu(AppScreen):
    pass

        
class PulseCalculatorApp(App):
    def build(self):
        self.screens = {}
        self.screens["menu"] = MainMenu(app = self)
        self.screens["bandwidth"] = BandwidthConversionScreen(app = self)
        self.screens["power"] = PowerConversionScreen(app = self)
        self.screens["nls"] = NLSScreen(app = self)
        self.root = FloatLayout()
        self.goto_screen("menu")

    def goto_screen(self, screen_name):
        self.root.clear_widgets()
        self.root.add_widget(self.screens[screen_name])

        
     
if __name__ == '__main__':
    PulseCalculatorApp().run()
