"""
class IceCream:
  max_scoops = 3
  def __init__(self):
      super().__init__()
      self.scoops = 0

  def eat(self, scoops):
    if self.scoops <= scoops:
      print("Not enough bites left")
    else:
      self.scoops -= scoops
    
  def add(self, scoops):
      self.scoops += scoops
      if self.scoops > self.max_scoops:
        self.scoops = 0
        print("Too many scoops! Dropped ice cream.")

class IceCreamTruck:
  def __init__(self):
    super().__init__()
    self.sold = 0
  def order(self, scoops):
    ice_cream = IceCream()
    self.add(ice_cream, scoops)
    return ice_cream

  def add(self, ice_cream, scoops):
    ice_cream.add(scoops)
    self.sold += scoops

class DeluxeIceCreamTruck(IceCreamTruck):
  def order(self, scoops):
    ice_cream = super().order(scoops)
    ice_cream.add(1)
    return ice_cream


class Drinkable:

  def __init__(self):
    self.cups = 0

  def add(self, cups):
    self.cups += cups

  def drink(self, cups):
    self.cups -= cups

class Lemonade(Drinkable):
  pass

class MeltingIceCream(IceCream, Drinkable):
  def elapse(self, t):
    melted = min(t, self.scoops)
    self.scoops -= melted
    self.cups += melted
#--------------------------------------------------
def sub(x, y):
  return x - y

def sub2(x, y = 0):
  return x - y

class Light:
  def __init__(self, sync=None):
    super().__init__()
    self.on = False
    self.sync = sync
  def toggle(self):
    self.on = not self.on
    if self.sync is not None:
      self.sync.toggle()
      
  def is_on(self):
    return self.on

class OldLight(Light):
  def __init__(self, sync=None):
    super().__init__(sync=sync)
    self.on = False
    self.sync = sync
    self.flicker = False

  def toggle(self):
    super().toggle()
    if self.on:
      self.flicker = not self.flicker
#--------------------------------------------------
class Light:
  on = False

a = Light()
b = Light()
#--------------------------------------------------
class A:
  pass

class B(A):
  pass

class C(A, B):
  pass



#--------------------------------------------------

"""

# run on Replit to use console