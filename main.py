from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Root(BoxLayout):
	pass
	
class MainApp(App):
		def build(self):
			main = Root()
			return main
if __name__ == '__main__':
	MainApp().run()			
