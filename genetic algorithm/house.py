class House():
  
  def __init__(self, x: int, y: int, name: str):
    self.x = x
    self.y = y
    self.name = name
      
  def distant(self, house: object):
    x = pow(house.x - self.x, 2)
    y = pow(house.y - self.y, 2)
    return int(pow(x + y, .5))
    #return abs(self.x - house.x) + abs(self.y - house.y)
  
  def __eq__(self, __o: object) -> bool:
    if __o == None: return False
    return self.x == __o.x and self.y == __o.y
    