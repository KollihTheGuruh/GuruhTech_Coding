import time
import sys

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  # You can adjust the speed of typing here
    print()

# Usage
typewriter_effect('''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math

class CalculatorApp(App):
    def build(self):
        Window.size = (350, 620)  # Width x Height in pixels, adjust as needed

        main_layout = GridLayout(cols=4, spacing=10)
        self.display = TextInput(multiline=False, readonly=True, halign="right", font_size=50)
        main_layout.add_widget(self.display)

        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "Del", "/",
            "sin", "cos", "tan", "√",
            "(", ")", "x²", "^",
            "="
        ]

        for button in buttons:
            btn = Button(text=button, pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=32)
            btn.bind(on_press=self.on_button_press)
            main_layout.add_widget(btn)

        return main_layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == "C":
            self.display.text = ""
        elif button_text == "Del":
            self.display.text = current[:-1]
        elif button_text == "=":
            try:
                self.display.text = str(eval(self.parse_expression(current)))
            except Exception:
                self.display.text = "Error"
        else:
            new_text = current + button_text
            self.display.text = new_text

    def parse_expression(self, expression):
        expression = expression.replace("^", "**")
        expression = expression.replace("√", "math.sqrt")
        for trig_func in ["sin", "cos", "tan"]:
            expression = expression.replace(trig_func, f"math.{trig_func}(math.radians")
            expression += ")" * expression.count(f"math.{trig_func}(math.radians")  # Close parentheses
        expression = expression.replace("x²", "**2")
        return expression

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()

''')
