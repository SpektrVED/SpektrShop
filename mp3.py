from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader,Sound
from kivy.lang import Builder
from kivy.clock import Clock


Builder.load_string('''
<MenuPage>:
    BoxLayout:
        orientation:'vertical'
        Button:
            text:'Горизонтальная синяя линяя'
        Label:
        	text: 'хуй'
        ProgressBar:
            id: myProgressBar
            value: .0
            min: 0
            max: 1
            pos_hint: {'x':.1}
            size_hint_x: .8

        BoxLayout:
            orientation:'horizontal'
            Button:
	            text:'Play'
	            on_press:root.plays()
	        Button:
	            text:'NextR'
	            on_press:root.progr()
	        Button:
	            text:'NextL'
''')

class MenuPage(Screen):
    M = SoundLoader.load('C:/Users/ярик/Desktop/mp3/mytest.mp3')

    def plays(self):
        if MenuPage.M.state == 'stop':
            MenuPage.M.play()
        else:
            MenuPage.M.stop()
    def progr(self):
    	print('qwe')
    	self.ProgressBar.value == 25
    	#if self.value < 100:
    	#	self.value =+ 1




sm = ScreenManager()
menu = MenuPage(name='menu')
sm.add_widget(menu)


class TestApp(App):
    def build(self):
        return sm




TestApp().run()