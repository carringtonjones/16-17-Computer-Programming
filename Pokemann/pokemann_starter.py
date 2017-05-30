import random
#import math

"""power = 8
defense = 7
stab = 0.33
critical_damage = random.uniform(1.9000, 1.9999)


crit=random.uniform(0,1)

if crit <= 0.0625:
  movepower = float(4.0)
  damage = 2 * 5.0 + 2 * movepower * power / defense + 2 * critical_damage + (movepower*stab)
  print(round(damage))
else: 
  movepower = float(4.0)
  damage = 2 * 5.0 + 2 * movepower * power / defense  + 2 + (movepower*stab)
  print(round(damage))"""

class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file

        self.fainted = False

    def execute_move(self, move, target):
        damage = move.get_damage(self, target)
        target.take_damage(damage)
        

    def apply_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.health = 0
            target.fainted = True

    def draw(self):
        pass


class Move:

    def __init__(self, name, kind, powerpoint, power, accuracy):

        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

    def get_effectiveness(self, target):
        if self.kind == 'student' and target.kind == 'teacher':
            effectiveness = 2.0
        elif self.kind == 'student' and target.kind == 'admin':
            effectiveness = 0.5
        elif self.kind == 'student' and target.kind == 'student':
            effectiveness == 1.0
        elif self.kind == 'admin' and target.kind == 'teacher':
            effectiveness = 0.5
        elif self.kind == 'admin' and target.kind == 'student':
            effectiveness = 2.0
        elif self.kind == 'admin' and target.kind == 'admin':
            effectiveness == 1.0
        elif self.kind == 'teacher' and target.kind == 'teacher':
            effectiveness = 1.0
        elif self.kind == 'teacher' and target.kind == 'student':
            effectiveness = 0.5
        elif self.kind == 'teacher' and target.kind == 'admin':
            effectiveness == 2.0
        else:
            effectiveness = 1.0
        return effectiveness


            
    def get_damage(self, attacker, target):
        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.get_effectiveness(target)

        return p * a / d * e
    

if __name__ == '__main__':

    # Make some moves
    homework = Move("Homework", "teacher", 30, 40, 100)
    pop_quiz = Move("Pop quiz", "teacher", 30, 40, 100)
    lecture = Move("Lecture", "teacher", 30, 40, 100)
    dress_code = Move("Dress Code", "administrator", 30, 50, 95)
    id_violation = Move("ID Violation", "administrator", 30, 50, 95)
    excessive_talking = Move("Excessive Talking", "student", 30, 40, 100)
    disruptive_behavior = Move("Disruptive Behavior", "student", 30, 40, 100)

    # Create some Pokemann(s)
    coopasaur = Pokemann("coopasaur", "teacher", 30, 20, 50, 30, [homework, pop_quiz, id_violation], "coopasaur.png")
    mayfieldarow = Pokemann("mayfieldarow", "administrator", 30, 20, 50, 30, [dress_code, id_violation, lecture], "mayfieldarow.png")
    andrewag = Pokemann("andrewag", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "andrewag.png")



