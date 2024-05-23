class Light:
  def __init__(self):
    self.on = False
  def toggle(self):
    self.on = not self.on
  def is_on(self):
    return self.on
  

"""
class Light:
  on = False

a = Light()
b = Light()
"""