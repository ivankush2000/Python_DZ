class user:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_first_name(self):
        return f"Имя: {self.first_name}"
    
    def say_last_name(self):
        return f"Фамилия: {self.last_name}"
    
    def say_f_l(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}"