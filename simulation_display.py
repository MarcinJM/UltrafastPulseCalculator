from math import sin, pi
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock

Builder.load_file('simulation_display.kv')

class SimulationDisplay(Widget):
    slider_range = ObjectProperty((20.0,100.0))
    slider_step = NumericProperty((1.0))
    
    def __init__(self,**kwargs):
        super(SimulationDisplay,self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui, 0)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])        
        
    def init_ui(self, dt=0):        
        self.ids['slider'].bind(value = self.replot)
        self.ids['slider'].range = self.slider_range
        self.ids['slider'].step = self.slider_step
        self.make_plot()


    def replot(self,obj, value):
        self.make_plot()
        

    def make_plot(self):
        period = self.ids['slider'].value
        self.plot.points = [(x, sin(2.0*pi*x/period)) for x in range(0, 101)]
        self.ids['graph'].add_plot(self.plot)
    
if __name__ == '__main__':
    
    class SimulationDisplayApp(App):
        def build(self):
	    return SimulationDisplay()
    
    SimulationDisplayApp().run()
