class Pet():

    def __init__(self, name):
        self.name = susan
        self.energy = 10
        self.is_alive = True
        
    def sleep(self):
        if self.is_alive:
           print(self.name +" goes 'zzzzz....'")
           self.energy = 10
        else:
                print("Error: " + self.name + "is dead!")
        
    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'nom nom nom'")
        self.energy += 2
        
    else:
    print(self.name +" goes 'nom nom nom' on brains!")
      def play(self):
      print(self.name +" says 'yippee!"
      elf.energy -= 2

        if self.energy <= 0:
            self.die()

    def speak(self, words):
        print(self.name +" says '" + words + "'")

    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.die()

    def die(self):
        print(self.name +" writes 'aaarrrrrrrrrrgggggggggggggg!!!!!!!!' and die")
        self.is_alive = False
