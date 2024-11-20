class Fan:
    def __init__(self):
        self.brand="Usha"
        self.color="Black"
        self.cost=1500
        self.noOfBlades=3
    def on(self):
        print("Fan is on")
    def rotating(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is off")

f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.noOfBlades)
f1.on()
f1.rotating()
f1.off()

