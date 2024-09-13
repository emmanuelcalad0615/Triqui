from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class TriquiApp(App):

    def build(self):
        tablero = GridLayout(rows = 3, cols = 3)
        self.count_click = True 

        for i in range(0, 9):
            casilla1 = Button(text = f" ", font_size = 40)
            casilla1.bind(on_press = self.jugar)
            tablero.add_widget(casilla1)

        return tablero
    
    def jugar(self, sender): 
        if sender.text == " ":

            if self.count_click:
                sender.text = "X"
                self.count_click = False
                 
            else:
                sender.text = "O"  
                self.count_click = True  
         




if __name__ == "__main__":
    triqui = TriquiApp()
    triqui.run()