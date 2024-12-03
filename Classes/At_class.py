class Player:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email

class Wizard(Player):
    def __init__(self, type_of_magic, name, email):
        Player.__init__(self, name, email)
        self.type_of_magic = type_of_magic

    def do_magic(self):
        return "Fireball"
    
class Elf(Player):
    
    def __init__(self, arrows):
        self.arrows = arrows
