from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# so we can easliy import numpad into the main file
Builder.load_file('simulation_settings.kv')


class SliderWithMultipliers(BoxLayout):
    slider_name = StringProperty('')
    value_string = StringProperty('')
    button1_name = StringProperty('')
    button1_multiplier = NumericProperty(1.0)
    button2_name = StringProperty('')
    button2_multiplier = NumericProperty(1.0)
    slider_range = ObjectProperty((1,100))
    slider_step = NumericProperty(1.0)
    slider_value = NumericProperty(1.0)
    multiplier_str = StringProperty('')
    multiplier_value = NumericProperty(1.0)

    #def __init__(self,**args):
    #    self.bind(slider_value = self.set_value_string)

    def set_value_string(self,instancce,value):
        self.value_string = num2str(self.slider_value) + self.multiplier_str
        
 
    def set_button1_multiplier(self):
        self.multiplier_str = self.button1_name
        self.multiplier = self.button1_multiplier
        # FIXME add behaviour of the value string
        #self.value_string = num2str(self.slider_value) + self.button1_name
        #self.slider_

    def set_button2_multiplier(self):
        pass
    
    
  

class SimulationSettings(BoxLayout):
    pass
   

class SimulationSettingsApp(App):
    def build(self):
        return SimulationSettings()
        
     
if __name__ == '__main__':  
    SimulationSettingsApp().run()
