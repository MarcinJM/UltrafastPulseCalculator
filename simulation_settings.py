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
from functools import partial
from nls import SimulationParameters


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
    simulation_parameters = ObjectProperty()

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
        self.update_simulation_parameters()

    def update_simulation_parameters(self):
        pass
       

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
    simulation_parameters = ObjectProperty()

    def __init__(self,**kwargs):
        super(MainButtonDropDown, self).__init__(**kwargs)   
        Clock.schedule_once(self.init_ui, 0)
        
    def init_ui(self, dt=0):
        self.drop_down = FiberDropDown(main_button = self)
        self.bind(on_release = self.drop_down.open)
        #FIXME should be possible from FiberDropDown
        self.bind(text = self.set_fiber_type)

    def set_fiber_type(self,instance,value):
        self.simulation_parameters.fiber = self.text

        

class FiberDropDown(DropDown):
    main_button = ObjectProperty()
    #FIXME
    #need external storage
    # need to display fiber parameters
    
    fibers = ['SMF', 'DCF', 'HNLF', 'Er80-8/125']
  
    
    def __init__(self,**kwargs):
        super(FiberDropDown, self).__init__(**kwargs)
        for fiber in self.fibers:
            btn = ButtonDropDown(text=fiber)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.add_widget(btn)
            self.bind(on_select=lambda instance, fiber: \
                      setattr(self.main_button, 'text', fiber))
        
 
class PulsePowerSlider(SliderWithMultipliers):
    # parsing problems when defined in kv file 
    # the parser neglects python defenition of class ...
    slider_name = StringProperty('Peak Power')
    button1_name = StringProperty('W')
    button1_multiplier = NumericProperty(1.0)
    button1_step =  NumericProperty(10.0)
    button1_range =  ObjectProperty((10.0,3000.0))
    button2_name = StringProperty('kW')
    button2_multiplier = NumericProperty(1000.0)
    button2_step =  NumericProperty(1.0)
    button2_range =  ObjectProperty((1.0,100.0))
    
    def update_simulation_parameters(self):
        self.simulation_parameters.peak_power = \
            self.ids['slider'].value*self.multiplier_value
        
        

class FiberLengthSlider(SliderWithMultipliers):
    slider_name = StringProperty('Fiber Length')
    button1_name = StringProperty('cm')
    button1_multiplier = NumericProperty(1e-2)
    button1_step =  NumericProperty(1.0)
    button1_range =  ObjectProperty((1.0,300.0))
    button2_name = StringProperty('m')
    button2_multiplier = NumericProperty(1.0)
    button2_step =  NumericProperty(1.0)
    button2_range =  ObjectProperty((1.0,1000.0))

    def update_simulation_parameters(self):
        self.simulation_parameters.fiber_length = \
            self.ids['slider'].value*self.multiplier_value
    
class PulseWidthSlider(SliderWithMultipliers):
    slider_name = StringProperty('Pulse Width')
    button1_name = StringProperty('fs')
    button1_multiplier = NumericProperty(1e-15)
    button1_step =  NumericProperty(1.0)
    button1_range =  ObjectProperty((10.0,3000.0))
    button2_name = StringProperty('ps')
    button2_multiplier = NumericProperty(1e-12)
    button2_step =  NumericProperty(1.0)
    button2_range =  ObjectProperty((1.0,100.0))
    
    def update_simulation_parameters(self):
        self.simulation_parameters.pulse_width = \
            self.ids['slider'].value*self.multiplier_value
        

class SimulationSettings(BoxLayout):
    simulation_parameters = ObjectProperty()
    pass
        
        
class SimulationSettingsApp(App):
    def build(self):
        self.simulation_parameters = SimulationParameters()
        return SimulationSettings(simulation_parameters =
                                  self.simulation_parameters)
        
if __name__ == '__main__':  
    SimulationSettingsApp().run()
