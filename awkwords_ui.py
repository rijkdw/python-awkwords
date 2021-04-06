import tkinter as tk

from awkwords_instance import AwkwordsInstance


class AwkwordsUI:

    def __init__(self):
        self.window = tk.Tk()

        self.category_input_header = tk.Label(self.window, text="Categories")
        self.category_input_header.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.category_input_widget = tk.Text(self.window, width=65, height=15)
        self.category_input_widget.grid(row=1, column=0, padx=10)

        self.main_string_header = tk.Label(self.window, text="Main string")
        self.main_string_header.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

        self.main_string_input_widget = tk.Entry(self.window, width=58)
        self.main_string_input_widget.grid(row=3, column=0, padx=10)

        self.button_generate = tk.Button(self.window, text="GENERATE", command=self.event_button_generate_pressed, width=40)
        self.button_generate.grid(row=4, column=0, pady=10)

        self.output_header = tk.Label(self.window, text="Output")
        self.output_header.grid(row=5, column=0, pady=10, padx=10, sticky=tk.W)

        self.output_widget = tk.Text(self.window, width=65, height=10)
        self.output_widget.grid(row=6, column=0, padx=10, pady=10)

        self.window.mainloop()

    @property
    def get_categories_raw(self) -> str:
        return self.category_input_widget.get("1.0", tk.END)[:-1]

    @property
    def get_categories(self) -> dict:
        categories = {}
        for line in self.get_categories_raw.splitlines():
            if not (len(line.strip()) == 0 or '=' not in line):
                name, body = line.strip().split('=')
                categories[name] = body
        AwkwordsInstance.validate_categories(category_dict=categories)
        return categories

    @property
    def get_main_string(self):
        return self.main_string_input_widget.get()

    @property
    def get_number_to_generate(self):
        return 10

    def event_button_generate_pressed(self):
        instance = AwkwordsInstance(category_dict=self.get_categories, main_string=self.get_main_string)
        words = instance.generate(number_words=self.get_number_to_generate)
        self.output_widget.delete("1.0", tk.END)
        self.output_widget.insert("1.0", '\n'.join(words))


if __name__ == '__main__':
    ui = AwkwordsUI()
