from dog import Dog


class Dog_Owner:

    def __init__(self):
        self.dog = Dog("Richard", "border collie", 6, "black and white")


owner = Dog_Owner()
print(owner.dog)
