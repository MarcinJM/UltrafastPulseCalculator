from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

# so we can easliy import numpad into the main file
Builder.load_file('simulation_settings.kv')


class SliderWithMultipliers(Widget):
    #FIXME would be best to inherit from Slider
    slider_name = StringProperty('')
    value_str = StringProperty('')
    button1_name = StringProperty('')
    button1_multiplier = NumericProperty(1.0)
    button1_step =  NumericProperty(1.0)
    button1_range =  ObjectProperty((1.0,100.0))
    button2_name = StringProperty('')
    button2_multiplier = NumericProperty(1.0)
    button2_step =  NumericProperty(1.0)
    button2_range =  ObjectProperty((1.0,100.0))
    multiplier_str = StringProperty('')
    multiplier_value = NumericProperty(1.0)

    def __init__(self,**kwargs):
        super(SliderWithMultipliers, self).__init__(**kwargs)
        # need to init ids before binding
        # workaround for binding in init
        Clock.schedule_once(self.init_ui, 0)
        
        
    def init_ui(self, dt=0):        
        self.ids['slider'].bind(value = self.set_value_string)
        # button1 pressed down in default        
        self.ids['slider'].range = self.button1_range
        self.ids['slider'].step = self.button1_step
        self.multiplier_str = self.button1_name        
        self.set_display()

    def set_display(self):
        self.value_str = str(self.ids['slider'].value) + ' ' + self.multiplier_str
        self.ids['slider_display'].text = self.value_str              
    

    def set_value_string(self,obj, value):
        self.set_display()        
        
 
    def set_button1_multiplier(self):
        self.multiplier_str = self.button1_name
        self.multiplier = self.button1_multiplier        
        self.ids['slider'].range = self.button1_range
        self.ids['slider'].value = self.ids['slider'].min
        self.ids['slider'].step = self.button1_step
        self.set_display()
      

    def set_button2_multiplier(self):
        self.multiplier_str = self.button2_name
        self.multiplier = self.button2_multiplier
        self.ids['slider'].range = self.button2_range
        self.ids['slider'].value = self.ids['slider'].min
        self.ids['slider'].step = self.button2_step
        self.set_display()


class ButtonDropDown(Button):
    pass

class MainButtonDropDown(Button):

    def __init__(self,**kwargs):
        super(MainButtonDropDown, self).__init__(**kwargs)   
        Clock.schedule_once(self.init_ui, 0)
        
        
    def init_ui(self, dt=0):
        self.drop_down = FiberDropDown()
        self.bind(on_release = self.drop_down.open)
       
    

class FiberDropDown(DropDown):
    #FIXME NOT FINISHED
    def __init__(self,**kwargs):
        super(FiberDropDown, self).__init__(**kwargs)
        for index in range(10):
            btn = ButtonDropDown(text='Value %d' % index)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.add_widget(btn)      
        #self.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        
class SimulationSettings(BoxLayout):
    pass
   

class SimulationSettingsApp(App):
    def build(self):
        return SimulationSettings()
        
     
if __name__ == '__main__':  
    SimulationSettingsApp().run()
