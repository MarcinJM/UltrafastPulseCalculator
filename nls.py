from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from numpad import Numpad, NumpadInput


Builder.load_file('nls_input.kv')



 

class PulseInterfaceApp(App):
    def build(self):
        self.root = BoxLayout()
        self.root.orientation = 'vertical'
        from numpad import Numpad
        self.pulse = Pulse()
        self.numpad = Numpad(size_hint =  (1,0.5))
        self.pulse_interface = PulseInterface(numpad = self.numpad,\
                                              pulse = self.pulse,\
                                              size_hint = (1,0.5))       
        self.root.add_widget(self.pulse_interface)     
        self.root.add_widget(self.numpad)
        
     
if __name__ == '__main__':  
    PulseInterfaceApp().run()







