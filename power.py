from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from math import log10

Builder.load_file('powerconversion.kv')


class PowerConversion(BoxLayout):
    numpad = ObjectProperty() 


    def update_dB(self):
        input_power = self.ids['input_power'].text
        output_power = self.ids['output_power'].text
        try:
           dB = 10*log10(float(input_power)/float(output_power))
           self.ids['dB'].text = str(round(dB,1))
	except:
            self.ids['dB'].text = 'Error'
    
