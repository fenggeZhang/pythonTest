#继承
class parent():
    def print_last_name(self):
        print("apple")


class child(parent):
    def print_first_name(self):
        print("orange")


obj = child()
obj.print_first_name()
obj.print_last_name()
