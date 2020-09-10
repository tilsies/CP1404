from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934


class MilesKmConverter(App):

    def build(self):
        self.title = "Miles to Km Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def calculate(self):
        value = self.get_validated_miles()
        result = value * CONVERSION
        self.root.ids.output_label.text = str(result)

    def change(self, difference):
        value = self.get_validated_miles() + difference
        self.root.ids.input_miles.text = str(value)
        self.calculate()


MilesKmConverter().run()
