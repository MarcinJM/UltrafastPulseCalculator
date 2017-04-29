from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# so we can easliy import numpad into the main file
Builder.load_file('numpad.kv')


class NumpadInput(Label):
    numpad = ObjectProperty()
    name = StringProperty('')
    
    def __init__(self,**kwargs):
        super(NumpadInput, self).__init__(**kwargs)  
       
    def custom_setter(self,instance,value):
        self.text = self.numpad.input     
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):            
            self.numpad.active_input = self.name        
            self.numpad.clear_observers_of_input()         
            self.numpad.input = self.text
            self.numpad.bind(input = self.custom_setter)
            self.numpad.observers_of_input.append(self.custom_setter)
            

            
     
            
     

class Numpad(Widget):
   input = StringProperty('')
   # FIXME the two properties serve similar purpuse
   active_input = StringProperty() 
   observers_of_input = []

   # crude but works ... 
   def clear_observers_of_input(self):        
        for observer in self.observers_of_input:
            self.unbind(input=observer)      
   
 

class NumpadApp(App):
    def build(self):
        self.root = BoxLayout()
        self.root.orientation = 'vertical'
        self.numpad = Numpad()
        self.input1 = NumpadInput(numpad=self.numpad)
        self.input2 = NumpadInput(numpad=self.numpad)
        self.root.add_widget(self.input1)
        self.root.add_widget(self.input2)
        self.root.add_widget(self.numpad)
        
     
if __name__ == '__main__':  
    NumpadApp().run()
