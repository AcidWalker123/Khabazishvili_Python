import ast

class InputHandler:
    def __init__(self, value):
        self.value = value

    def process_inpt(self):
        if self.value.startswith('[') and self.value.endswith(']'):
            self.process_array()
        elif self.value.isdigit():
            self.process_number()
        else:
            self.process_name()

    def process_array(self):
        arr = ast.literal_eval(self.value)
        if isinstance(arr, list) and all(isinstance(x, int) for x in arr):
            multiples_of_3 = [x for x in arr if x % 3 == 0]
            print(multiples_of_3)
        else:
            print("Please enter a list of integers only!")

    def process_number(self):
        if self.value.isdigit() and int(self.value) > 7:
            print("Hello")
            return
        
    def process_name(self):
        if self.value == "John":
            print("Hello, John")
            return
        else:
            print("There is no such name")
            return
