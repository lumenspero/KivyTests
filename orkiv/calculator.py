import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, ObjectProperty, StringProperty, NumericProperty

class Screen(TextInput):
    pass

class Calculator(BoxLayout):

    function_btns = ListProperty(['+', '-', '*', '/', '^', 'Mem <-', 'Mem ->', 'Clear'])
    digit_btns = ListProperty(['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '+/-'])
    eval_string = StringProperty() # one of these strings is probably unnecessary
    calc_string = StringProperty()
    result = NumericProperty(0)

    def build_calc(self):
        # add screen textinput
        #self.add_widget(Screen(text='0', multiline=False, on_calc_string=self.screen_callback))

        scr = Screen(text='0', multiline=False)
        self.add_widget(scr)
        self.bind(calc_string=scr.setter('text'))

        #create inner boxlayout to hold 2 button gridlayouts
        main_buttons_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.75))

        # create 2 button gridlayouts
        digit_grid = GridLayout(cols=3, rows=4, size_hint=(0.5, 1))
        function_grid = GridLayout(cols=1, size_hint=(0.5, 1))

        # populate grids with buttons
        for i in self.digit_btns:
            digit_grid.add_widget(Button(text=str(i), on_press=self.button_callback))

        for f in self.function_btns:
            function_grid.add_widget(Button(text=str(f), on_press=self.button_callback))

        # add grids to inner boxlayout
        main_buttons_box.add_widget(digit_grid)
        main_buttons_box.add_widget(function_grid)

        # add inner boxlayout to main grid(root)
        self.add_widget(main_buttons_box)

        # finally, add boxlayout at bottom of main grid and insert equals btn
        equals_box = BoxLayout(size_hint=(1, 0.25))
        equals_box.add_widget(Button(text='=', on_press=self.button_callback))
        self.add_widget(equals_box)

    def button_callback(self, instance):
        value = instance.text
        if value == '=':
            try:
                self.result = eval(self.eval_string)
                self.calc_string = str(self.result)
                self.eval_string = ''
            except SyntaxError:
                self.calc_string = 'Error: Invalid Input'
        else:
            self.eval_string += value
            self.calc_string = self.eval_string

        print self.calc_string

    def screen_callback(self, instance):
        instance.text = self.calc_string # not working
        print 'seeing this!!!' # not working


class CalcApp(App):

    def build(self):
        calc = Calculator()
        calc.build_calc()
        return calc

if __name__ == '__main__':
    CalcApp().run()