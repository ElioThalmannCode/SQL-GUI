from pydblite import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.instructions import Canvas
from kivy.uix.boxlayout import *

db = Base('customers.pdl')
db.create('first_name', 'last_name', 'age', mode="open")

class ClearApp(App):

    def build(self):
        self.site = self.box = BoxLayout(orientation="vertical")
        self.box = BoxLayout(orientation='horizontal', minimum_height=(.5,1))
        self.txt = TextInput(hint_text='Vorname', size_hint=(.5,.1))
        self.txt2 = TextInput(hint_text='Nachname', size_hint=(.5,.1))
        self.txt3 = TextInput(hint_text='Alter', size_hint=(0.1,.1))
        self.btn = Button(text='Erstellen', on_press=self.submit, size_hint=(.5,.1))
        self.box.add_widget(self.txt)
        self.box.add_widget(self.txt2)
        self.box.add_widget(self.txt3)
        self.box.add_widget(self.btn)
        for i in db:
            self.site.add_widget(Label(text=f"Vorname={i['first_name']}  Nachname={i['last_name']}  Alter={i['age']}", size_hint=(1,.1)))
        self.site.add_widget(self.box)

        return self.site

    def submit(self, instance):
        if self.txt.text == "" or self.txt2.text == "" or self.txt3.text == "":
            print("ERROR: One field is empty!")
        else:
            db.insert(self.txt.text, self.txt2.text, self.txt3.text)
ClearApp().run()
