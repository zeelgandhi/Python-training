class shark:
  def swim(self):
      print("I can swim")
  def swim_f(self):
      print("I can swim forward")
  def swim_b(self):
      print("I can swim backward")

class tiger:
    def swim(self):
        print("I cannot swim")
    def swim_f(self):
        print("I cannot swim forward")
    def swim_b(self):
        print("I cannot swim backward")

fish=shark() #fish is object of shark class
t=tiger()
for i in(fish,t):
    i.swim()
    i.swim_f()
    i.swim_b()
