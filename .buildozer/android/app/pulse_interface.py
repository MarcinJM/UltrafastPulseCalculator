from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from numpad import Numpad, NumpadInput


Builder.load_file('pulseinterface.kv')




class Pulse():
    def __init__(self,**kwargs): 
        self.fwhm = 200e-15 #[s]
        self.bandwidth = 200e-9 #[m]
        self.time_bandwidth_product = 0.315 #0.44 for gaussian
        self.c0 = 299792458;
        self.lam_center = 1.55e-6;

    def calculate_fwhm(self):        
        self.fwhm = self.time_bandwidth_product* \
                          self.lam_center**2/ \
                    (self.c0*self.bandwidth)
       

    def calculate_bandwidth(self):    
        self.bandwidth = self.time_bandwidth_product* \
                          self.lam_center**2/ \
                          (self.c0*self.fwhm) 


class PulseInterface(BoxLayout):
    numpad = ObjectProperty()
    pulse = ObjectProperty()
    active_input = StringProperty('')

    def __init__(self,**kwargs):
        super(PulseInterface, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui, 0)
        
        
    def init_ui(self, dt=0):
        self.set_all()

    def set_all(self):
        self.set_bandwidth()
        self.set_wavelength()
        self.set_fwhm()

    def set_bandwidth(self):
        self.ids['bandwidth'].text = str(round(self.pulse.bandwidth*1e9,0))

    def set_fwhm(self):
        self.ids['fwhm'].text = str(round(self.pulse.fwhm*1e15,0))
        
    def set_wavelength(self):
        self.ids['wavelength'].text = str(round(self.pulse.lam_center*1e9,0))
        

    def set_soliton(self):
        self.numpad.active_input = ''
        self.pulse.time_bandwidth_product = 0.315
        # keep fwhm recalculate bandwidth
        self.pulse.calculate_bandwidth()
        self.set_bandwidth()        
        

    def set_gaussian(self):
        self.numpad.active_input = ''        
        self.pulse.time_bandwidth_product = 0.44
        # keep fwhm recalculate bandwidth
        self.pulse.calculate_bandwidth()
        self.set_bandwidth()

    def update_wavelength(self):
        try:
            self.pulse.lam_center = float(self.ids['wavelength'].text)*1e-9
            # keep fwhm recalculate bandwidth
            self.pulse.calculate_bandwidth()
            self.set_bandwidth()
        except:
            pass

    def update_fwhm(self):
        try:            
            if self.numpad.active_input == 'fwhm':
                self.pulse.fwhm = float(self.ids['fwhm'].text)*1e-15
                self.pulse.calculate_bandwidth()
                self.set_bandwidth()
            else:
                pass
        except:
            pass  #this is needed for initilization

    def update_bandwidth(self):
        try:
            if self.numpad.active_input == 'bandwidth':                
                self.pulse.bandwidth = float(self.ids['bandwidth'].text)*1e-9    
                self.pulse.calculate_fwhm()
                self.set_fwhm()
            else:
                pass
                
        except:           
            pass  #this is needed for initilization    



 

class PulseInterfaceApp(App):
    def build(self):
        self.root = BoxLayout()
        self.root.orientation = 'vertical'
        from numpad import Numpad
        self.pulse = Pulse()
        self.numpad = Numpad(size_hint =  (1.0,0.5))
        self.pulse_interface = PulseInterface(numpad = self.numpad,\
                                              pulse = self.pulse,\
                                              size_hint = (1.0,0.5))       
        self.root.add_widget(self.pulse_interface)     
        self.root.add_widget(self.numpad)
        
     
if __name__ == '__main__':  
    PulseInterfaceApp().run()


