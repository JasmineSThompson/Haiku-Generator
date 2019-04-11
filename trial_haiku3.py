import kivy
kivy.require("1.9.1")
import haiku2
import random

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.textinput import TextInput

def callback(instance):
    print("The button <%s> is being pressed." % instance.text)

class Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.cols = 2
        
        self.button1 = Button(text="Line 1", font_size=28, background_normal="", background_color=[1, 0, 0, 0.9], width=250, size_hint_x=None)
        self.button1.bind(on_press=self.count1)
        self.add_widget(self.button1)
        self.label1 = Label(text=haiku2.allWriteLine(random.randint(2, 3), 5, False), font_size=28)
        self.add_widget(self.label1)

        self.button2 = Button(text="Line 2", font_size=28, background_normal="", background_color=[0, 1, 0, 0.7], width=250, size_hint_x=None)
        self.button2.bind(on_press=self.count2)
        self.add_widget(self.button2)
        self.label2 = Label(text=haiku2.allWriteLine(random.randint(2, 3), 6, False), font_size=28)
        self.add_widget(self.label2)
        
        self.button3 = Button(text="Line 3", font_size=28, background_normal="", background_color=[0, 0, 1, 0.9], width=250, size_hint_x=None)
        self.button3.bind(on_press=self.count3)
        self.add_widget(self.button3)
        self.label3 = Label(text=haiku2.allWriteLine(random.randint(2, 3), 5, True), font_size=28)
        self.add_widget(self.label3)
    def count1(self, instance):
        #print("count1")
        #print(haiku2.allWriteLine(2, 5))
        self.remove_widget(self.label1)
        self.label1 = Label(text=haiku2.allWriteLine(random.randint(2, 3), 5, False), font_size=28)
        self.add_widget(self.label1, 4)
    def count2(self, instance):
        #print("count1")
        #print(haiku2.allWriteLine(2, 5))
        self.remove_widget(self.label2)
        self.label2 = Label(text=haiku2.allWriteLine(random.randint(2, 3), 6, False), font_size=28)
        self.add_widget(self.label2, 2)
    def count3(self, instance):
        #print("count3")
        self.remove_widget(self.label3)
        self.label3 = Label(text=haiku2.allWriteLine(random.randint(2, 3), 5, True), font_size=28)
        self.add_widget(self.label3)

class Haiku(App):

    def build(self):
        return Screen()

    

if __name__ == "__main__":
    Haiku = Haiku()
    Haiku.run()
