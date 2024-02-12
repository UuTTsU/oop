class Heart():
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 70:
            return 'high blood preasure'
        else:
            return 'feeling good'


class Brain:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 90:
            return 'tired'
        else:
            return 'rested'


class Leg:
    def __init__(self, moving_speed):
        self.moving_speed = moving_speed

    @property
    def running(self):
        if self.moving_speed > 10:
            return 'running'
        elif self.moving_speed == 0:
            return 'standing'
        else:
            return 'Walking'


class Person:
    def __init__(self, heart_usage, brain_usage):
        self.heart = Heart(heart_usage)
        self.brain = Brain(brain_usage)
        self.leg = None

    def leg_runtime(self, leg):
        self.leg = leg


# Example usage:
person = Person(80, 91)
leg = Leg(0)
person.leg_runtime(leg)

print(person.__dict__)
print(person.leg.running)
print(person.heart.state)
print(person.brain.state)
