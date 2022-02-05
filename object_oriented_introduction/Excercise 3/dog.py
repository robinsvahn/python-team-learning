class Dog:

    def __init__(self, name, breed, age, colour):
        self.name = name
        self.breed = breed
        self.age = age
        self.colour = colour

    # def __str__(self) -> str:
    #     return "Namnet hunden är {} namnet på rasen är {}, det är följande typ {}. Denna krabat är {} år gammal och i färgen {}".format(self.namnet, self.rasen, self.typen, self.åldern, self.färgen)

    def __str__(self) -> str:
        return f"The dog {self.name} is a {self.colour} {self.breed} which is {self.age} years old"
