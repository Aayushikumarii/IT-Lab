class Question4:
    str = ""
    def get_String(self):
        self.str = input('Enter a string: ')
    def print_String(self):
        print(self.str.upper())
question4 = Question4()
question4.get_String()
question4.print_String()