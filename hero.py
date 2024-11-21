class Hero:
    def __init__(self):
        self.name="AA"
        self.age=52
        self.add="tg"
        self.noOfMovies=38

    def act(self):
        print("Actor is acting")
    def dance(self):
        print("Actor is dancing")

h1=Hero()
print(h1.name)
print(h1.age)
print(h1.add)
print(h1.noOfMovies)
h1.age=43
h1.add="Hyderabad"
h1.noOfHits=10
h1.height="6'1"
print(h1.name)
print(h1.age)
print(h1.add)
print(h1.noOfMovies)
print(h1.noOfHits)
print(h1.height)
h2=h1
h3=h2
h2.dance()
