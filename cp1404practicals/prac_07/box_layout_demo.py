from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear(self):
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""

if __name__ == '__main__':
    box_layout_demo = BoxLayoutDemo()
    box_layout_demo.run()
