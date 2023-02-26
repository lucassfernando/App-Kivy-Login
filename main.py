from kivymd.app import MDApp
from kivy.lang import Builder


class MyApp(MDApp):
    
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('file.kv')
    
MyApp().run()