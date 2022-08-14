class Step_1 (Step):
    def __init__ (self, parent, name):
        self.content = MDFileReader (parent, name)
